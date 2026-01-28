# 📁 TripBud Project Structure

```
tripbud/
├── backend/                    # FastAPI Backend
│   ├── app.py                 # Main FastAPI application
│   ├── requirements.txt       # Python dependencies
│   └── .env.example          # Environment variables template
│
├── frontend/                   # React Frontend
│   ├── src/
│   │   ├── App.jsx           # Main application component
│   │   ├── App.css           # Application styles
│   │   ├── main.jsx          # React entry point
│   │   └── index.css         # Global styles
│   ├── index.html            # HTML entry point
│   ├── package.json          # Node dependencies
│   └── vite.config.js        # Vite configuration
│
├── README.md                  # Main documentation
├── setup.sh                   # Quick setup script
└── .gitignore                # Git ignore rules
```

## 🔍 File Descriptions

### Backend Files

**app.py**
- Main FastAPI application
- API endpoints for recommendations
- Claude AI integration
- Mock data fallback for testing

**requirements.txt**
- fastapi - Web framework
- uvicorn - ASGI server
- anthropic - Claude AI SDK
- pydantic - Data validation

### Frontend Files

**App.jsx**
- Main React component
- Trip planning form
- Recommendations display
- State management

**App.css**
- Beautiful gradient designs
- Responsive layouts
- Card animations
- Form styling

**vite.config.js**
- Development server config
- API proxy setup
- Build optimization

### Configuration Files

**.env.example**
- Environment variables template
- API key configuration
- Server settings

**setup.sh**
- Automated setup script
- Installs all dependencies
- Creates virtual environment

## 🎯 Key Components

### Backend API Endpoints

1. **GET /** - Health check
2. **POST /recommendations** - Get AI recommendations
3. **GET /cities** - List supported cities
4. **GET /categories** - List recommendation categories

### Frontend Components

1. **Trip Form** - User input collection
2. **Interest Selector** - Interactive category selection
3. **Recommendation Cards** - Display results
4. **Results Grid** - Responsive layout

## 🔄 Data Flow

1. User fills out trip preferences in React form
2. Frontend sends POST request to /recommendations
3. Backend processes request with Claude AI
4. AI generates personalized recommendations
5. Backend returns structured JSON response
6. Frontend displays beautiful recommendation cards

## 🎨 Design System

**Colors:**
- Primary: #667eea (Purple-Blue)
- Secondary: #764ba2 (Purple)
- Background: Linear gradients
- Cards: Soft grays with gradients

**Typography:**
- Headers: System fonts
- Body: Sans-serif
- Responsive sizing

**Components:**
- Rounded corners (10-20px)
- Smooth animations
- Box shadows for depth
- Hover effects

## 🚀 Development Workflow

1. Start backend: `cd backend && python app.py`
2. Start frontend: `cd frontend && npm run dev`
3. Access at: `http://localhost:5173`
4. Backend API: `http://localhost:8000`

## 📝 Adding Features

### New API Endpoint
1. Add route in `backend/app.py`
2. Define request/response models
3. Implement logic
4. Test with mock data

### New UI Component
1. Create component in `frontend/src/`
2. Import in `App.jsx`
3. Add styling in CSS
4. Connect to API

## 🔧 Configuration Options

### Backend
- Change port in `app.py`: `uvicorn.run(app, port=8000)`
- Add CORS origins in CORS middleware
- Adjust AI model in `model="claude-sonnet-4-20250514"`

### Frontend
- Change port in `vite.config.js`: `port: 5173`
- Update API URL in `App.jsx`: `API_URL`
- Customize colors in CSS variables

## 📦 Dependencies Explained

### Backend Dependencies
- **fastapi**: Modern Python web framework
- **uvicorn**: Lightning-fast ASGI server
- **anthropic**: Official Claude AI SDK
- **pydantic**: Data validation and settings

### Frontend Dependencies
- **react**: UI library
- **vite**: Next-gen frontend tooling
- **axios**: Promise-based HTTP client

## 🎓 Learning Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [React Documentation](https://react.dev/)
- [Anthropic API Docs](https://docs.anthropic.com/)
- [Vite Guide](https://vitejs.dev/guide/)

---

Happy coding! 🚀
