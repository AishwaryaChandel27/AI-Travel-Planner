# Analyze the code changes and combine them with the original code to generate the complete modified code.
```
```replit_final_file
try:
    import google.generativeai as genai
    GENAI_AVAILABLE = True
except ImportError:
    GENAI_AVAILABLE = False

import os
import logging
from typing import List, Dict, Any
from pydantic import BaseModel, Field

# Initialize Gemini client
api_key = os.environ.get("GEMINI_API_KEY")
if api_key and GENAI_AVAILABLE:
    try:
        genai.configure(api_key=api_key)
        client = genai
    except Exception as e:
        client = None
        logging.error(f"Failed to configure Gemini: {e}")
        logging.warning("Using fallback recommendations.")
else:
    client = None
    if not api_key:
        logging.warning("GEMINI_API_KEY not found. Using fallback recommendations.")
    if not GENAI_AVAILABLE:
        logging.warning("Google Generative AI not available. Using fallback recommendations.")

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
    # Use fallback if no API key available
    if not client:
        logging.info("Using fallback recommendations due to missing API key")
        return get_fallback_recommendations(preferences)

    try:
        interests_str = ", ".join(preferences.get('interests', []))
        country_info = preferences.get('country_info', {})
        popular_destinations = preferences.get('popular_destinations', [])
        currency = country_info.get('currency', 'USD')

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

        response = genai.GenerativeModel('gemini-2.5-flash').generate_content(prompt)

        if response.text:
            try:
                data = json.loads(response.text)
                return [TravelRecommendation(**rec) for rec in data]
            except json.JSONDecodeError as e:
                logging.error(f"JSONDecodeError: {e}, Response Text: {response.text}")
                return get_fallback_recommendations(preferences)

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
    # Use fallback if no API key available
    if not client:
        logging.info("Using fallback itinerary due to missing API key")
        return get_fallback_itinerary(preferences, destination)

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

        response = genai.GenerativeModel('gemini-2.5-pro').generate_content(prompt)

        if response.text:
            # Parse the response into a structured format
            class ItineraryPlan:
                def __init__(self):
                    self.daily_activities = []
                    self.budget_breakdown = {}
                    self.recommended_restaurants = []
                    self.accommodation_suggestions = []

            plan = ItineraryPlan()

            # Simple parsing - in a real app, you'd want more sophisticated parsing
            lines = response.text.split('\n')
            current_section = None
            current_day = None

            for line in lines:
                line = line.strip()
                if ('Day' in line and ':' in line) or ('day' in line.lower() and ':' in line):
                    current_section = 'activities'
                    current_day = {'day': line, 'activities': []}
                    plan.daily_activities.append(current_day)
                elif 'Budget' in line.lower() or 'Cost' in line.lower():
                    current_section = 'budget'
                elif 'Restaurant' in line.lower() or 'Food' in line.lower() or 'Dining' in line.lower():
                    current_section = 'restaurants'
                elif 'Hotel' in line.lower() or 'Accommodation' in line.lower() or 'Stay' in line.lower():
                    current_section = 'accommodation'
                elif line.startswith('- ') and current_section:
                    if current_section == 'activities' and current_day:
                        activity_text = line[2:]
                        time_part = 'All Day'
                        if ':' in activity_text:
                            parts = activity_text.split(':', 1)
                            if len(parts) == 2 and any(char.isdigit() for char in parts[0]):
                                time_part = parts[0].strip()
                                activity_text = parts[1].strip()

                        current_day['activities'].append({
                            'time': time_part,
                            'activity': activity_text,
                            'description': activity_text,
                            'duration': '2-3 hours'
                        })
                    elif current_section == 'restaurants':
                        restaurant_name = line[2:]
                        plan.recommended_restaurants.append({
                            'name': restaurant_name,
                            'description': f'Recommended restaurant in {destination}',
                            'cuisine_type': 'Local',
                            'price_range': '$$ - $$$'
                        })
                    elif current_section == 'accommodation':
                        hotel_name = line[2:]
                        plan.accommodation_suggestions.append({
                            'name': hotel_name,
                            'description': f'Recommended accommodation in {destination}',
                            'type': 'Hotel',
                            'price_range': '$$ - $$$'
                        })
                elif line and current_section == 'activities' and current_day and not line.startswith('**'):
                    # Additional activity description
                    if current_day['activities']:
                        current_day['activities'][-1]['description'] += ' ' + line

            # Ensure we have at least one day of activities
            if not plan.daily_activities:
                plan.daily_activities = [{
                    'day': 'Day 1: Arrival and Exploration',
                    'activities': [
                        {
                            'time': '10:00 AM',
                            'activity': f'Explore {destination}',
                            'description': f'Start your adventure in {destination}',
                            'duration': '3-4 hours'
                        },
                        {
                            'time': '2:00 PM',
                            'activity': 'Local Lunch',
                            'description': 'Try local cuisine',
                            'duration': '1 hour'
                        },
                        {
                            'time': '4:00 PM',
                            'activity': 'Sightseeing',
                            'description': 'Visit popular attractions',
                            'duration': '2-3 hours'
                        }
                    ]
                }]

            # Set a default budget if none was parsed
            if not plan.budget_breakdown:
                total_budget = preferences.get('budget', 1000)
                plan.budget_breakdown = {
                    'accommodation': total_budget * 0.4,
                    'food': total_budget * 0.3,
                    'activities': total_budget * 0.2,
                    'transport': total_budget * 0.1
                }

            # Ensure we have restaurant recommendations
            if not plan.recommended_restaurants:
                plan.recommended_restaurants = [
                    {
                        'name': f'Local Restaurant in {destination}',
                        'description': 'Great local cuisine and atmosphere',
                        'cuisine_type': 'Local',
                        'price_range': '$$ - $$$'
                    }
                ]

            # Ensure we have accommodation suggestions
            if not plan.accommodation_suggestions:
                plan.accommodation_suggestions = [
                    {
                        'name': f'Hotel in {destination}',
                        'description': 'Comfortable and well-located accommodation',
                        'type': 'Hotel',
                        'price_range': '$$ - $$$'
                    }
                ]

            return plan
        else:
            return None

    except Exception as e:
        logging.error(f"Error generating itinerary: {e}")
        # Return a basic fallback itinerary
        return get_fallback_itinerary(preferences, destination)

