#!/usr/bin/env python3
"""
AI Travel Planner Demo Script
This script demonstrates the key features of the AI Travel Planner application.
"""

import os
import sys
from datetime import datetime, timedelta

# Add the project root to the Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from gemini import get_destination_recommendations, generate_itinerary, get_travel_tips
from travel_service import TravelService

def demo_ai_recommendations():
    """Demonstrate AI-powered destination recommendations."""
    print("🧠 AI-Powered Destination Recommendations Demo")
    print("=" * 50)
    
    # Sample preferences
    preferences = {
        'budget': 2500,
        'start_date': datetime.now().date() + timedelta(days=30),
        'end_date': datetime.now().date() + timedelta(days=37),
        'group_size': 2,
        'interests': ['culture', 'food', 'adventure'],
        'accommodation_type': 'hotel',
        'transport_preference': 'public_transport'
    }
    
    print(f"Sample preferences: {preferences}")
    print("\nGenerating AI recommendations...")
    
    try:
        recommendations = get_destination_recommendations(preferences)
        
        if recommendations:
            print(f"\n✅ Generated {len(recommendations)} recommendations:")
            for i, rec in enumerate(recommendations, 1):
                print(f"\n{i}. {rec.destination}")
                print(f"   Best time: {rec.best_time_to_visit}")
                print(f"   Highlights: {', '.join(rec.highlights[:3])}")
        else:
            print("\n❌ No recommendations generated (check your GEMINI_API_KEY)")
            
    except Exception as e:
        print(f"\n❌ Error: {e}")
        if "GEMINI_API_KEY" in str(e):
            print("💡 Please set your GEMINI_API_KEY environment variable")

def demo_travel_service():
    """Demonstrate the travel booking service."""
    print("\n\n🏨 Travel Booking Service Demo")
    print("=" * 50)
    
    service = TravelService()
    
    # Demo flight search
    print("\n✈️  Flight Search:")
    flights = service.search_flights("New York", "Paris", "2025-08-01", "2025-08-08", 2)
    if flights:
        print(f"Found {len(flights)} flights:")
        for flight in flights[:2]:  # Show first 2
            print(f"  - {flight['airline']} {flight['flight_number']}: ${flight['price']}")
    
    # Demo hotel search
    print("\n🏨 Hotel Search:")
    hotels = service.search_hotels("Paris", "2025-08-01", "2025-08-08", 2)
    if hotels:
        print(f"Found {len(hotels)} hotels:")
        for hotel in hotels[:2]:  # Show first 2
            print(f"  - {hotel['name']}: ${hotel['price_per_night']}/night")
    
    # Demo activities
    print("\n🎯 Activities:")
    activities = service.get_activities("Paris", ["culture", "food"])
    if activities:
        print(f"Found {len(activities)} activities:")
        for activity in activities[:3]:  # Show first 3
            print(f"  - {activity['name']}: ${activity['price']}")

def demo_itinerary_generation():
    """Demonstrate AI itinerary generation."""
    print("\n\n📅 AI Itinerary Generation Demo")
    print("=" * 50)
    
    preferences = {
        'budget': 2500,
        'start_date': datetime.now().date() + timedelta(days=30),
        'end_date': datetime.now().date() + timedelta(days=37),
        'group_size': 2,
        'interests': ['culture', 'food', 'adventure'],
        'accommodation_type': 'hotel',
        'transport_preference': 'public_transport'
    }
    
    destination = "Paris"
    print(f"Generating itinerary for: {destination}")
    
    try:
        itinerary = generate_itinerary(preferences, destination)
        
        if itinerary and itinerary.daily_activities:
            print(f"\n✅ Generated {itinerary.duration_days}-day itinerary:")
            print(f"Destination: {itinerary.destination}")
            print(f"Activities: {len(itinerary.daily_activities)} days planned")
            
            # Show first day's activities
            if itinerary.daily_activities:
                first_day = itinerary.daily_activities[0]
                print(f"\nDay 1 sample activities:")
                activities = first_day.get('activities', [])
                for activity in activities[:2]:  # Show first 2
                    if isinstance(activity, dict):
                        print(f"  - {activity.get('activity', 'Activity')}")
        else:
            print("\n❌ No itinerary generated (check your GEMINI_API_KEY)")
            
    except Exception as e:
        print(f"\n❌ Error: {e}")
        if "GEMINI_API_KEY" in str(e):
            print("💡 Please set your GEMINI_API_KEY environment variable")

def main():
    """Run the complete demo."""
    print("🌍 AI Travel Planner - Feature Demo")
    print("=" * 60)
    
    # Check if API key is set
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("\n⚠️  Warning: GEMINI_API_KEY not found in environment")
        print("AI features will not work without a valid API key")
        print("Get your free key at: https://aistudio.google.com/app/apikey")
    
    # Run demos
    demo_ai_recommendations()
    demo_travel_service()
    demo_itinerary_generation()
    
    print("\n\n🎉 Demo completed!")
    print("To run the full application: python main.py")
    print("Then visit: http://localhost:5000")

if __name__ == "__main__":
    main()