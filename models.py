from datetime import datetime
from sqlalchemy import Column, Integer, String, Text, Float, DateTime, ForeignKey, JSON
from sqlalchemy.orm import relationship
from app import db

class TravelPreference(db.Model):
    """Model for storing user travel preferences."""
    __tablename__ = 'travel_preferences'

    id = Column(Integer, primary_key=True)
    session_id = Column(String(100), nullable=False)
    destination_country = Column(String(100), nullable=False)
    budget_type = Column(String(50), nullable=False)
    budget = Column(Float, nullable=False)
    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime, nullable=False)
    group_size = Column(Integer, nullable=False)
    interests = Column(Text, nullable=False)  # Store as JSON string for SQLite compatibility

    @property
    def interests_list(self):
        """Get interests as a list."""
        import json
        try:
            return json.loads(self.interests) if isinstance(self.interests, str) else self.interests
        except (json.JSONDecodeError, TypeError):
            return []

    @interests_list.setter
    def interests_list(self, value):
        """Set interests from a list."""
        import json
        self.interests = json.dumps(value) if isinstance(value, list) else str(value)

    accommodation_type = Column(String(50), nullable=False)
    transport_preference = Column(String(50), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationship
    itineraries = relationship('Itinerary', back_populates='preference')

class Itinerary(db.Model):
    """Model for storing generated itineraries."""
    __tablename__ = 'itineraries'

    id = Column(Integer, primary_key=True)
    session_id = Column(String(100), nullable=False)
    preference_id = Column(Integer, ForeignKey('travel_preferences.id'), nullable=False)
    destination = Column(String(100), nullable=False)
    title = Column(String(200), nullable=False)
    description = Column(Text)
    activities = Column(Text, nullable=False)  # Store as JSON string
    budget_breakdown = Column(Text, nullable=False)  # Store as JSON string
    recommendations = Column(Text)  # Store as JSON string

    @property
    def activities_data(self):
        """Get activities as parsed data."""
        import json
        try:
            return json.loads(self.activities) if isinstance(self.activities, str) else self.activities
        except (json.JSONDecodeError, TypeError):
            return []

    @property
    def budget_data(self):
        """Get budget breakdown as parsed data."""
        import json
        try:
            return json.loads(self.budget_breakdown) if isinstance(self.budget_breakdown, str) else self.budget_breakdown
        except (json.JSONDecodeError, TypeError):
            return {}

    @property
    def recommendations_data(self):
        """Get recommendations as parsed data."""
        import json
        try:
            return json.loads(self.recommendations) if isinstance(self.recommendations, str) else self.recommendations
        except (json.JSONDecodeError, TypeError):
            return {}

    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationships
    preference = relationship('TravelPreference', back_populates='itineraries')
    bookings = relationship('Booking', back_populates='itinerary')

class Booking(db.Model):
    """Model for storing user bookings."""
    __tablename__ = 'bookings'

    id = Column(Integer, primary_key=True)
    session_id = Column(String(100), nullable=False)
    itinerary_id = Column(Integer, ForeignKey('itineraries.id'), nullable=False)
    booking_type = Column(String(50), nullable=False)  # flight, hotel, activity
    provider = Column(String(100), nullable=False)
    details = Column(JSON)
    cost = Column(Float, nullable=False)
    booking_reference = Column(String(100), nullable=False)
    status = Column(String(50), default='confirmed')
    booking_date = Column(DateTime, default=datetime.utcnow)

    # Relationship
    itinerary = relationship('Itinerary', back_populates='bookings')