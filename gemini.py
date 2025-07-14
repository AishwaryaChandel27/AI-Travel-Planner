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
            ),
        )

        if response.text:
            data = json.loads(response.text)
            return [TravelRecommendation(**rec) for rec in data]
        else:
            raise ValueError("Empty response from Gemini")

    except Exception as e:
        logging.error(f"Error getting destination recommendations: {e}")
        # Return realistic fallback data based on country and preferences
        return get_fallback_recommendations(preferences)

def get_fallback_recommendations(preferences: dict) -> list[TravelRecommendation]:
    """Get realistic fallback recommendations when AI fails."""
    country = preferences.get('destination_country', 'Unknown')
    country_info = preferences.get('country_info', {})
    currency = country_info.get('currency', 'USD')
    popular_destinations = preferences.get('popular_destinations', [])
    budget_type = preferences.get('budget_type', 'mid_range')
    
    # Country-specific fallback data
    fallback_data = {
        'Japan': [
            {
                'destination': 'Tokyo',
                'reasons': ['World-class cuisine and street food', 'Mix of traditional and modern culture', 'Excellent public transportation', 'Safe and clean environment'],
                'best_time_to_visit': 'Spring (March-May) for cherry blossoms or Fall (September-November)',
                'estimated_budget': {'accommodation': 8000, 'food': 4000, 'activities': 3000, 'transport': 2000},
                'highlights': ['Tsukiji Fish Market', 'Senso-ji Temple', 'Shibuya Crossing', 'Tokyo Skytree', 'Meiji Shrine']
            },
            {
                'destination': 'Kyoto',
                'reasons': ['Historic temples and shrines', 'Traditional Japanese culture', 'Beautiful gardens and bamboo forests', 'Geisha districts'],
                'best_time_to_visit': 'Spring for cherry blossoms or Fall for autumn colors',
                'estimated_budget': {'accommodation': 7000, 'food': 3500, 'activities': 2500, 'transport': 1500},
                'highlights': ['Fushimi Inari Shrine', 'Kinkaku-ji Golden Pavilion', 'Arashiyama Bamboo Grove', 'Gion District', 'Kiyomizu-dera Temple']
            }
        ],
        'Thailand': [
            {
                'destination': 'Bangkok',
                'reasons': ['Vibrant street food culture', 'Magnificent temples and palaces', 'Affordable luxury experiences', 'Bustling markets and nightlife'],
                'best_time_to_visit': 'Cool season (November-February)',
                'estimated_budget': {'accommodation': 1200, 'food': 800, 'activities': 600, 'transport': 400},
                'highlights': ['Grand Palace', 'Wat Pho Temple', 'Chatuchak Weekend Market', 'Chao Phraya River', 'Khao San Road']
            },
            {
                'destination': 'Chiang Mai',
                'reasons': ['Rich cultural heritage', 'Mountain temples and nature', 'Authentic Thai cooking classes', 'Elephant sanctuaries'],
                'best_time_to_visit': 'Cool season (November-February)',
                'estimated_budget': {'accommodation': 800, 'food': 600, 'activities': 700, 'transport': 300},
                'highlights': ['Doi Suthep Temple', 'Old City temples', 'Night Bazaar', 'Elephant Nature Park', 'Cooking classes']
            }
        ],
        'India': [
            {
                'destination': 'Delhi',
                'reasons': ['Rich Mughal and British history', 'Incredible street food scene', 'Budget-friendly luxury', 'Gateway to Golden Triangle'],
                'best_time_to_visit': 'Winter (October-March)',
                'estimated_budget': {'accommodation': 2500, 'food': 1500, 'activities': 1000, 'transport': 500},
                'highlights': ['Red Fort', 'India Gate', 'Lotus Temple', 'Chandni Chowk', 'Humayun\'s Tomb']
            },
            {
                'destination': 'Jaipur',
                'reasons': ['Pink City architecture', 'Royal palaces and forts', 'Vibrant local markets', 'Authentic Rajasthani culture'],
                'best_time_to_visit': 'Winter (October-March)',
                'estimated_budget': {'accommodation': 2000, 'food': 1200, 'activities': 800, 'transport': 400},
                'highlights': ['Amber Fort', 'City Palace', 'Hawa Mahal', 'Jantar Mantar', 'Local bazaars']
            }
        ],
        'United Kingdom': [
            {
                'destination': 'London',
                'reasons': ['Rich history and royal heritage', 'World-class museums and galleries', 'Diverse neighborhoods and culture', 'Excellent public transport'],
                'best_time_to_visit': 'Late spring to early autumn (May-September)',
                'estimated_budget': {'accommodation': 120, 'food': 60, 'activities': 40, 'transport': 25},
                'highlights': ['Big Ben & Westminster', 'British Museum', 'Tower of London', 'Buckingham Palace', 'Thames River']
            },
            {
                'destination': 'Edinburgh',
                'reasons': ['Medieval Old Town and elegant New Town', 'Rich Scottish culture and history', 'Stunning castle views', 'Festival city atmosphere'],
                'best_time_to_visit': 'Summer (June-August) for festivals',
                'estimated_budget': {'accommodation': 100, 'food': 50, 'activities': 35, 'transport': 20},
                'highlights': ['Edinburgh Castle', 'Royal Mile', 'Arthur\'s Seat', 'Holyrood Palace', 'Scottish whisky tours']
            }
        ],
        'France': [
            {
                'destination': 'Paris',
                'reasons': ['Iconic landmarks and architecture', 'World-renowned cuisine and wine', 'Art museums and galleries', 'Romantic atmosphere'],
                'best_time_to_visit': 'Late spring to early autumn (May-September)',
                'estimated_budget': {'accommodation': 140, 'food': 70, 'activities': 45, 'transport': 30},
                'highlights': ['Eiffel Tower', 'Louvre Museum', 'Notre-Dame Cathedral', 'Champs-Élysées', 'Montmartre']
            },
            {
                'destination': 'Nice',
                'reasons': ['Beautiful Mediterranean coastline', 'Vibrant markets and old town', 'Perfect weather year-round', 'Gateway to French Riviera'],
                'best_time_to_visit': 'Late spring to early autumn (May-September)',
                'estimated_budget': {'accommodation': 120, 'food': 60, 'activities': 40, 'transport': 25},
                'highlights': ['Promenade des Anglais', 'Old Town (Vieux Nice)', 'Castle Hill', 'Flower Market', 'Beach clubs']
            }
        ]
    }
    
    # Get fallback recommendations for the country
    if country in fallback_data:
        recommendations = []
        for rec_data in fallback_data[country]:
            recommendations.append(TravelRecommendation(**rec_data))
        return recommendations
    else:
        # Generic fallback
        return [
            TravelRecommendation(
                destination=popular_destinations[0] if popular_destinations else f"Capital of {country}",
                reasons=[f"Cultural heart of {country}", "Local cuisine and attractions", "Historical significance", "Good transportation links"],
                best_time_to_visit="Year-round",
                estimated_budget={'accommodation': 100, 'food': 50, 'activities': 40, 'transport': 30},
                highlights=["Main attractions", "Local markets", "Cultural sites", "Historical landmarks", "Local cuisine"]
            )
        ]

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
