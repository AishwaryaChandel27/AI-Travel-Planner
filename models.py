
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
    interests = Column(JSON, nullable=False)
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
    activities = Column(JSON)
    budget_breakdown = Column(JSON)
    recommendations = Column(JSON)
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
