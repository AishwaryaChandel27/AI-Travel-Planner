# 🌍 AI Travel Planner

<div align="center">
  <img src="https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/Flask-2.3.3-green?style=for-the-badge&logo=flask&logoColor=white">
  <img src="https://img.shields.io/badge/Google%20Gemini-AI-orange?style=for-the-badge&logo=google&logoColor=white">
  <img src="https://img.shields.io/badge/Bootstrap-5.3-purple?style=for-the-badge&logo=bootstrap&logoColor=white">
  <img src="https://img.shields.io/badge/SQLAlchemy-ORM-red?style=for-the-badge&logo=sqlite&logoColor=white">
</div>

<div align="center">
  <h3>🚀 Create personalized travel itineraries powered by artificial intelligence</h3>
  <p>Get AI-powered destination recommendations, detailed travel plans, and seamless booking management - all in one intelligent platform.</p>
</div>

---

## ✨ Features

### 🧠 AI-Powered Intelligence
- **Smart Destination Recommendations**: Get personalized suggestions based on your preferences, budget, and travel style
- **Dynamic Itinerary Generation**: Receive comprehensive daily plans with activities, restaurants, and local insights
- **Intelligent Travel Tips**: Get location-specific advice for customs, safety, and cultural experiences

### 🎯 Comprehensive Travel Planning
- **Budget Management**: Track expenses with detailed breakdowns and cost-effective recommendations
- **Multi-Service Booking**: Browse and book flights, hotels, and activities from one platform
- **Weather Integration**: Real-time weather information and forecasts for your destination
- **Preference Tracking**: Save and reuse your travel preferences for future trips

### 🎨 Modern User Experience
- **Responsive Design**: Beautiful, mobile-first interface with Bootstrap 5
- **Dark Theme**: Easy-on-the-eyes interface optimized for extended planning sessions
- **Interactive Elements**: Smooth animations and intuitive navigation
- **Accessibility**: WCAG-compliant design with keyboard navigation support

---

## 🚀 Quick Start

