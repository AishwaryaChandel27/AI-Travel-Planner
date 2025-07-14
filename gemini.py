
import os
import logging
from typing import Dict, List, Any, Optional
import json

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Try to import Google Generative AI
try:
    import google.generativeai as genai
    GEMINI_AVAILABLE = True
except ImportError:
    GEMINI_AVAILABLE = False
    logger.warning("Google Generative AI not available. Using fallback responses.")

# Configure Gemini if available
if GEMINI_AVAILABLE:
    api_key = os.environ.get("GEMINI_API_KEY")
    if api_key:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-pro')
    else:
        GEMINI_AVAILABLE = False
        logger.warning("GEMINI_API_KEY not found. Using fallback responses.")

def get_destination_recommendations(preferences: Dict[str, Any]) -> List[Dict[str, Any]]:
    """Get AI-powered destination recommendations based on user preferences."""
    
    country = preferences.get('destination_country', 'France')
    budget_type = preferences.get('budget_type', 'mid_range')
    interests = preferences.get('interests', [])
    budget = preferences.get('budget', 150)
    
    if GEMINI_AVAILABLE:
        try:
            prompt = f"""
            As a travel expert, recommend 3 specific destinations in {country} based on these preferences:
            - Budget type: {budget_type}
            - Daily budget: ${budget}
            - Interests: {', '.join(interests) if interests else 'general tourism'}
            - Group size: {preferences.get('group_size', 2)}
            
            For each destination, provide:
            1. City/destination name
            2. 3-4 reasons why it's perfect for this traveler
            3. Best time to visit
            4. Estimated daily budget breakdown (accommodation, food, activities, transport)
            5. Top 3-5 highlights/attractions
            
            Format as JSON array with this structure:
            [
                {{
                    "destination": "City Name",
                    "reasons": ["reason1", "reason2", "reason3"],
                    "best_time_to_visit": "season/months",
                    "estimated_budget": {{
                        "accommodation": 80,
                        "food": 50,
                        "activities": 40,
                        "transport": 20
                    }},
                    "highlights": ["attraction1", "attraction2", "attraction3"]
                }}
            ]
            """
            
            response = model.generate_content(prompt)
            
            # Try to parse JSON response
            try:
                # Clean the response text
                response_text = response.text.strip()
                if response_text.startswith('```json'):
                    response_text = response_text[7:]
                if response_text.endswith('```'):
                    response_text = response_text[:-3]
                    
                recommendations = json.loads(response_text.strip())
                if isinstance(recommendations, list) and len(recommendations) > 0:
                    return recommendations
            except json.JSONDecodeError:
                logger.warning("Failed to parse Gemini JSON response, using fallback")
                
        except Exception as e:
            logger.error(f"Gemini API error: {e}")
    
    # Fallback recommendations
    return get_fallback_recommendations(country, budget_type, interests, budget)

def generate_itinerary(preferences: Dict[str, Any], destination: str) -> Dict[str, Any]:
    """Generate a detailed itinerary for the selected destination."""
    
    start_date = preferences.get('start_date')
    end_date = preferences.get('end_date')
    interests = preferences.get('interests', [])
    budget = preferences.get('budget', 150)
    group_size = preferences.get('group_size', 2)
    
    if GEMINI_AVAILABLE:
        try:
            prompt = f"""
            Create a detailed {(end_date - start_date).days if start_date and end_date else 5}-day itinerary for {destination}.
            
            Traveler preferences:
            - Interests: {', '.join(interests) if interests else 'general sightseeing'}
            - Daily budget: ${budget}
            - Group size: {group_size}
            - Travel dates: {start_date} to {end_date}
            
            Provide:
            1. Daily activities with time slots
            2. Budget breakdown by category
            3. Restaurant recommendations
            4. Accommodation suggestions
            
            Format as JSON:
            {{
                "daily_activities": [
                    {{
                        "day": 1,
                        "date": "YYYY-MM-DD",
                        "activities": [
                            {{
                                "time": "9:00 AM",
                                "activity": "Activity name",
                                "description": "Brief description",
                                "cost": 25,
                                "duration": "2 hours"
                            }}
                        ]
                    }}
                ],
                "budget_breakdown": {{
                    "accommodation": 400,
                    "food": 300,
                    "activities": 200,
                    "transport": 100,
                    "total": 1000
                }},
                "recommended_restaurants": [
                    {{
                        "name": "Restaurant Name",
                        "cuisine": "Type",
                        "price_range": "$$",
                        "specialty": "Famous dish"
                    }}
                ],
                "accommodation_suggestions": [
                    {{
                        "name": "Hotel Name",
                        "type": "hotel/hostel/etc",
                        "price_per_night": 80,
                        "rating": 4.5,
                        "location": "Area name"
                    }}
                ]
            }}
            """
            
            response = model.generate_content(prompt)
            
            try:
                response_text = response.text.strip()
                if response_text.startswith('```json'):
                    response_text = response_text[7:]
                if response_text.endswith('```'):
                    response_text = response_text[:-3]
                    
                itinerary = json.loads(response_text.strip())
                return itinerary
                
            except json.JSONDecodeError:
                logger.warning("Failed to parse Gemini itinerary response, using fallback")
                
        except Exception as e:
            logger.error(f"Gemini API error generating itinerary: {e}")
    
    # Fallback itinerary
    return get_fallback_itinerary(destination, preferences)

