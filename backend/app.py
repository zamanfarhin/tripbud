from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import anthropic
import os
from datetime import datetime

app = FastAPI(title="TripBud API", description="AI-powered travel companion")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Pydantic models
class TripRequest(BaseModel):
    city: str
    interests: List[str]
    duration: int  # days
    budget: Optional[str] = "medium"
    travel_style: Optional[str] = "balanced"

class Recommendation(BaseModel):
    name: str
    category: str
    description: str
    reason: str
    estimated_time: str
    price_range: str

class ItineraryResponse(BaseModel):
    city: str
    recommendations: List[Recommendation]
    summary: str

# Initialize Anthropic client
def get_anthropic_client():
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        return None
    return anthropic.Anthropic(api_key=api_key)

@app.get("/")
async def root():
    return {
        "message": "Welcome to TripBud API!",
        "version": "1.0.0",
        "endpoints": {
            "/recommendations": "POST - Get personalized travel recommendations",
            "/cities": "GET - Get available cities",
            "/categories": "GET - Get recommendation categories"
        }
    }

@app.post("/recommendations", response_model=ItineraryResponse)
async def get_recommendations(request: TripRequest):
    """
    Generate personalized travel recommendations using Claude AI
    """
    client = get_anthropic_client()
    
    if not client:
        # Fallback with mock data if no API key
        return generate_mock_recommendations(request)
    
    try:
        # Build the prompt for Claude
        prompt = f"""You are TripBud, an AI travel companion that curates authentic, personalized recommendations.

User wants to visit: {request.city}
Interests: {', '.join(request.interests)}
Trip duration: {request.duration} days
Budget: {request.budget}
Travel style: {request.travel_style}

Please provide personalized recommendations including:
- Restaurants and cafes (focus on local favorites, not chains)
- Activities and experiences
- Hidden gems and local spots
- Museums or cultural sites if interested

For each recommendation, provide:
1. Name
2. Category (food/activity/culture/nightlife/nature)
3. Brief description
4. Why it matches their interests
5. Estimated time needed
6. Price range ($/$$/$$$/free)

Format your response as a JSON object with this structure:
{{
    "recommendations": [
        {{
            "name": "...",
            "category": "...",
            "description": "...",
            "reason": "...",
            "estimated_time": "...",
            "price_range": "..."
        }}
    ],
    "summary": "A brief overview of the trip plan"
}}

Focus on quality over quantity - 8-12 excellent recommendations total.
Prioritize authentic local experiences over tourist traps."""

        message = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=2000,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        
        # Parse Claude's response
        response_text = message.content[0].text
        
        # Extract JSON from response
        import json
        import re
        
        # Try to find JSON in the response
        json_match = re.search(r'\{.*\}', response_text, re.DOTALL)
        if json_match:
            data = json.loads(json_match.group())
            return ItineraryResponse(
                city=request.city,
                recommendations=[Recommendation(**rec) for rec in data["recommendations"]],
                summary=data.get("summary", f"Personalized {request.duration}-day itinerary for {request.city}")
            )
        else:
            raise ValueError("Could not parse AI response")
            
    except Exception as e:
        print(f"Error with AI generation: {e}")
        return generate_mock_recommendations(request)

def generate_mock_recommendations(request: TripRequest) -> ItineraryResponse:
    """
    Generate mock recommendations when AI is not available
    """
    mock_data = {
        "paris": [
            Recommendation(
                name="Le Comptoir du Relais",
                category="food",
                description="Authentic bistro in Saint-Germain serving classic French cuisine",
                reason="Perfect for food lovers seeking genuine Parisian dining",
                estimated_time="2 hours",
                price_range="$$"
            ),
            Recommendation(
                name="Musée Rodin",
                category="culture",
                description="Beautiful sculpture museum with stunning gardens",
                reason="Less crowded than major museums, perfect for art enthusiasts",
                estimated_time="2-3 hours",
                price_range="$$"
            ),
            Recommendation(
                name="Canal Saint-Martin",
                category="nature",
                description="Picturesque canal with trendy cafes and local atmosphere",
                reason="Great for leisurely walks and people-watching",
                estimated_time="1-2 hours",
                price_range="free"
            )
        ],
        "tokyo": [
            Recommendation(
                name="Tsukiji Outer Market",
                category="food",
                description="Fresh seafood and street food from local vendors",
                reason="Authentic local food experience",
                estimated_time="2-3 hours",
                price_range="$$"
            ),
            Recommendation(
                name="TeamLab Borderless",
                category="activity",
                description="Immersive digital art museum",
                reason="Unique modern cultural experience",
                estimated_time="3 hours",
                price_range="$$$"
            ),
            Recommendation(
                name="Yanaka District",
                category="culture",
                description="Traditional neighborhood with temples and old shops",
                reason="Experience old Tokyo atmosphere",
                estimated_time="2-3 hours",
                price_range="$"
            )
        ]
    }
    
    city_lower = request.city.lower()
    recommendations = mock_data.get(city_lower, mock_data["paris"])
    
    return ItineraryResponse(
        city=request.city,
        recommendations=recommendations[:min(len(recommendations), 8)],
        summary=f"Curated {request.duration}-day itinerary for {request.city} based on your interests"
    )

@app.get("/cities")
async def get_cities():
    """
    Get list of supported cities
    """
    return {
        "cities": [
            {"name": "Paris", "country": "France"},
            {"name": "Tokyo", "country": "Japan"},
            {"name": "New York", "country": "USA"},
            {"name": "Barcelona", "country": "Spain"},
            {"name": "Bangkok", "country": "Thailand"},
            {"name": "Istanbul", "country": "Turkey"},
            {"name": "London", "country": "UK"},
            {"name": "Rome", "country": "Italy"}
        ]
    }

@app.get("/categories")
async def get_categories():
    """
    Get available recommendation categories
    """
    return {
        "categories": [
            {"id": "food", "name": "Food & Dining", "icon": "🍽️"},
            {"id": "culture", "name": "Culture & Museums", "icon": "🏛️"},
            {"id": "activity", "name": "Activities", "icon": "🎯"},
            {"id": "nature", "name": "Nature & Outdoors", "icon": "🌳"},
            {"id": "nightlife", "name": "Nightlife", "icon": "🌙"},
            {"id": "shopping", "name": "Shopping", "icon": "🛍️"}
        ]
    }

if __name__ == "__main__":
    import uvicorn
    print("🚀 Starting TripBud Backend...")
    print("📍 Backend will be available at: http://localhost:8000")
    print("📍 API docs available at: http://localhost:8000/docs")
    uvicorn.run(app, host="0.0.0.0", port=8000)
