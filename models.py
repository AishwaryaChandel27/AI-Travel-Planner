from datetime import datetime
from sqlalchemy import Column, Integer, String, Text, Float, DateTime, ForeignKey, Date
from sqlalchemy.orm import relationship
import json
from app import db

class TravelPreference(db.Model):
    __tablename__ = 'travel_preferences'

    id = Column(Integer, primary_key=True)
    session_id = Column(String(50), nullable=False)
    destination_country = Column(String(100), nullable=False)
    budget_type = Column(String(20), nullable=False)
    budget = Column(Float, nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    group_size = Column(Integer, nullable=False)
    accommodation_type = Column(String(50), nullable=False)
    transport_preference = Column(String(50), nullable=False)
    interests = Column(Text)  # JSON string
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationships
    itineraries = relationship("Itinerary", back_populates="preference")

    @property
    def interests_list(self):
        """Get interests as a list"""
        if self.interests:
            try:
                return json.loads(self.interests)
            except:
                return []
        return []

    @interests_list.setter
    def interests_list(self, value):
        """Set interests from a list"""
        self.interests = json.dumps(value) if value else None

class Itinerary(db.Model):
    __tablename__ = 'itineraries'

    id = Column(Integer, primary_key=True)
    session_id = Column(String(50), nullable=False)
    preference_id = Column(Integer, ForeignKey('travel_preferences.id'), nullable=False)
    destination = Column(String(100), nullable=False)
    title = Column(String(200), nullable=False)
    description = Column(Text)
    activities = Column(Text)  # JSON string
    budget_breakdown = Column(Text)  # JSON string
    recommendations = Column(Text)  # JSON string
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationships
    preference = relationship("TravelPreference", back_populates="itineraries")
    bookings = relationship("Booking", back_populates="itinerary")

    @property
    def activities_list(self):
        """Get activities as a list"""
        if self.activities:
            try:
                return json.loads(self.activities)
            except:
                return []
        return []

    @property
    def budget_breakdown_dict(self):
        """Get budget breakdown as a dict"""
        if self.budget_breakdown:
            try:
                return json.loads(self.budget_breakdown)
            except:
                return {}
        return {}

    @property
    def recommendations_dict(self):
        """Get recommendations as a dict"""
        if self.recommendations:
            try:
                return json.loads(self.recommendations)
            except:
                return {}
        return {}

class Booking(db.Model):
    __tablename__ = 'bookings'

    id = Column(Integer, primary_key=True)
    session_id = Column(String(50), nullable=False)
    itinerary_id = Column(Integer, ForeignKey('itineraries.id'), nullable=False)
    booking_type = Column(String(20), nullable=False)  # flight, hotel, activity
    provider = Column(String(100), nullable=False)
    details = Column(Text)  # JSON string
    cost = Column(Float, nullable=False)
    booking_reference = Column(String(100), nullable=False)
    status = Column(String(20), default='confirmed')
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationships
    itinerary = relationship("Itinerary", back_populates="bookings")

    @property
    def details_dict(self):
        """Get details as a dict"""
        if self.details:
            try:
                return json.loads(self.details)
            except:
                return {}
        return {}