def get_travel_tips(destination: str, preferences: dict) -> list[str]:
    """Get AI-powered travel tips for the destination."""
    # Use fallback if no API key available
    if not client:
        return [
            f'Research local customs before visiting {destination}',
            'Always carry local currency for small purchases',
            'Download offline maps and translation apps',
            'Keep copies of important documents',
            'Learn basic phrases in the local language',
            'Respect local dress codes and traditions',
            'Stay aware of your surroundings',
            'Try local cuisine but be cautious with street food'
        ]

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

        response = genai.GenerativeModel('gemini-2.5-flash').generate_content(prompt)

        if response.text:
            try:
                return json.loads(response.text)
            except json.JSONDecodeError as e:
                logging.error(f"JSONDecodeError: {e}, Response Text: {response.text}")
                return []
        else:
            return []

    except Exception as e:
        logging.error(f"Error getting travel tips: {e}")
        return []

def get_fallback_itinerary(preferences: dict, destination: str) -> ItineraryPlan:
    """Generate a fallback itinerary when AI is not available."""
    duration = (preferences.get('end_date') - preferences.get('start_date')).days if preferences.get('end_date') and preferences.get('start_date') else 3

    daily_activities = []
    for i in range(duration):
        day_activities = [
            {
                'time': '09:00',
                'activity': f'Morning exploration of {destination}',
                'description': 'Start your day with local sights and attractions',
                'duration': '3 hours'
            },
            {
                'time': '13:00',
                'activity': 'Local lunch experience',
                'description': 'Try authentic local cuisine',
                'duration': '1.5 hours'
            },
            {
                'time': '15:00',
                'activity': f'Afternoon activities in {destination}',
                'description': 'Explore museums, parks, or cultural sites',
                'duration': '3 hours'
            },
            {
                'time': '19:00',
                'activity': 'Evening dining and relaxation',
                'description': 'Enjoy dinner and evening entertainment',
                'duration': '2 hours'
            }
        ]
        daily_activities.append({
            'day': f'Day {i+1}',
            'activities': day_activities
        })

    budget_breakdown = {
        'accommodation': 100 * duration,
        'food': 60 * duration,
        'activities': 40 * duration,
        'transport': 30 * duration
    }

    recommended_restaurants = [
        {'name': f'{destination} Local Bistro', 'cuisine': 'Local', 'price_range': '20-40'},
        {'name': f'{destination} Fine Dining', 'cuisine': 'International', 'price_range': '50-80'},
        {'name': f'{destination} Street Food', 'cuisine': 'Street Food', 'price_range': '10-20'}
    ]

    accommodation_suggestions = [
        {'name': f'{destination} Hotel', 'type': 'Hotel', 'price_range': '80-120'},
        {'name': f'{destination} Boutique Stay', 'type': 'Boutique', 'price_range': '100-150'},
        {'name': f'{destination} Budget Lodge', 'type': 'Hostel', 'price_range': '30-60'}
    ]

    travel_tips = [
        f'Research local customs before visiting {destination}',
        'Always carry local currency for small vendors',
        'Download offline maps for navigation',
        'Learn a few basic phrases in the local language',
        'Keep important documents in a safe place'
    ]

    return ItineraryPlan(
        destination=destination,
        duration_days=duration,
        daily_activities=daily_activities,
        budget_breakdown=budget_breakdown,
        travel_tips=travel_tips,
        recommended_restaurants=recommended_restaurants,
        accommodation_suggestions=accommodation_suggestions
    )
```This code refactors the AI response parsing and improves error handling for destination recommendations and itinerary generation.