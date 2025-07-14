from app import db
from datetime import datetime
from sqlalchemy import JSON

class TravelPreference(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    session_id = db.Column(db.String(255), nullable=False)
    destination_country = db.Column(db.String(255))
    budget_type = db.Column(db.String(50))  # budget, mid_range, luxury, ultra_luxury
    budget = db.Column(db.Float)  # Daily budget
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    group_size = db.Column(db.Integer)
    interests = db.Column(JSON)  # Store as JSON array
    accommodation_type = db.Column(db.String(100))
    transport_preference = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Itinerary(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    session_id = db.Column(db.String(255), nullable=False)
    preference_id = db.Column(db.Integer, db.ForeignKey('travel_preference.id'), nullable=False)
    destination = db.Column(db.String(255), nullable=False)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    activities = db.Column(JSON)  # Store daily activities as JSON
    budget_breakdown = db.Column(JSON)  # Store budget details as JSON
    recommendations = db.Column(JSON)  # Store AI recommendations as JSON
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    preference = db.relationship('TravelPreference', backref='itineraries')

class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    session_id = db.Column(db.String(255), nullable=False)
    itinerary_id = db.Column(db.Integer, db.ForeignKey('itinerary.id'), nullable=False)
    booking_type = db.Column(db.String(50), nullable=False)  # 'flight', 'hotel', 'activity'
    provider = db.Column(db.String(100))
    details = db.Column(JSON)  # Store booking details as JSON
    cost = db.Column(db.Float)
    booking_reference = db.Column(db.String(100))
    status = db.Column(db.String(50), default='pending')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    itinerary = db.relationship('Itinerary', backref='bookings')
