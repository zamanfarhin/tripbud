import { useState } from 'react'
import axios from 'axios'
import './App.css'

const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000'

function App() {
  const [formData, setFormData] = useState({
    city: '',
    interests: [],
    duration: 3,
    budget: 'medium',
    travel_style: 'balanced'
  })
  const [recommendations, setRecommendations] = useState(null)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState(null)

  const interestOptions = [
    { id: 'food', label: '🍽️ Food & Dining', icon: '🍽️' },
    { id: 'culture', label: '🏛️ Culture & Museums', icon: '🏛️' },
    { id: 'nature', label: '🌳 Nature & Outdoors', icon: '🌳' },
    { id: 'nightlife', label: '🌙 Nightlife', icon: '🌙' },
    { id: 'shopping', label: '🛍️ Shopping', icon: '🛍️' },
    { id: 'adventure', label: '🎯 Adventure & Activities', icon: '🎯' }
  ]

  const handleInterestToggle = (interest) => {
    setFormData(prev => ({
      ...prev,
      interests: prev.interests.includes(interest)
        ? prev.interests.filter(i => i !== interest)
        : [...prev.interests, interest]
    }))
  }

  const handleSubmit = async (e) => {
    e.preventDefault()
    setLoading(true)
    setError(null)

    if (formData.interests.length === 0) {
      setError('Please select at least one interest')
      setLoading(false)
      return
    }

    try {
      const response = await axios.post(`${API_URL}/recommendations`, formData)
      setRecommendations(response.data)
    } catch (err) {
      setError('Failed to get recommendations. Please try again.')
      console.error(err)
    } finally {
      setLoading(false)
    }
  }

  const getCategoryEmoji = (category) => {
    const emojiMap = {
      food: '🍽️',
      culture: '🏛️',
      activity: '🎯',
      nature: '🌳',
      nightlife: '🌙',
      shopping: '🛍️'
    }
    return emojiMap[category] || '📍'
  }

  return (
    <div className="app">
      <header className="header">
        <h1>✈️ TripBud</h1>
        <p className="tagline">Your AI-Powered Travel Companion</p>
      </header>

      <main className="main-content">
        {!recommendations ? (
          <div className="form-container">
            <h2>Plan Your Perfect Trip</h2>
            <form onSubmit={handleSubmit} className="trip-form">
              <div className="form-group">
                <label htmlFor="city">Where do you want to go?</label>
                <input
                  type="text"
                  id="city"
                  value={formData.city}
                  onChange={(e) => setFormData({...formData, city: e.target.value})}
                  placeholder="e.g., Paris, Tokyo, New York"
                  required
                />
              </div>

              <div className="form-group">
                <label>What are you interested in?</label>
                <div className="interests-grid">
                  {interestOptions.map(option => (
                    <button
                      key={option.id}
                      type="button"
                      className={`interest-button ${formData.interests.includes(option.id) ? 'selected' : ''}`}
                      onClick={() => handleInterestToggle(option.id)}
                    >
                      <span className="interest-icon">{option.icon}</span>
                      <span className="interest-label">{option.label.split(' ').slice(1).join(' ')}</span>
                    </button>
                  ))}
                </div>
              </div>

              <div className="form-row">
                <div className="form-group">
                  <label htmlFor="duration">Trip Duration</label>
                  <select
                    id="duration"
                    value={formData.duration}
                    onChange={(e) => setFormData({...formData, duration: parseInt(e.target.value)})}
                  >
                    <option value="1">1 day</option>
                    <option value="2">2 days</option>
                    <option value="3">3 days</option>
                    <option value="4">4 days</option>
                    <option value="5">5 days</option>
                    <option value="7">1 week</option>
                    <option value="14">2 weeks</option>
                  </select>
                </div>

                <div className="form-group">
                  <label htmlFor="budget">Budget</label>
                  <select
                    id="budget"
                    value={formData.budget}
                    onChange={(e) => setFormData({...formData, budget: e.target.value})}
                  >
                    <option value="budget">Budget ($)</option>
                    <option value="medium">Medium ($$)</option>
                    <option value="luxury">Luxury ($$$)</option>
                  </select>
                </div>
              </div>

              <div className="form-group">
                <label htmlFor="travel_style">Travel Style</label>
                <select
                  id="travel_style"
                  value={formData.travel_style}
                  onChange={(e) => setFormData({...formData, travel_style: e.target.value})}
                >
                  <option value="relaxed">Relaxed & Leisurely</option>
                  <option value="balanced">Balanced</option>
                  <option value="packed">Fast-Paced & Packed</option>
                </select>
              </div>

              {error && <div className="error-message">{error}</div>}

              <button type="submit" className="submit-button" disabled={loading}>
                {loading ? 'Finding Perfect Spots...' : '🔍 Get Recommendations'}
              </button>
            </form>
          </div>
        ) : (
          <div className="results-container">
            <div className="results-header">
              <h2>Your {recommendations.city} Itinerary</h2>
              <p className="summary">{recommendations.summary}</p>
              <button 
                className="new-search-button"
                onClick={() => setRecommendations(null)}
              >
                ← Plan Another Trip
              </button>
            </div>

            <div className="recommendations-grid">
              {recommendations.recommendations.map((rec, index) => (
                <div key={index} className="recommendation-card">
                  <div className="card-header">
                    <span className="category-badge">
                      {getCategoryEmoji(rec.category)} {rec.category}
                    </span>
                    <span className="price-badge">{rec.price_range}</span>
                  </div>
                  <h3>{rec.name}</h3>
                  <p className="description">{rec.description}</p>
                  <div className="card-footer">
                    <span className="time-badge">⏱️ {rec.estimated_time}</span>
                    <p className="reason"><strong>Why:</strong> {rec.reason}</p>
                  </div>
                </div>
              ))}
            </div>
          </div>
        )}
      </main>

      <footer className="footer">
        <p>Built with ❤️ by TripBud • Powered by Claude AI</p>
      </footer>
    </div>
  )
}

export default App
