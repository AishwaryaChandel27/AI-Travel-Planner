
import random
from datetime import datetime, timedelta
from typing import List, Dict, Any

class TravelService:
    """Service for handling travel-related operations like booking flights, hotels, and activities."""
    
    def __init__(self):
        self.booking_counter = 1000
    
    def get_weather_info(self, destination: str) -> Dict[str, Any]:
        """Get weather information for a destination."""
        # Mock weather data
        weather_conditions = ['Sunny', 'Partly Cloudy', 'Cloudy', 'Light Rain', 'Clear']
        
        return {
            'destination': destination,
            'current_temp': random.randint(15, 30),
            'condition': random.choice(weather_conditions),
            'humidity': random.randint(40, 80),
            'wind_speed': random.randint(5, 25),
            'forecast': [
                {
                    'day': 'Today',
                    'high': random.randint(20, 35),
                    'low': random.randint(10, 20),
                    'condition': random.choice(weather_conditions)
                },
                {
                    'day': 'Tomorrow',
                    'high': random.randint(20, 35),
                    'low': random.randint(10, 20),
                    'condition': random.choice(weather_conditions)
                },
                {
                    'day': 'Day 3',
                    'high': random.randint(20, 35),
                    'low': random.randint(10, 20),
                    'condition': random.choice(weather_conditions)
                }
            ]
        }
    
    def get_activities(self, destination: str, interests: List[str]) -> List[Dict[str, Any]]:
        """Get activities for a destination based on interests."""
        activities_pool = {
            'culture': [
                {'name': f'{destination} Historical Museum', 'description': 'Explore local history and culture', 'price': 25, 'duration': '2-3 hours'},
                {'name': f'{destination} Art Gallery', 'description': 'Contemporary and classical art exhibitions', 'price': 20, 'duration': '1-2 hours'},
                {'name': 'Cultural Walking Tour', 'description': 'Guided tour of historical sites', 'price': 35, 'duration': '3 hours'},
                {'name': 'Traditional Craft Workshop', 'description': 'Learn local crafts and traditions', 'price': 45, 'duration': '2 hours'}
            ],
            'food': [
                {'name': 'Food Market Tour', 'description': 'Explore local markets and taste specialties', 'price': 40, 'duration': '3 hours'},
                {'name': 'Cooking Class', 'description': 'Learn to cook traditional dishes', 'price': 65, 'duration': '4 hours'},
                {'name': 'Wine Tasting', 'description': 'Sample local wines and learn about production', 'price': 55, 'duration': '2 hours'},
                {'name': 'Street Food Tour', 'description': 'Discover the best street food spots', 'price': 30, 'duration': '2.5 hours'}
            ],
            'adventure': [
                {'name': 'Hiking Tour', 'description': 'Explore scenic trails and viewpoints', 'price': 50, 'duration': '6 hours'},
                {'name': 'Bike Rental', 'description': 'Explore the city on two wheels', 'price': 25, 'duration': 'Full day'},
                {'name': 'Kayaking Experience', 'description': 'Paddle through scenic waterways', 'price': 60, 'duration': '4 hours'},
                {'name': 'Rock Climbing', 'description': 'Guided climbing experience', 'price': 80, 'duration': '5 hours'}
            ],
            'nature': [
                {'name': 'Nature Walk', 'description': 'Guided walk through natural areas', 'price': 30, 'duration': '3 hours'},
                {'name': 'Botanical Garden Visit', 'description': 'Explore diverse plant collections', 'price': 15, 'duration': '2 hours'},
                {'name': 'Wildlife Watching', 'description': 'Spot local wildlife in natural habitat', 'price': 45, 'duration': '4 hours'},
                {'name': 'Photography Tour', 'description': 'Capture stunning natural landscapes', 'price': 55, 'duration': '3 hours'}
            ],
            'relaxation': [
                {'name': 'Spa Treatment', 'description': 'Rejuvenating spa experience', 'price': 120, 'duration': '2 hours'},
                {'name': 'Beach Day', 'description': 'Relax on pristine beaches', 'price': 10, 'duration': 'Full day'},
                {'name': 'Meditation Class', 'description': 'Learn mindfulness and meditation', 'price': 35, 'duration': '1.5 hours'},
                {'name': 'Yoga Session', 'description': 'Outdoor yoga with scenic views', 'price': 25, 'duration': '1 hour'}
            ]
        }
        
        selected_activities = []
        for interest in interests:
            if interest in activities_pool:
                selected_activities.extend(activities_pool[interest])
        
        # If no interests match, return general activities
        if not selected_activities:
            selected_activities = activities_pool['culture'] + activities_pool['food']
        
        return selected_activities[:8]  # Return max 8 activities
    
    def search_flights(self, origin: str, destination: str, departure_date: str, return_date: str, passengers: int) -> List[Dict[str, Any]]:
        """Search for flights (mock implementation)."""
        airlines = ['SkyWings', 'AirTravel', 'CloudHopper', 'JetStream', 'FlyHigh']
        flight_times = ['06:30', '09:15', '12:45', '15:30', '18:20', '21:10']
        
        flights = []
        for i in range(5):  # Return 5 flight options
            price = random.randint(200, 800)
            airline = random.choice(airlines)
            departure_time = random.choice(flight_times)
            arrival_time = flight_times[(flight_times.index(departure_time) + random.randint(2, 4)) % len(flight_times)]
            
            flights.append({
                'id': f'flight_{i+1}',
                'airline': airline,
                'flight_number': f'{airline[:2].upper()}{random.randint(100, 999)}',
                'origin': origin,
                'destination': destination,
                'departure_date': departure_date,
                'return_date': return_date,
                'departure_time': departure_time,
                'arrival_time': arrival_time,
                'price': price,
                'passengers': passengers,
                'total_price': price * passengers,
                'duration': f'{random.randint(2, 12)}h {random.randint(0, 59)}m',
                'stops': random.randint(0, 2),
                'baggage': '1 checked bag included',
                'provider': 'FlightBooking Pro'
            })
        
        return sorted(flights, key=lambda x: x['total_price'])
    
    def search_hotels(self, destination: str, check_in: str, check_out: str, guests: int) -> List[Dict[str, Any]]:
        """Search for hotels (mock implementation)."""
        hotel_types = ['Hotel', 'Resort', 'Boutique Hotel', 'Business Hotel', 'Luxury Hotel']
        amenities_pool = ['Free WiFi', 'Pool', 'Gym', 'Spa', 'Restaurant', 'Bar', 'Room Service', 'Concierge', 'Parking']
        
        hotels = []
        for i in range(6):  # Return 6 hotel options
            price_per_night = random.randint(80, 400)
            hotel_type = random.choice(hotel_types)
            stars = random.randint(3, 5)
            amenities = random.sample(amenities_pool, random.randint(4, 7))
            
            hotels.append({
                'id': f'hotel_{i+1}',
                'name': f'{destination} {hotel_type}',
                'type': hotel_type,
                'stars': stars,
                'destination': destination,
                'check_in': check_in,
                'check_out': check_out,
                'guests': guests,
                'price_per_night': price_per_night,
                'total_price': price_per_night * 7,  # Assuming 7 nights
                'rating': round(random.uniform(3.5, 4.8), 1),
                'reviews': random.randint(50, 500),
                'amenities': amenities,
                'description': f'Comfortable {hotel_type.lower()} in the heart of {destination}',
                'provider': 'HotelBooking Plus'
            })
        
        return sorted(hotels, key=lambda x: x['total_price'])
    
    def create_booking(self, booking_type: str, item_id: str, details: Dict[str, Any]) -> Dict[str, Any]:
        """Create a booking (mock implementation)."""
        self.booking_counter += 1
        booking_reference = f'{booking_type.upper()}{self.booking_counter}'
        
        booking_info = {
            'booking_reference': booking_reference,
            'booking_type': booking_type,
            'item_id': item_id,
            'status': 'confirmed',
            'booking_date': datetime.now().isoformat(),
            'total_amount': details.get('total_price', details.get('price', 0)),
            'currency': 'USD',
            'confirmation_email': 'travel@example.com',
            'customer_service': '+1-800-TRAVEL',
            'cancellation_policy': 'Free cancellation up to 24 hours before travel',
            'details': details
        }
        
        return booking_info
