
from flask import render_template, request, jsonify
from app import app
from gemini import get_travel_response
import logging

@app.route('/')
def index():
    """Homepage with travel assistant interface."""
    return render_template('index.html')

@app.route('/generate_plan', methods=['POST'])
def generate_plan():
    """Generate AI travel plan based on user input."""
    try:
        # Get form data
        destination = request.form.get('destination', '').strip()
        duration = request.form.get('duration', '').strip()
        budget = request.form.get('budget', '').strip()
        interests = request.form.get('interests', '').strip()
        additional_info = request.form.get('additional_info', '').strip()

        if not destination:
            return jsonify({'error': 'Please enter a destination'}), 400

        # Create detailed user prompt
        user_prompt = f"""
        Create a detailed travel plan for:
        Destination: {destination}
        Duration: {duration if duration else 'Not specified'}
        Budget: {budget if budget else 'Not specified'}
        Interests: {interests if interests else 'General tourism'}
        Additional Information: {additional_info if additional_info else 'None'}

        Please provide a comprehensive travel plan including:
        1. Best time to visit and weather information
        2. Daily itinerary suggestions with specific activities
        3. Budget breakdown for accommodation, food, activities, and transport
        4. Must-see attractions and hidden gems
        5. Local cuisine recommendations and where to try them
        6. Transportation options and tips
        7. Cultural insights and travel tips
        8. Packing suggestions
        """

        # Get AI response
        ai_response = get_travel_response(user_prompt)

        return jsonify({
            'success': True,
            'response': ai_response,
            'destination': destination
        })

    except Exception as e:
        logging.error(f"Error generating travel plan: {e}")
        return jsonify({'error': 'Failed to generate travel plan. Please try again.'}), 500

@app.route('/ask_question', methods=['POST'])
def ask_question():
    """Handle general travel questions."""
    try:
        question = request.form.get('question', '').strip()

        if not question:
            return jsonify({'error': 'Please enter a question'}), 400

        # Get AI response with travel context
        travel_question = f"Travel question: {question}\n\nPlease provide detailed, helpful travel advice."
        ai_response = get_travel_response(travel_question)

        return jsonify({
            'success': True,
            'response': ai_response,
            'question': question
        })

    except Exception as e:
        logging.error(f"Error answering question: {e}")
        return jsonify({'error': 'Failed to answer question. Please try again.'}), 500

@app.route('/preferences')
def preferences():
    """Travel preferences page."""
    return render_template('preferences.html')

@app.route('/destinations')
def destinations():
    """Destinations page."""
    return render_template('destinations.html')

@app.route('/itinerary')
def itinerary():
    """Itinerary page."""
    return render_template('itinerary.html')

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors."""
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors."""
    return render_template('500.html'), 500