### Prerequisites
- Python 3.11+
- Google Gemini API Key ([Get yours free](https://aistudio.google.com/app/apikey))

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/ai-travel-planner.git
   cd ai-travel-planner
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   ```bash
   export GEMINI_API_KEY="your-gemini-api-key"
   export SESSION_SECRET="your-session-secret"
   export DATABASE_URL="sqlite:///travel_planner.db"  # Optional: defaults to SQLite
   ```

4. **Run the application**
   ```bash
   python main.py
   ```

5. **Open your browser**
   Navigate to `http://localhost:5000`

---

## 🏗️ Architecture

### Core Components

```
ai-travel-planner/
├── 🎯 Core Application
│   ├── app.py              # Flask app configuration
│   ├── main.py             # Application entry point
│   └── routes.py           # Route handlers and business logic
├── 🧠 AI & Services
│   ├── gemini.py           # Google Gemini AI integration
│   └── travel_service.py   # Mock travel booking services
├── 🗄️ Data Layer
│   ├── models.py           # SQLAlchemy database models
│   └── instance/           # Database files
├── 🎨 Frontend
│   ├── templates/          # Jinja2 HTML templates
│   ├── static/css/         # Custom stylesheets
│   └── static/js/          # JavaScript functionality
└── 📚 Documentation
    └── README.md           # This file
```

### Technology Stack

| Component | Technology | Purpose |
|-----------|------------|---------|
| **Backend** | Flask 2.3.3 | Web framework and API |
| **AI Engine** | Google Gemini 2.5 | Travel recommendations and planning |
| **Database** | SQLAlchemy + SQLite/PostgreSQL | Data persistence |
| **Frontend** | Bootstrap 5 + Vanilla JS | Responsive UI |
| **Deployment** | Gunicorn + Replit | Production server |

---

## 🎮 Usage Guide

### 1. **Set Your Preferences**
- Choose your budget range
- Select travel dates
- Pick interests (adventure, culture, food, etc.)
- Set group size and accommodation preferences

### 2. **Get AI Recommendations**
- Receive 3 personalized destination suggestions
- View detailed reasons why each destination fits your preferences
- See budget breakdowns and best times to visit

### 3. **Generate Your Itinerary**
- Select your preferred destination
- Get a comprehensive daily itinerary
- View restaurant recommendations and travel tips
- See weather forecasts and local insights

### 4. **Book Your Trip**
- Browse available flights, hotels, and activities
- Compare prices and options
- Make bookings with mock payment system
- Track all your bookings in one place

---

## 🔧 API Reference

### Core Models

#### TravelPreference
```python
{
    "id": int,
    "session_id": str,
    "budget": float,
    "start_date": date,
    "end_date": date,
    "group_size": int,
    "interests": [str],
    "accommodation_type": str,
    "transport_preference": str
}
```

#### Itinerary
```python
{
    "id": int,
    "destination": str,
    "title": str,
    "description": str,
    "activities": [
        {
            "day": str,
            "activities": [
                {
                    "time": str,
                    "activity": str,
                    "description": str,
                    "duration": str
                }
            ]
        }
    ],
    "budget_breakdown": {
        "accommodation": float,
        "food": float,
        "activities": float,
        "transport": float
    },
    "recommendations": {
        "restaurants": [dict],
        "accommodations": [dict],
        "travel_tips": [str]
    }
}
```

### Key Endpoints

| Endpoint | Method | Description |
|----------|---------|-------------|
| `/` | GET | Homepage |
| `/preferences` | GET/POST | Travel preferences form |
| `/destinations` | GET | AI destination recommendations |
| `/itinerary` | GET | Generated travel itinerary |
| `/book/<type>` | GET | Booking interface (flights/hotels/activities) |
| `/my_bookings` | GET | User's booking history |

---

## 🔐 Environment Variables

| Variable | Required | Default | Description |
|----------|----------|---------|-------------|
| `GEMINI_API_KEY` | ✅ | - | Google Gemini API key for AI features |
| `SESSION_SECRET` | ✅ | - | Flask session encryption key |
| `DATABASE_URL` | ❌ | `sqlite:///travel_planner.db` | Database connection string |

---

## 🎨 Customization

### Styling
- Modify `static/css/style.css` for custom themes
- Update Bootstrap variables in templates
- Add custom animations and transitions

### AI Behavior
- Adjust prompts in `gemini.py` for different recommendation styles
- Modify response schemas for additional data fields
- Customize travel tips and suggestions

### Mock Services
- Extend `travel_service.py` with real API integrations
- Add more booking providers and options
- Implement real payment processing

---

## 🚀 Deployment

### Development
```bash
python main.py
```

### Production (Gunicorn)
```bash
gunicorn --bind 0.0.0.0:5000 --reuse-port --reload main:app
```

### Docker
```dockerfile
FROM python:3.11-slim
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "main:app"]
```

### Environment-Specific Settings
- **Development**: SQLite database, debug mode enabled
- **Production**: PostgreSQL database, optimized for performance
- **Cloud**: Compatible with Replit, Heroku, AWS, and other platforms

---

## 🤝 Contributing

We welcome contributions! Here's how to get started:

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/amazing-feature
   ```
3. **Make your changes**
4. **Add tests** (if applicable)
5. **Commit your changes**
   ```bash
   git commit -m "Add amazing feature"
   ```
6. **Push to the branch**
   ```bash
   git push origin feature/amazing-feature
   ```
7. **Open a Pull Request**

### Development Guidelines
- Follow PEP 8 for Python code
- Use meaningful commit messages
- Add documentation for new features
- Test your changes thoroughly

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- **Google Gemini**: For providing powerful AI capabilities
- **Bootstrap Team**: For the excellent CSS framework
- **Flask Community**: For the lightweight web framework
- **Font Awesome**: For beautiful icons

---

## 📞 Support

- **Documentation**: [Wiki](https://github.com/yourusername/ai-travel-planner/wiki)
- **Issues**: [GitHub Issues](https://github.com/yourusername/ai-travel-planner/issues)
- **Discussions**: [GitHub Discussions](https://github.com/yourusername/ai-travel-planner/discussions)

---

<div align="center">
  <p>Made with ❤️ by the AI Travel Planner team</p>
  <p>
    <a href="https://github.com/yourusername/ai-travel-planner/stargazers">⭐ Star us on GitHub</a> |
    <a href="https://twitter.com/intent/tweet?text=Check%20out%20this%20amazing%20AI%20Travel%20Planner!&url=https://github.com/yourusername/ai-travel-planner">🐦 Share on Twitter</a>
  </p>
</div>