#!/bin/bash

echo "🌍 Setting up TripBud..."
echo ""

# Backend setup
echo "📦 Setting up Backend..."
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
echo "✅ Backend dependencies installed!"
echo ""

# Return to root
cd ..

# Frontend setup
echo "🎨 Setting up Frontend..."
cd frontend
npm install
echo "✅ Frontend dependencies installed!"
echo ""

# Return to root
cd ..

echo "🎉 Setup complete!"
echo ""
echo "To run TripBud:"
echo "1. Terminal 1 - Backend:"
echo "   cd backend && source venv/bin/activate && python app.py"
echo ""
echo "2. Terminal 2 - Frontend:"
echo "   cd frontend && npm run dev"
echo ""
echo "Then open: http://localhost:5173"
echo ""
echo "Optional: Set ANTHROPIC_API_KEY environment variable for AI features"
