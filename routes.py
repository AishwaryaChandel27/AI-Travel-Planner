from flask import render_template, request, session, redirect, url_for, flash, jsonify
from datetime import datetime
import uuid
import logging

from app import app, db
from models import TravelPreference, Itinerary, Booking
from gemini import get_destination_recommendations, generate_itinerary, get_travel_tips
from travel_service import TravelService
from country_data import get_country_info, get_popular_destinations, get_budget_ranges

travel_service = TravelService()

@app.route('/')
def index():
    """Homepage with travel planner introduction."""
    return render_template('index.html')

@app.route('/preferences', methods=['GET', 'POST'])
def preferences():
    """Handle travel preferences input."""
    if request.method == 'POST':
        # Generate session ID if not exists
        if 'session_id' not in session:
            session['session_id'] = str(uuid.uuid4())
        
        # Parse form data
        try:
            start_date = datetime.strptime(request.form['start_date'], '%Y-%m-%d').date()
            end_date = datetime.strptime(request.form['end_date'], '%Y-%m-%d').date()
            
            if start_date >= end_date:
                flash('End date must be after start date', 'error')
                return render_template('preferences.html')
            
            # Get interests from form
            interests = request.form.getlist('interests')
            if not interests:
                flash('Please select at least one interest', 'error')
                return render_template('preferences.html')
            
            # Create travel preference record
            preference = TravelPreference(
                session_id=session['session_id'],
                destination_country=request.form.get('destination_country'),
                budget_type=request.form.get('budget_type'),
                budget=float(request.form['budget']),
                start_date=start_date,
                end_date=end_date,
                group_size=int(request.form['group_size']),
                interests=interests,
                accommodation_type=request.form['accommodation_type'],
                transport_preference=request.form['transport_preference']
            )
            
            db.session.add(preference)
            db.session.commit()
            
            session['preference_id'] = preference.id
            session['destination_country'] = preference.destination_country
            session['budget_type'] = preference.budget_type
            
            # Get country info and popular destinations
            country_info = get_country_info(preference.destination_country)
            popular_destinations = get_popular_destinations(preference.destination_country)
            
            # Get AI recommendations
            preferences_dict = {
                'destination_country': preference.destination_country,
                'budget_type': preference.budget_type,
                'budget': preference.budget,
                'start_date': preference.start_date,
                'end_date': preference.end_date,
                'group_size': preference.group_size,
                'interests': preference.interests,
                'accommodation_type': preference.accommodation_type,
                'transport_preference': preference.transport_preference,
                'country_info': country_info,
                'popular_destinations': popular_destinations
            }
            
            recommendations = get_destination_recommendations(preferences_dict)
            session['recommendations'] = [rec.dict() for rec in recommendations]
            
            return redirect(url_for('destinations'))
            
        except ValueError as e:
            flash(f'Invalid input: {str(e)}', 'error')
            return render_template('preferences.html')
        except Exception as e:
            logging.error(f"Error processing preferences: {e}")
            flash('An error occurred while processing your preferences. Please try again.', 'error')
            return render_template('preferences.html')
    
    return render_template('preferences.html')

@app.route('/destinations')
def destinations():
    """Display AI-recommended destinations."""
    if 'recommendations' not in session:
        flash('Please fill in your preferences first', 'error')
        return redirect(url_for('preferences'))
    
    recommendations = session['recommendations']
    return render_template('destinations.html', recommendations=recommendations)

@app.route('/select_destination/<int:destination_index>')
def select_destination(destination_index):
    """Select a destination and generate itinerary."""
    if 'recommendations' not in session or 'preference_id' not in session:
        flash('Please start over with your preferences', 'error')
        return redirect(url_for('preferences'))
    
    try:
        recommendations = session['recommendations']
        if destination_index >= len(recommendations):
            flash('Invalid destination selection', 'error')
            return redirect(url_for('destinations'))
        
        selected_destination = recommendations[destination_index]
        
        # Get preference from database
        preference = TravelPreference.query.get(session['preference_id'])
        if not preference:
            flash('Preference not found', 'error')
            return redirect(url_for('preferences'))
        
        # Generate detailed itinerary
        country_info = get_country_info(preference.destination_country)
        preferences_dict = {
            'destination_country': preference.destination_country,
            'budget_type': preference.budget_type,
            'budget': preference.budget,
            'start_date': preference.start_date,
            'end_date': preference.end_date,
            'group_size': preference.group_size,
            'interests': preference.interests,
            'accommodation_type': preference.accommodation_type,
            'transport_preference': preference.transport_preference,
            'country_info': country_info
        }
        
        itinerary_plan = generate_itinerary(preferences_dict, selected_destination['destination'])
        travel_tips = get_travel_tips(selected_destination['destination'], preferences_dict)
        
        # Create itinerary record
        itinerary = Itinerary(
            session_id=session['session_id'],
            preference_id=preference.id,
            destination=selected_destination['destination'],
            title=f"{selected_destination['destination']} Adventure",
            description=f"Personalized {itinerary_plan.duration_days}-day itinerary for {selected_destination['destination']}",
            activities=itinerary_plan.daily_activities,
            budget_breakdown=itinerary_plan.budget_breakdown,
            recommendations={
                'restaurants': itinerary_plan.recommended_restaurants,
                'accommodations': itinerary_plan.accommodation_suggestions,
                'travel_tips': travel_tips
            }
        )
        
        db.session.add(itinerary)
        db.session.commit()
        
        session['itinerary_id'] = itinerary.id
        
        return redirect(url_for('itinerary'))
        
    except Exception as e:
        logging.error(f"Error selecting destination: {e}")
        flash('An error occurred while generating your itinerary. Please try again.', 'error')
        return redirect(url_for('destinations'))

