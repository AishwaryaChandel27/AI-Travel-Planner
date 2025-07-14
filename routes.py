
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
            return jsonify({'error': 'Destination is required'}), 400

        # Create user prompt
        user_prompt = f"""
        Create a detailed travel plan for:
        Destination: {destination}
        Duration: {duration if duration else 'Not specified'}
        Budget: {budget if budget else 'Not specified'}
        Interests: {interests if interests else 'General tourism'}
        Additional Information: {additional_info if additional_info else 'None'}

        Please provide a comprehensive travel plan including:
        1. Best time to visit
        2. Daily itinerary suggestions
        3. Budget breakdown
        4. Must-see attractions
        5. Local cuisine recommendations
        6. Travel tips
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
            return jsonify({'error': 'Question is required'}), 400

        # Get AI response
        ai_response = get_travel_response(f"Travel question: {question}")

        return jsonify({
            'success': True,
            'response': ai_response
        })

    except Exception as e:
        logging.error(f"Error answering question: {e}")
        return jsonify({'error': 'Failed to answer question. Please try again.'}), 500

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500
