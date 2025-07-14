
#!/usr/bin/env python3
"""
AI Travel Assistant - Simple Travel Planning App
"""

from app import app
import routes

if __name__ == '__main__':
    print("🌍 Starting AI Travel Assistant...")
    print("📍 Visit: http://localhost:5000")
    print("🔑 Make sure to set GEMINI_API_KEY in Secrets for AI features")
    app.run(host='0.0.0.0', port=5000, debug=True)