def get_travel_tips(destination: str, preferences: Dict[str, Any]) -> List[str]:
    """Get travel tips for the destination."""
    
    if GEMINI_AVAILABLE:
        try:
            prompt = f"""
            Provide 5-7 practical travel tips for visiting {destination}.
            Consider:
            - Budget type: {preferences.get('budget_type', 'mid_range')}
            - Interests: {', '.join(preferences.get('interests', []))}
            - Group size: {preferences.get('group_size', 2)}
            
            Focus on:
            - Local customs and etiquette
            - Money and payment tips
            - Transportation advice
            - Safety considerations
            - Best times to visit attractions
            - Local food recommendations
            
            Return as a JSON array of strings:
            ["tip1", "tip2", "tip3", ...]
            """
            
            response = model.generate_content(prompt)
            
            try:
                response_text = response.text.strip()
                if response_text.startswith('```json'):
                    response_text = response_text[7:]
                if response_text.endswith('```'):
                    response_text = response_text[:-3]
                    
                tips = json.loads(response_text.strip())
                if isinstance(tips, list):
                    return tips
                    
            except json.JSONDecodeError:
                logger.warning("Failed to parse Gemini tips response, using fallback")
                
        except Exception as e:
            logger.error(f"Gemini API error getting travel tips: {e}")
    
    # Fallback tips
    return get_fallback_tips(destination)

def get_fallback_recommendations(country: str, budget_type: str, interests: List[str], budget: float) -> List[Dict[str, Any]]:
    """Fallback recommendations when AI is unavailable."""
    
    fallback_data = {
        'France': [
            {
                'destination': 'Paris',
                'reasons': ['Iconic landmarks like Eiffel Tower', 'World-class museums and art', 'Romantic atmosphere', 'Excellent cuisine and wine'],
                'best_time_to_visit': 'Late spring to early autumn (May-September)',
                'estimated_budget': {'accommodation': 120, 'food': 60, 'activities': 50, 'transport': 20},
                'highlights': ['Eiffel Tower', 'Louvre Museum', 'Notre-Dame Cathedral', 'Seine River Cruise', 'Montmartre']
            },
            {
                'destination': 'Nice',
                'reasons': ['Beautiful Mediterranean coast', 'Vibrant Old Town', 'Perfect weather', 'Gateway to French Riviera'],
                'best_time_to_visit': 'May to September',
                'estimated_budget': {'accommodation': 100, 'food': 50, 'activities': 40, 'transport': 15},
                'highlights': ['Promenade des Anglais', 'Old Town', 'Castle Hill', 'Beach clubs', 'Day trips to Monaco']
            },
            {
                'destination': 'Lyon',
                'reasons': ['UNESCO World Heritage sites', 'Gastronomic capital', 'Beautiful Renaissance architecture', 'Less crowded than Paris'],
                'best_time_to_visit': 'April to October',
                'estimated_budget': {'accommodation': 90, 'food': 55, 'activities': 35, 'transport': 20},
                'highlights': ['Vieux Lyon', 'Basilica of Notre-Dame', 'Traboules', 'Food markets', 'Parc de la Tête d\'Or']
            }
        ],
        'Italy': [
            {
                'destination': 'Rome',
                'reasons': ['Ancient history and ruins', 'Vatican City', 'Amazing Italian cuisine', 'Walkable historic center'],
                'best_time_to_visit': 'April to June, September to October',
                'estimated_budget': {'accommodation': 110, 'food': 55, 'activities': 45, 'transport': 15},
                'highlights': ['Colosseum', 'Vatican Museums', 'Roman Forum', 'Trevi Fountain', 'Pantheon']
            },
            {
                'destination': 'Florence',
                'reasons': ['Renaissance art and architecture', 'Compact historic center', 'Excellent museums', 'Tuscan cuisine'],
                'best_time_to_visit': 'April to June, September to October',
                'estimated_budget': {'accommodation': 100, 'food': 50, 'activities': 40, 'transport': 10},
                'highlights': ['Duomo Cathedral', 'Uffizi Gallery', 'Ponte Vecchio', 'Palazzo Pitti', 'Boboli Gardens']
            },
            {
                'destination': 'Venice',
                'reasons': ['Unique canal system', 'Romantic gondola rides', 'St. Mark\'s Square', 'Rich maritime history'],
                'best_time_to_visit': 'April to June, September to November',
                'estimated_budget': {'accommodation': 130, 'food': 60, 'activities': 50, 'transport': 20},
                'highlights': ['St. Mark\'s Basilica', 'Doge\'s Palace', 'Rialto Bridge', 'Gondola rides', 'Murano Island']
            }
        ]
    }
    
    return fallback_data.get(country, fallback_data['France'])