@app.route('/itinerary')
def itinerary():
    """Display generated itinerary."""
    if 'itinerary_id' not in session:
        flash('No itinerary found. Please start over.', 'error')
        return redirect(url_for('preferences'))
    
    itinerary = Itinerary.query.get(session['itinerary_id'])
    if not itinerary:
        flash('Itinerary not found', 'error')
        return redirect(url_for('preferences'))
    
    # Get weather information
    weather_info = travel_service.get_weather_info(itinerary.destination)
    
    # Get available activities
    activities = travel_service.get_activities(itinerary.destination, itinerary.preference.interests)
    
    return render_template('itinerary.html', 
                         itinerary=itinerary, 
                         weather_info=weather_info,
                         activities=activities)

@app.route('/book/<booking_type>')
def book(booking_type):
    """Display booking options (flights, hotels, activities)."""
    if 'itinerary_id' not in session:
        flash('No itinerary found. Please start over.', 'error')
        return redirect(url_for('preferences'))
    
    itinerary = Itinerary.query.get(session['itinerary_id'])
    if not itinerary:
        flash('Itinerary not found', 'error')
        return redirect(url_for('preferences'))
    
    if booking_type == 'flights':
        # Mock flight search
        flights = travel_service.search_flights(
            origin="Home City",
            destination=itinerary.destination,
            departure_date=itinerary.preference.start_date.isoformat(),
            return_date=itinerary.preference.end_date.isoformat(),
            passengers=itinerary.preference.group_size
        )
        return render_template('booking.html', 
                             booking_type='flights', 
                             items=flights, 
                             itinerary=itinerary)
    
    elif booking_type == 'hotels':
        # Mock hotel search
        hotels = travel_service.search_hotels(
            destination=itinerary.destination,
            check_in=itinerary.preference.start_date.isoformat(),
            check_out=itinerary.preference.end_date.isoformat(),
            guests=itinerary.preference.group_size
        )
        return render_template('booking.html', 
                             booking_type='hotels', 
                             items=hotels, 
                             itinerary=itinerary)
    
    elif booking_type == 'activities':
        # Get activities
        activities = travel_service.get_activities(itinerary.destination, itinerary.preference.interests)
        return render_template('booking.html', 
                             booking_type='activities', 
                             items=activities, 
                             itinerary=itinerary)
    
    else:
        flash('Invalid booking type', 'error')
        return redirect(url_for('itinerary'))

@app.route('/confirm_booking', methods=['POST'])
def confirm_booking():
    """Confirm a booking."""
    if 'itinerary_id' not in session:
        flash('No itinerary found. Please start over.', 'error')
        return redirect(url_for('preferences'))
    
    try:
        booking_type = request.form['booking_type']
        item_id = request.form['item_id']
        item_details = request.form.get('item_details', '{}')
        
        # Parse item details
        import json
        details = json.loads(item_details)
        
        # Create booking using travel service
        booking_info = travel_service.create_booking(booking_type, item_id, details)
        
        # Save booking to database
        booking = Booking(
            session_id=session['session_id'],
            itinerary_id=session['itinerary_id'],
            booking_type=booking_type,
            provider=details.get('provider', 'Unknown'),
            details=booking_info,
            cost=booking_info['total_amount'],
            booking_reference=booking_info['booking_reference'],
            status='confirmed'
        )
        
        db.session.add(booking)
        db.session.commit()
        
        flash(f'Booking confirmed! Reference: {booking_info["booking_reference"]}', 'success')
        return redirect(url_for('itinerary'))
        
    except Exception as e:
        logging.error(f"Error confirming booking: {e}")
        flash('An error occurred while confirming your booking. Please try again.', 'error')
        return redirect(url_for('itinerary'))

@app.route('/my_bookings')
def my_bookings():
    """Display user's bookings."""
    if 'session_id' not in session:
        flash('No bookings found', 'error')
        return redirect(url_for('index'))
    
    bookings = Booking.query.filter_by(session_id=session['session_id']).all()
    return render_template('my_bookings.html', bookings=bookings)

@app.route('/reset')
def reset():
    """Reset session and start over."""
    session.clear()
    flash('Session reset. You can start planning a new trip!', 'info')
    return redirect(url_for('index'))

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'), 500
