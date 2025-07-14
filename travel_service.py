import random
import uuid
from datetime import datetime, timedelta
from typing import Dict, List, Optional

class TravelService:
    """Service class for mock travel booking functionality."""
    
    def __init__(self):
        self.airlines = [
            "United Airlines", "Delta Air Lines", "American Airlines", 
            "Southwest Airlines", "JetBlue Airways", "Alaska Airlines"
        ]
        
        self.hotels = [
            "Hilton", "Marriott", "Hyatt", "Holiday Inn", "Best Western",
            "Sheraton", "Radisson", "Courtyard", "Hampton Inn", "Doubletree"
        ]
        
        self.cities = {
            "New York": {"code": "NYC", "country": "USA"},
            "London": {"code": "LON", "country": "UK"},
            "Paris": {"code": "PAR", "country": "France"},
            "Tokyo": {"code": "TYO", "country": "Japan"},
            "Sydney": {"code": "SYD", "country": "Australia"},
            "Rome": {"code": "ROM", "country": "Italy"},
            "Barcelona": {"code": "BCN", "country": "Spain"},
            "Amsterdam": {"code": "AMS", "country": "Netherlands"},
            "Dubai": {"code": "DXB", "country": "UAE"},
            "Singapore": {"code": "SIN", "country": "Singapore"}
        }

    def search_flights(self, origin: str, destination: str, departure_date: str, 
                      return_date: Optional[str] = None, passengers: int = 1) -> List[Dict]:
        """Mock flight search functionality."""
        flights = []
        
        for i in range(random.randint(3, 8)):
            base_price = random.randint(200, 1500)
            departure_time = f"{random.randint(6, 22):02d}:{random.randint(0, 59):02d}"
            arrival_time = f"{random.randint(6, 22):02d}:{random.randint(0, 59):02d}"
            
            flight = {
                "id": str(uuid.uuid4()),
                "airline": random.choice(self.airlines),
                "flight_number": f"{random.choice(['UA', 'DL', 'AA', 'WN'])}{random.randint(100, 9999)}",
                "origin": origin,
                "destination": destination,
                "departure_date": departure_date,
                "departure_time": departure_time,
                "arrival_time": arrival_time,
                "duration": f"{random.randint(1, 15)}h {random.randint(0, 59)}m",
                "price": base_price * passengers,
                "stops": random.randint(0, 2),
                "aircraft": random.choice(["Boeing 737", "Airbus A320", "Boeing 777", "Airbus A350"]),
                "class": "Economy",
                "seats_available": random.randint(5, 50)
            }
            flights.append(flight)
        
        # Sort by price
        flights.sort(key=lambda x: x['price'])
        return flights

    def search_hotels(self, destination: str, check_in: str, check_out: str, 
                     guests: int = 1, rooms: int = 1) -> List[Dict]:
        """Mock hotel search functionality."""
        hotels = []
        
        for i in range(random.randint(5, 12)):
            base_price = random.randint(50, 500)
            rating = round(random.uniform(3.0, 5.0), 1)
            
            hotel = {
                "id": str(uuid.uuid4()),
                "name": f"{random.choice(self.hotels)} {destination}",
                "address": f"{random.randint(1, 999)} {random.choice(['Main St', 'Park Ave', 'Broadway', 'Central Blvd'])}",
                "rating": rating,
                "price_per_night": base_price,
                "total_price": base_price * self._calculate_nights(check_in, check_out) * rooms,
                "amenities": random.sample([
                    "Free WiFi", "Pool", "Gym", "Restaurant", "Bar", "Spa", 
                    "Business Center", "Pet Friendly", "Airport Shuttle", "Room Service"
                ], random.randint(3, 6)),
                "room_type": random.choice(["Standard Room", "Deluxe Room", "Suite", "Executive Room"]),
                "cancellation": random.choice(["Free cancellation", "Non-refundable", "Partial refund"]),
                "distance_city_center": f"{random.uniform(0.5, 5.0):.1f} km",
                "images": [f"https://picsum.photos/400/300?random={i}"],
                "available_rooms": random.randint(1, 10)
            }
            hotels.append(hotel)
        
        # Sort by rating and price
        hotels.sort(key=lambda x: (-x['rating'], x['price_per_night']))
        return hotels

    def get_activities(self, destination: str, interests: List[str]) -> List[Dict]:
        """Mock activity search functionality."""
        activities = []
        
        activity_types = {
            "adventure": ["Hiking", "Rock Climbing", "Zipline", "Bungee Jumping", "Rafting"],
            "culture": ["Museum Tour", "Historical Walk", "Art Gallery", "Cultural Show", "Local Workshop"],
            "food": ["Food Tour", "Cooking Class", "Wine Tasting", "Street Food Walk", "Local Market Visit"],
            "nature": ["Nature Walk", "Bird Watching", "Botanical Garden", "Beach Day", "Scenic Drive"],
            "nightlife": ["Bar Crawl", "Night Club", "Live Music", "Comedy Show", "Rooftop Bar"],
            "shopping": ["Shopping Tour", "Local Market", "Souvenir Hunt", "Vintage Shopping", "Mall Visit"],
            "relaxation": ["Spa Day", "Yoga Class", "Meditation", "Beach Relaxation", "Wellness Retreat"]
        }
        
        for interest in interests:
            if interest.lower() in activity_types:
                for activity_name in activity_types[interest.lower()]:
                    activity = {
                        "id": str(uuid.uuid4()),
                        "name": f"{activity_name} in {destination}",
                        "type": interest,
                        "description": f"Experience the best {activity_name.lower()} that {destination} has to offer.",
                        "duration": f"{random.randint(1, 8)} hours",
                        "price": random.randint(20, 200),
                        "rating": round(random.uniform(3.5, 5.0), 1),
                        "location": f"{destination} {random.choice(['Downtown', 'Old Town', 'City Center', 'Waterfront'])}",
                        "includes": random.sample([
                            "Professional Guide", "Transportation", "Equipment", "Refreshments", 
                            "Entry Fees", "Photo Service", "Certificate", "Souvenir"
                        ], random.randint(2, 4)),
                        "difficulty": random.choice(["Easy", "Moderate", "Challenging"]),
                        "group_size": f"Max {random.randint(8, 20)} people"
                    }
                    activities.append(activity)
        
        return activities[:random.randint(8, 15)]

    def create_booking(self, booking_type: str, item_id: str, details: Dict) -> Dict:
        """Mock booking creation functionality."""
        booking_reference = f"{booking_type.upper()}{random.randint(100000, 999999)}"
        
        booking = {
            "booking_reference": booking_reference,
            "type": booking_type,
            "item_id": item_id,
            "status": "confirmed",
            "confirmation_number": booking_reference,
            "created_at": datetime.now().isoformat(),
            "details": details,
            "total_amount": details.get('total_price', details.get('price', 0)),
            "payment_method": "Credit Card",
            "cancellation_policy": "Free cancellation up to 24 hours before"
        }
        
        return booking

    def _calculate_nights(self, check_in: str, check_out: str) -> int:
        """Calculate number of nights between check-in and check-out."""
        try:
            check_in_date = datetime.strptime(check_in, "%Y-%m-%d")
            check_out_date = datetime.strptime(check_out, "%Y-%m-%d")
            return (check_out_date - check_in_date).days
        except:
            return 1

    def get_weather_info(self, destination: str) -> Dict:
        """Mock weather information."""
        temperatures = {
            "hot": {"min": 25, "max": 35},
            "warm": {"min": 15, "max": 25},
            "cool": {"min": 5, "max": 15},
            "cold": {"min": -5, "max": 5}
        }
        
        climate = random.choice(list(temperatures.keys()))
        temp_range = temperatures[climate]
        
        return {
            "destination": destination,
            "current_temp": random.randint(temp_range["min"], temp_range["max"]),
            "climate": climate,
            "conditions": random.choice(["Sunny", "Partly Cloudy", "Cloudy", "Light Rain", "Clear"]),
            "humidity": random.randint(40, 80),
            "wind_speed": random.randint(5, 25),
            "forecast": [
                {
                    "day": (datetime.now() + timedelta(days=i)).strftime("%A"),
                    "high": random.randint(temp_range["min"], temp_range["max"]),
                    "low": random.randint(temp_range["min"] - 5, temp_range["max"] - 5),
                    "condition": random.choice(["Sunny", "Cloudy", "Rain", "Partly Cloudy"])
                }
                for i in range(5)
            ]
        }
