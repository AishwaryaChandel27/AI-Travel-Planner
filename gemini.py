import os
import logging

try:
    import google.generativeai as genai
    GENAI_AVAILABLE = True
except ImportError:
    GENAI_AVAILABLE = False
    logging.warning("Google Generative AI not available. Install with: pip install google-generativeai")

# Initialize Gemini client
api_key = os.environ.get("GEMINI_API_KEY")
if api_key and GENAI_AVAILABLE:
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-pro')
        logging.info("Gemini AI initialized successfully")
    except Exception as e:
        model = None
        logging.error(f"Failed to configure Gemini: {e}")
else:
    model = None
    if not api_key:
        logging.warning("GEMINI_API_KEY not found. Set it in the Secrets tab.")
    if not GENAI_AVAILABLE:
        logging.warning("Google Generative AI not available.")

def get_travel_response(prompt: str) -> str:
    """Get AI-powered travel response based on user prompt."""
    if not model:
        return get_fallback_response()

    try:
        # Enhanced prompt for better travel responses
        enhanced_prompt = f"""
        You are an expert travel advisor with extensive knowledge of destinations worldwide.
        Provide detailed, practical, and personalized travel advice.

        User Request: {prompt}

        Please provide a comprehensive response that includes:
        - Specific recommendations
        - Practical tips
        - Budget considerations
        - Cultural insights
        - Safety information when relevant

        Format your response in a clear, organized manner with proper sections.
        """

        response = model.generate_content(enhanced_prompt)

        if response.text:
            return response.text
        else:
            logging.warning("Empty response from Gemini")
            return get_fallback_response()

    except Exception as e:
        logging.error(f"Error getting AI response: {e}")
        return get_fallback_response()

def get_fallback_response() -> str:
    """Provide fallback response when AI is not available."""
    return """
    🌍 **Travel Planning Assistant**

    Thank you for your travel inquiry! While our AI service is currently unavailable, here are some general travel tips:

    **Planning Your Trip:**
    • Research your destination's visa requirements and entry restrictions
    • Check the best time to visit based on weather and local events
    • Set a realistic budget including accommodation, food, transport, and activities
    • Book flights and accommodation in advance for better rates

    **Packing Tips:**
    • Pack light and versatile clothing
    • Bring necessary medications and copies of important documents
    • Check luggage restrictions for your airline

    **Safety & Health:**
    • Register with your embassy if traveling internationally
    • Get travel insurance
    • Research local customs and cultural norms

    **Money Matters:**
    • Notify your bank of travel plans
    • Research local currency and payment methods
    • Keep emergency cash in multiple locations

    To get personalized AI-powered recommendations, please ensure the GEMINI_API_KEY is properly configured.
    You can get a free API key at: https://aistudio.google.com/app/apikey
    """