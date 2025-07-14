import json
import logging
import os
from google import genai
from google.genai import types
from pydantic import BaseModel

# Initialize Gemini client
client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY", "default_key"))

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
        
        prompt = f"""
        As a travel expert, recommend 3 destinations based on these preferences:
        - Budget: ${preferences.get('budget', 'Not specified')}
        - Interests: {interests_str}
        - Group size: {preferences.get('group_size', 1)} people
        - Travel dates: {preferences.get('start_date', 'Flexible')} to {preferences.get('end_date', 'Flexible')}
        
        For each destination, provide:
        - Destination name
        - 3-4 reasons why it's perfect for these preferences
        - Best time to visit
        - Estimated budget breakdown (accommodation, food, activities, transport)
        - Top 5 highlights/attractions
        
        Respond with JSON array of recommendations.
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
        
        prompt = f"""
        Create a detailed {duration}-day itinerary for {destination} based on these preferences:
        - Budget: ${preferences.get('budget', 2000)}
        - Interests: {interests_str}
        - Group size: {preferences.get('group_size', 1)} people
        - Accommodation preference: {preferences.get('accommodation_type', 'Hotel')}
        - Transport preference: {preferences.get('transport_preference', 'Public transport')}
        
        Include:
        - Daily activities with timings and descriptions
        - Budget breakdown (accommodation, food, activities, transport, miscellaneous)
        - 5 essential travel tips
        - Top 5 recommended restaurants with cuisine types
        - 3 accommodation suggestions with price ranges
        
        Make it practical and realistic for the budget and preferences.
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
        prompt = f"""
        Provide 8 essential travel tips for visiting {destination} considering:
        - Budget: ${preferences.get('budget', 2000)}
        - Group size: {preferences.get('group_size', 1)} people
        - Interests: {', '.join(preferences.get('interests', []))}
        
        Focus on practical advice about:
        - Local customs and etiquette
        - Money-saving tips
        - Safety considerations
        - Best ways to get around
        - Food and dining recommendations
        - Cultural insights
        - Packing suggestions
        - Language tips
        
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
