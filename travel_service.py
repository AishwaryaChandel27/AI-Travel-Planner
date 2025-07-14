import json
import random
from datetime import datetime, timedelta

class TravelService:
    """Mock travel service for flights, hotels, and activities."""

    def get_weather_info(self, destination):
        """Get mock weather information for a destination."""
        conditions = ['Sunny', 'Partly Cloudy', 'Cloudy', 'Light Rain', 'Clear']

        current_weather = {
            'temperature': random.randint(15, 30),
            'condition': random.choice(conditions),
            'humidity': random.randint(40, 80),
            'wind_speed': random.randint(5, 20)
        }

        # Generate 5-day forecast
        forecast = []
        for i in range(5):
            date = datetime.now() + timedelta(days=i)
            forecast.append({
                'day': date.strftime('%A'),
                'condition': random.choice(conditions),
                'high': random.randint(20, 35),
                'low': random.randint(10, 25)
            })

        return {
            'current': current_weather,
            'forecast': forecast
        }

    def get_activities(self, destination, interests):
        """Get mock activities for a destination based on interests."""
        activities_data = {
            'culture': [
                {'name': 'Historical Museum Tour', 'description': 'Explore local history and culture', 'price': 25, 'duration': '2 hours'},
                {'name': 'Traditional Art Gallery', 'description': 'Local art and exhibitions', 'price': 15, 'duration': '1.5 hours'},
                {'name': 'Cultural Walking Tour', 'description': 'Guided tour of cultural sites', 'price': 30, 'duration': '3 hours'}
            ],
            'food': [
                {'name': 'Street Food Tour', 'description': 'Taste authentic local cuisine', 'price': 40, 'duration': '3 hours'},
                {'name': 'Cooking Class', 'description': 'Learn to cook local dishes', 'price': 60, 'duration': '4 hours'},
                {'name': 'Market Visit', 'description': 'Explore local food markets', 'price': 20, 'duration': '2 hours'}
            ],
            'adventure': [
                {'name': 'Hiking Trail', 'description': 'Scenic hiking experience', 'price': 35, 'duration': '4 hours'},
                {'name': 'Water Sports', 'description': 'Kayaking or snorkeling', 'price': 50, 'duration': '3 hours'},
                {'name': 'Adventure Park', 'description': 'Zip-lining and climbing', 'price': 45, 'duration': '3 hours'}
            ],
            'shopping': [
                {'name': 'Local Markets', 'description': 'Traditional shopping experience', 'price': 10, 'duration': '2 hours'},
                {'name': 'Artisan Workshops', 'description': 'Meet local craftspeople', 'price': 25, 'duration': '1.5 hours'},
                {'name': 'Shopping District Tour', 'description': 'Best shopping areas', 'price': 20, 'duration': '2.5 hours'}
            ],
            'nature': [
                {'name': 'Botanical Garden', 'description': 'Beautiful plant collections', 'price': 15, 'duration': '2 hours'},
                {'name': 'Nature Walk', 'description': 'Peaceful nature experience', 'price': 25, 'duration': '3 hours'},
                {'name': 'Wildlife Watching', 'description': 'Observe local wildlife', 'price': 40, 'duration': '4 hours'}
            ]
        }

        activities = []
        for interest in interests:
            if interest in activities_data:
                activities.extend(activities_data[interest])

        # Add some general activities if none found
        if not activities:
            activities = [
                {'name': 'City Tour', 'description': 'General city sightseeing', 'price': 30, 'duration': '3 hours'},
                {'name': 'Local Experience', 'description': 'Authentic local activity', 'price': 25, 'duration': '2 hours'}
            ]

        return activities[:8]  # Return max 8 activities

    def search_flights(self, origin, destination, departure_date, return_date, passengers):
        """Mock flight search results."""
        airlines = ['AirTravel', 'SkyWings', 'CloudLine', 'FastJet', 'BlueAir']

        flights = []
        for i in range(3):
            base_price = random.randint(300, 800)
            flights.append({
                'id': f'flight_{i+1}',
                'airline': random.choice(airlines),
                'departure_time': f'{random.randint(6, 22):02d}:{random.randint(0, 59):02d}',
                'arrival_time': f'{random.randint(6, 22):02d}:{random.randint(0, 59):02d}',
                'duration': f'{random.randint(2, 12)}h {random.randint(0, 59)}m',
                'price': base_price * passengers,
                'stops': random.randint(0, 2),
                'provider': random.choice(airlines)
            })

        return flights

    def search_hotels(self, destination, check_in, check_out, guests):
        """Mock hotel search results."""
        hotel_types = ['Hotel', 'Resort', 'Boutique Hotel', 'Luxury Hotel', 'Budget Hotel']

        hotels = []
        for i in range(4):
            base_price = random.randint(80, 300)
            hotels.append({
                'id': f'hotel_{i+1}',
                'name': f'{random.choice(hotel_types)} {destination}',
                'rating': random.randint(3, 5),
                'price_per_night': base_price,
                'total_price': base_price * 3,  # Assuming 3 nights
                'amenities': ['WiFi', 'Breakfast', 'Pool', 'Gym'][:random.randint(2, 4)],
                'location': f'{destination} City Center',
                'provider': random.choice(['BookingCom', 'Hotels.com', 'Agoda'])
            })

        return hotels

    def create_booking(self, booking_type, item_id, details):
        """Mock booking creation."""
        booking_reference = f'BK{random.randint(100000, 999999)}'

        booking_info = {
            'booking_reference': booking_reference,
            'status': 'confirmed',
            'total_amount': details.get('price', random.randint(50, 500)),
            'booking_date': datetime.now().isoformat(),
            'details': details
        }

        return booking_info