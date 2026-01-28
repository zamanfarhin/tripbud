# 🚀 TripBud - Quick Start Guide

## What You've Got

TripBud is a complete, working AI-powered travel companion app with:
- ✅ Beautiful React frontend
- ✅ FastAPI backend with AI integration
- ✅ Works out of the box (no API key needed for testing)
- ✅ Fully styled and responsive

## 📥 Installation (3 Simple Steps)

### Step 1: Open Two Terminal Windows

You'll need 2 terminal windows - one for backend, one for frontend.

### Step 2: Start the Backend (Terminal 1)

```bash
# Navigate to the tripbud directory
cd tripbud/backend

# Create virtual environment
python3 -m venv venv

# Activate it
source venv/bin/activate  # Mac/Linux
# OR
venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt

# Run the backend
python app.py
```

✅ You should see: 
```
🚀 Starting TripBud Backend...
📍 Backend will be available at: http://localhost:8000
📍 API docs available at: http://localhost:8000/docs
INFO: Uvicorn running on http://0.0.0.0:8000
```

**Important:** Even though it says `0.0.0.0:8000`, you access it at `http://localhost:8000`

### Step 3: Start the Frontend (Terminal 2)

```bash
# Navigate to frontend directory
cd tripbud/frontend

# Install dependencies
npm install

# Run the development server
npm run dev
```

✅ You should see: `Local: http://localhost:5173/`

### Step 4: Open Your Browser

Visit: **http://localhost:5173**

🎉 **You're done!** TripBud is now running!

---

## 🎯 How to Use TripBud

1. **Enter a destination** (e.g., "Paris", "Tokyo", "New York")
2. **Select your interests** (click the emoji buttons)
3. **Choose trip duration** (1 day to 2 weeks)
4. **Set your budget** (Budget, Medium, Luxury)
5. **Pick travel style** (Relaxed, Balanced, or Fast-paced)
6. **Click "Get Recommendations"** 🔍

You'll instantly get personalized recommendations with:
- Restaurant and cafe suggestions
- Activities and experiences
- Cultural sites
- Local hidden gems
- Time estimates and pricing

---

## 🔑 Optional: Add Claude AI (For Real AI Recommendations)

By default, TripBud uses mock data so you can test it immediately. To get real AI-powered recommendations:

1. **Get an API key** from: https://console.anthropic.com/
2. **Set the environment variable:**

```bash
# Mac/Linux (in your backend terminal)
export ANTHROPIC_API_KEY=your_actual_api_key_here

# Windows
set ANTHROPIC_API_KEY=your_actual_api_key_here
```

3. **Restart the backend** (Ctrl+C then `python app.py` again)

Now TripBud will use Claude AI to generate truly personalized recommendations!

---

## 🛠️ Troubleshooting

### "This site can't be reached" or "0.0.0.0 refused to connect"
**Don't go to 0.0.0.0!** Use these URLs instead:
- Frontend: **http://localhost:5173** ✅
- Backend: **http://localhost:8000** ✅

The `0.0.0.0` in the terminal is just the binding address, not the URL you visit.

### Backend not starting / Port already in use
Someone else is using port 8000. Kill the process:
```bash
# Mac/Linux
lsof -ti:8000 | xargs kill -9

# Windows
netstat -ano | findstr :8000
# Then: taskkill /PID <PID_NUMBER> /F
```

### "Command not found: python"
Try `python3` instead of `python`

### "Command not found: npm"
Install Node.js from: https://nodejs.org/

### Port already in use
Backend: Change port in `backend/app.py` (line: `uvicorn.run(app, port=8000)`)
Frontend: Change port in `frontend/vite.config.js` (line: `port: 5173`)

### Dependencies fail to install
Backend: Make sure Python 3.8+ is installed: `python3 --version`
Frontend: Make sure Node.js 16+ is installed: `node --version`

---

## 📁 Project Structure

```
tripbud/
├── backend/          # Python FastAPI server
│   ├── app.py       # Main API with AI integration
│   └── requirements.txt
├── frontend/         # React application
│   ├── src/
│   │   ├── App.jsx  # Main component
│   │   └── App.css  # Styles
│   └── package.json
└── README.md
```

---

## 🎨 Features

- **🤖 AI-Powered** - Uses Claude AI for personalized recommendations
- **🎯 Multi-Category** - Food, culture, nature, nightlife, shopping
- **💰 Budget-Aware** - Respects your spending preferences
- **⏱️ Time Estimates** - Know how long each activity takes
- **📱 Responsive** - Works on desktop, tablet, and mobile
- **🎨 Beautiful UI** - Modern gradient design with smooth animations

---

## 🔄 Making Changes

### Update the Backend
Edit `backend/app.py` - changes take effect after restart

### Update the Frontend
Edit `frontend/src/App.jsx` - changes are instant (hot reload)

### Change Styling
Edit `frontend/src/App.css` - changes are instant

---

## 📝 Next Steps

1. ✅ Get it running (you're here!)
2. 🎨 Customize the colors and styling
3. 🔑 Add your Claude API key for real AI
4. 🌍 Test different destinations
5. 🚀 Deploy to production (Vercel, Railway, etc.)

---

## 🤝 Need Help?

- Check README.md for detailed documentation
- Check PROJECT_STRUCTURE.md for architecture info
- All files are well-commented

---

## 🎉 You're All Set!

TripBud is ready to help you plan amazing trips. Start exploring destinations and discovering hidden gems!

**Happy Traveling! ✈️🌍**