def get_fallback_itinerary(destination: str, preferences: Dict[str, Any]) -> Dict[str, Any]:
    """Fallback itinerary when AI is unavailable."""
    
    return {
        'daily_activities': [
            {
                'day': 1,
                'date': str(preferences.get('start_date', '2024-06-01')),
                'activities': [
                    {
                        'time': '9:00 AM',
                        'activity': f'Arrival in {destination}',
                        'description': 'Check-in to accommodation and get oriented',
                        'cost': 0,
                        'duration': '2 hours'
                    },
                    {
                        'time': '11:00 AM',
                        'activity': 'City Walking Tour',
                        'description': 'Explore the main historic areas and get your bearings',
                        'cost': 25,
                        'duration': '3 hours'
                    },
                    {
                        'time': '2:00 PM',
                        'activity': 'Local Lunch',
                        'description': 'Try traditional local cuisine',
                        'cost': 35,
                        'duration': '1.5 hours'
                    },
                    {
                        'time': '4:00 PM',
                        'activity': 'Main Attraction Visit',
                        'description': f'Visit the most famous landmark in {destination}',
                        'cost': 20,
                        'duration': '2 hours'
                    }
                ]
            },
            {
                'day': 2,
                'date': str(preferences.get('start_date', '2024-06-02')),
                'activities': [
                    {
                        'time': '9:00 AM',
                        'activity': 'Museum Visit',
                        'description': 'Explore local art and history',
                        'cost': 15,
                        'duration': '3 hours'
                    },
                    {
                        'time': '1:00 PM',
                        'activity': 'Local Market Tour',
                        'description': 'Experience local culture and food',
                        'cost': 30,
                        'duration': '2 hours'
                    },
                    {
                        'time': '4:00 PM',
                        'activity': 'Neighborhood Exploration',
                        'description': 'Discover hidden gems and local life',
                        'cost': 10,
                        'duration': '3 hours'
                    }
                ]
            }
        ],
        'budget_breakdown': {
            'accommodation': int(preferences.get('budget', 150) * 0.4 * 5),
            'food': int(preferences.get('budget', 150) * 0.3 * 5),
            'activities': int(preferences.get('budget', 150) * 0.2 * 5),
            'transport': int(preferences.get('budget', 150) * 0.1 * 5),
            'total': int(preferences.get('budget', 150) * 5)
        },
        'recommended_restaurants': [
            {
                'name': f'Local Bistro {destination}',
                'cuisine': 'Local',
                'price_range': '$$',
                'specialty': 'Traditional dishes'
            },
            {
                'name': f'{destination} Market Cafe',
                'cuisine': 'Casual',
                'price_range': '$',
                'specialty': 'Fresh local ingredients'
            }
        ],
        'accommodation_suggestions': [
            {
                'name': f'{destination} Central Hotel',
                'type': 'hotel',
                'price_per_night': int(preferences.get('budget', 150) * 0.4),
                'rating': 4.2,
                'location': 'City Center'
            }
        ]
    }

def get_fallback_tips(destination: str) -> List[str]:
    """Fallback travel tips when AI is unavailable."""
    
    return [
        f"Research local customs and etiquette before visiting {destination}",
        "Always carry some local currency for small purchases and tips",
        "Download offline maps and translation apps before traveling",
        "Book popular attractions in advance to avoid long queues",
        "Try local specialties but be cautious with street food if you have a sensitive stomach",
        "Keep copies of important documents in separate locations",
        "Learn a few basic phrases in the local language - locals appreciate the effort"
    ]
