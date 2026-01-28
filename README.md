# 🌍 TripBud - Your AI-Powered Travel Companion

TripBud is an intelligent travel planning application that uses AI to curate personalized, authentic recommendations for your trips. Say goodbye to generic travel blogs and hello to trusted, personalized travel experiences!

## ✨ Features

- **AI-Powered Recommendations** - Uses Claude AI to generate personalized travel suggestions
- **Curated Content** - Focus on authentic local experiences over tourist traps
- **Multi-Category Support** - Food, culture, nature, nightlife, shopping, and more
- **Flexible Itineraries** - Customizable by budget, duration, and travel style
- **Beautiful UI** - Clean, modern interface built with React
- **Real-time Planning** - Get instant recommendations based on your preferences

## 🏗️ Tech Stack

### Backend
- **FastAPI** - Modern, fast Python web framework
- **Anthropic Claude** - AI-powered recommendation engine
- **Pydantic** - Data validation
- **Uvicorn** - ASGI server

### Frontend
- **React** - UI framework
- **Vite** - Build tool and dev server
- **Axios** - HTTP client
- **CSS3** - Beautiful gradient designs

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Node.js 16+
- npm or yarn

### Backend Setup

1. **Navigate to backend directory:**
   ```bash
   cd backend
   ```

2. **Create virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables (optional):**
   ```bash
   export ANTHROPIC_API_KEY=your_api_key_here
   ```
   > **Note:** The app works without an API key using mock data. Add your Claude API key for AI-powered recommendations.

5. **Run the backend:**
   ```bash
   python app.py
   ```
   Backend will run at: `http://localhost:8000`

### Frontend Setup

1. **Navigate to frontend directory:**
   ```bash
   cd frontend
   ```

2. **Install dependencies:**
   ```bash
   npm install
   ```

3. **Run the development server:**
   ```bash
   npm run dev
   ```
   Frontend will run at: `http://localhost:5173`

## 📖 Usage

1. Open your browser to `http://localhost:5173`
2. Enter your destination city
3. Select your interests (food, culture, nature, etc.)
4. Choose trip duration and budget
5. Click "Get Recommendations"
6. Explore your personalized itinerary!

## 🔧 Configuration

### Backend API
The backend accepts the following parameters:

```json
{
  "city": "Paris",
  "interests": ["food", "culture", "nature"],
  "duration": 3,
  "budget": "medium",
  "travel_style": "balanced"
}
```

### Environment Variables

**Backend:**
- `ANTHROPIC_API_KEY` - Your Claude API key (optional, uses mock data if not provided)

**Frontend:**
- `VITE_API_URL` - Backend API URL (default: `http://localhost:8000`)

## 🛣️ API Endpoints

### GET /
Health check and API information

### POST /recommendations
Generate travel recommendations
- **Body:** TripRequest object
- **Returns:** ItineraryResponse with recommendations

### GET /cities
Get list of supported cities

### GET /categories
Get available recommendation categories

## 🎨 Features in Detail

### AI-Powered Planning
- Uses Claude Sonnet 4 for intelligent recommendations
- Contextual understanding of user preferences
- Curated local experiences over generic tourist spots

### Smart Categorization
- Food & Dining 🍽️
- Culture & Museums 🏛️
- Nature & Outdoors 🌳
- Nightlife 🌙
- Shopping 🛍️
- Adventure & Activities 🎯

### Flexible Budget Options
- Budget ($)
- Medium ($$)
- Luxury ($$$)

### Travel Styles
- Relaxed & Leisurely
- Balanced
- Fast-Paced & Packed

## 🔮 Future Enhancements

- [ ] User authentication and saved itineraries
- [ ] Integration with booking platforms
- [ ] Interactive maps with recommendations
- [ ] Social sharing features
- [ ] Multi-day detailed itinerary planning
- [ ] Integration with real-time data (weather, events)
- [ ] Mobile app version
- [ ] Collaborative trip planning

## 🤝 Contributing

Contributions are welcome! Feel free to:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📝 License

This project is open source and available under the MIT License.

## 🙏 Acknowledgments

- Backend built with [Claude AI](https://claude.ai) by Anthropic
- Curated UI design inspired by Barcelona aesthetics
- Thanks to all travelers seeking meaningful adventures!

## 💬 Support

For questions or issues, please open an issue on GitHub.

---

**Happy Traveling! ✈️🌍**

Built with ❤️ by TripBud Team
