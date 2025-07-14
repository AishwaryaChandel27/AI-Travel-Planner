import os
import logging

try:
    import google.generativeai as genai
    GEMINI_AVAILABLE = True
except ImportError:
    GEMINI_AVAILABLE = False
    logging.warning("Google Generative AI not available. Install with: pip install google-generativeai")

def get_travel_response(user_input):
    """Generate travel response using Gemini AI or fallback."""

    # Get API key from environment
    api_key = os.environ.get('GEMINI_API_KEY')

    if not GEMINI_AVAILABLE:
        return get_fallback_response(user_input)

    if not api_key:
        logging.warning("GEMINI_API_KEY not found. Using fallback responses.")
        return get_fallback_response(user_input)

    try:
        # Configure Gemini
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-pro')

        # Enhanced prompt for better travel responses
        travel_prompt = f"""
        You are an expert travel assistant. Provide detailed, helpful travel advice.

        User Request: {user_input}

        Please provide a comprehensive response that includes:
        - Specific recommendations
        - Practical tips
        - Budget considerations
        - Best times to visit
        - Local insights

        Format your response in a clear, organized way with bullet points and sections where appropriate.
        """

        # Generate response
        response = model.generate_content(travel_prompt)

        if response.text:
            return response.text
        else:
            return get_fallback_response(user_input)

    except Exception as e:
        logging.error(f"Gemini API error: {e}")
        return get_fallback_response(user_input)

def get_fallback_response(user_input):
    """Provide fallback responses when Gemini is not available."""

    user_lower = user_input.lower()

    # Destination-specific responses
    if any(dest in user_lower for dest in ['paris', 'france']):
        return """
        🇫🇷 **Paris Travel Guide**

        **Best Time to Visit:** April-June, September-October

        **Must-See Attractions:**
        • Eiffel Tower - Visit at sunset for magical views
        • Louvre Museum - Book skip-the-line tickets
        • Notre-Dame Cathedral - Currently under restoration
        • Champs-Élysées - Perfect for shopping and cafes

        **Budget Tips:**
        • Museum passes save money and time
        • Lunch at local bistros vs tourist areas
        • Metro day passes for easy transportation

        **Local Cuisine:**
        • Croissants at local boulangeries
        • Seine riverside picnics
        • Traditional French onion soup

        **Travel Tips:**
        • Learn basic French phrases
        • Carry cash for small purchases
        • Book restaurants in advance
        """

    elif any(dest in user_lower for dest in ['tokyo', 'japan']):
        return """
        🇯🇵 **Tokyo Travel Guide**

        **Best Time to Visit:** March-May (Cherry Blossoms), September-November

        **Must-See Areas:**
        • Shibuya Crossing - Iconic intersection experience
        • Senso-ji Temple - Historic Buddhist temple
        • Tsukiji Outer Market - Fresh sushi breakfast
        • Harajuku - Youth culture and fashion

        **Budget Breakdown:**
        • Accommodation: $50-150/night
        • Meals: $30-60/day
        • Transportation: $10-15/day (JR Pass)

        **Cultural Tips:**
        • Bow when greeting
        • Remove shoes indoors
        • No tipping culture
        • Respect quiet zones on trains

        **Food Experiences:**
        • Ramen shops in Golden Gai
        • Conveyor belt sushi
        • Traditional tea ceremony
        """

    elif any(dest in user_lower for dest in ['london', 'uk', 'england']):
        return """
        🇬🇧 **London Travel Guide**

        **Best Time to Visit:** May-September (warmer weather)

        **Top Attractions:**
        • Big Ben & Parliament - Iconic landmarks
        • British Museum - Free admission
        • Tower of London - Crown Jewels
        • Camden Market - Alternative shopping

        **Budget Guide:**
        • Many museums are free
        • Pub meals are affordable
        • Oyster Card for transport savings

        **Weather Tips:**
        • Always carry an umbrella
        • Layer clothing
        • Waterproof jacket essential

        **Cultural Experiences:**
        • Traditional afternoon tea
        • West End theater shows
        • Sunday roast at historic pubs
        """

    # Budget-related responses
    elif any(budget in user_lower for budget in ['budget', 'cheap', 'affordable']):
        return """
        💰 **Budget Travel Tips**

        **Accommodation:**
        • Hostels and guesthouses
        • Airbnb for longer stays
        • House-sitting opportunities

        **Transportation:**
        • Book flights in advance
        • Use budget airlines
        • Public transport vs taxis
        • Walking tours (often free)

        **Food Savings:**
        • Local markets and street food
        • Cook your own meals
        • Lunch specials vs dinner prices

        **Activities:**
        • Free museums and galleries
        • City walking tours
        • Beach and nature activities
        • Local festivals and events
        """

    # Duration-specific advice
    elif any(duration in user_lower for duration in ['weekend', '2 days', 'short']):
        return """
        ⏰ **Weekend Travel Guide**

        **Planning Tips:**
        • Choose nearby destinations
        • Focus on 2-3 main attractions
        • Book accommodation early

        **Packing Light:**
        • Carry-on only
        • Comfortable walking shoes
        • Weather-appropriate clothing

        **Time Management:**
        • Arrive Friday evening
        • Full days Saturday & Sunday
        • Monday morning departure

        **City Break Ideas:**
        • Historic city centers
        • Cultural districts
        • Food and market tours
        """

    # General travel advice
    else:
        return """
        🌍 **General Travel Assistance**

        **Planning Your Trip:**
        • Research your destination thoroughly
        • Check visa and passport requirements
        • Book flights and accommodation in advance
        • Create a flexible itinerary

        **Packing Essentials:**
        • Travel documents and copies
        • Comfortable walking shoes
        • Weather-appropriate clothing
        • Universal adapter and chargers
        • Basic first aid kit

        **Safety Tips:**
        • Share itinerary with someone at home
        • Keep emergency contacts handy
        • Research local customs and laws
        • Stay aware of your surroundings

        **Money Matters:**
        • Notify bank of travel plans
        • Have multiple payment methods
        • Research local tipping customs
        • Keep some cash for emergencies

        **Making the Most of Your Trip:**
        • Try local cuisine
        • Learn basic local phrases
        • Be open to spontaneous experiences
        • Take time to rest and enjoy

        *For more specific advice, please tell me about your destination, budget, and travel preferences!*
        """

    return response