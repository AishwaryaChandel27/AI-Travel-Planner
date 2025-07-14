import json
import logging
import os
from google import genai
from google.genai import types
from pydantic import BaseModel

# Initialize Gemini client
client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

class TravelRecommendation(BaseModel):
    destination: str
    reasons: list[str]
    best_time_to_visit: str
    estimated_budget: dict
    highlights: list[str]

class ItineraryPlan(BaseModel):
    destination: str
    duration_days: int
    daily_activities: list[dict]
    budget_breakdown: dict
    travel_tips: list[str]
    recommended_restaurants: list[dict]
    accommodation_suggestions: list[dict]

def get_destination_recommendations(preferences: dict) -> list[TravelRecommendation]:
    """Get AI-powered destination recommendations based on user preferences."""
    try:
        interests_str = ", ".join(preferences.get('interests', []))
        country_info = preferences.get('country_info', {})
        popular_destinations = preferences.get('popular_destinations', [])
        currency = country_info.get('currency', 'USD')
        
        destinations_str = ", ".join(popular_destinations) if popular_destinations else "major cities and attractions"
        
        prompt = f"""
        As a travel expert, recommend 3 specific destinations in {preferences.get('destination_country', 'the selected country')} based on these preferences:
        
        USER PREFERENCES:
        - Country: {preferences.get('destination_country')}
        - Budget Type: {preferences.get('budget_type', 'mid_range')}
        - Daily Budget: {preferences.get('budget', 100)} {currency}
        - Interests: {interests_str}
        - Group size: {preferences.get('group_size', 1)} people
        - Travel dates: {preferences.get('start_date', 'Flexible')} to {preferences.get('end_date', 'Flexible')}
        - Accommodation: {preferences.get('accommodation_type', 'hotel')}
        - Transport: {preferences.get('transport_preference', 'public transport')}
        
        COUNTRY INFORMATION:
        - Currency: {currency}
        - Popular destinations: {destinations_str}
        - Best time to visit: {country_info.get('best_time', 'Year-round')}
        - Cultural notes: {country_info.get('cultural_notes', 'No specific notes')}
        
        For each destination, provide:
        - Destination name (choose from popular destinations or suggest similar)
        - 3-4 reasons why it's perfect for these preferences
        - Best time to visit (considering local seasons)
        - Estimated budget breakdown in {currency} (accommodation, food, activities, transport)
        - Top 5 highlights/attractions specific to this destination
        
        Focus on destinations that match the budget type and interests. Be specific about costs in {currency}.
        """

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
            config=types.GenerateContentConfig(
                response_mime_type="application/json",
                response_schema=list[TravelRecommendation],
            ),
        )

        if response.text:
            data = json.loads(response.text)
            return [TravelRecommendation(**rec) for rec in data]
        else:
            raise ValueError("Empty response from Gemini")

    except Exception as e:
        logging.error(f"Error getting destination recommendations: {e}")
        return []

def generate_itinerary(preferences: dict, destination: str) -> ItineraryPlan:
    """Generate a detailed itinerary for the selected destination."""
    try:
        interests_str = ", ".join(preferences.get('interests', []))
        duration = (preferences.get('end_date') - preferences.get('start_date')).days if preferences.get('end_date') and preferences.get('start_date') else 7
        country_info = preferences.get('country_info', {})
        currency = country_info.get('currency', 'USD')
        
        prompt = f"""
        Create a detailed {duration}-day itinerary for {destination} in {preferences.get('destination_country')} based on these preferences:
        
        USER PREFERENCES:
        - Country: {preferences.get('destination_country')}
        - Budget Type: {preferences.get('budget_type', 'mid_range')}
        - Daily Budget: {preferences.get('budget', 100)} {currency}
        - Interests: {interests_str}
        - Group size: {preferences.get('group_size', 1)} people
        - Accommodation: {preferences.get('accommodation_type', 'hotel')}
        - Transport: {preferences.get('transport_preference', 'public transport')}
        
        COUNTRY CONTEXT:
        - Currency: {currency}
        - Best time to visit: {country_info.get('best_time', 'Year-round')}
        - Cultural notes: {country_info.get('cultural_notes', 'No specific notes')}
        - Language: {country_info.get('language', 'Local language')}
        
        Include:
        - Daily activities with timings and descriptions (consider local customs and opening hours)
        - Budget breakdown in {currency} (accommodation, food, activities, transport, miscellaneous)
        - 5 essential travel tips specific to {destination} and {preferences.get('destination_country')}
        - Top 5 recommended restaurants with local cuisine types and price ranges in {currency}
        - 3 accommodation suggestions with price ranges in {currency} matching the {preferences.get('budget_type')} budget type
        
        Make it practical, realistic, and culturally appropriate for {preferences.get('destination_country')}.
        Consider local customs, tipping practices, and cultural norms.
        """

        response = client.models.generate_content(
            model="gemini-2.5-pro",
            contents=prompt,
            config=types.GenerateContentConfig(
                response_mime_type="application/json",
                response_schema=ItineraryPlan,
            ),
        )

        if response.text:
            data = json.loads(response.text)
            return ItineraryPlan(**data)
        else:
            raise ValueError("Empty response from Gemini")

    except Exception as e:
        logging.error(f"Error generating itinerary: {e}")
        # Return a basic fallback itinerary
        return ItineraryPlan(
            destination=destination,
            duration_days=duration,
            daily_activities=[],
            budget_breakdown={},
            travel_tips=[],
            recommended_restaurants=[],
            accommodation_suggestions=[]
        )

def get_travel_tips(destination: str, preferences: dict) -> list[str]:
    """Get AI-powered travel tips for the destination."""
    try:
        country_info = preferences.get('country_info', {})
        currency = country_info.get('currency', 'USD')
        
        prompt = f"""
        Provide 8 essential travel tips for visiting {destination} in {preferences.get('destination_country')} considering:
        
        USER CONTEXT:
        - Budget Type: {preferences.get('budget_type', 'mid_range')}
        - Daily Budget: {preferences.get('budget', 100)} {currency}
        - Group size: {preferences.get('group_size', 1)} people
        - Interests: {', '.join(preferences.get('interests', []))}
        
        COUNTRY CONTEXT:
        - Currency: {currency}
        - Language: {country_info.get('language', 'Local language')}
        - Cultural notes: {country_info.get('cultural_notes', 'No specific notes')}
        - Visa requirements: {country_info.get('visa_info', 'Check requirements')}
        
        Focus on practical advice about:
        - Local customs and etiquette specific to {preferences.get('destination_country')}
        - Money-saving tips and currency exchange
        - Safety considerations and local laws
        - Best ways to get around {destination}
        - Food and dining recommendations with local specialties
        - Cultural insights and social norms
        - Packing suggestions for local climate/culture
        - Language tips and useful phrases
        
        Make tips specific to {destination} and {preferences.get('destination_country')}.
        Return as a JSON array of strings.
        """

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
            config=types.GenerateContentConfig(
                response_mime_type="application/json",
                response_schema=list[str],
            ),
        )

        if response.text:
            return json.loads(response.text)
        else:
            return []

    except Exception as e:
        logging.error(f"Error getting travel tips: {e}")
        return []
