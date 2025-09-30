import os
from flask import Flask, render_template, request, redirect, url_for, jsonify, session
from logger import CustomLogger  # Import custom logger class
from chatbot import Chatbot

def create_app():
    """Create and configure the Flask application."""
    app = Flask(__name__)
    app.secret_key = os.urandom(24)  # Set a secret key for session management
    logger = CustomLogger().get_logger()  # Initialize custom logger

    @app.route('/', methods=['GET', 'POST'])
    def index():
        """Render the API key input page and handle form submissions."""
        error_message = None  # Variable to hold any error messages

        if request.method == 'POST':
            api_key = request.form['api_key']
            
            try:
                session['groq_api_key'] = api_key  # Store API key in session
                
                chatbot_instance = Chatbot(api_key)  # Initialize chatbot with API key
                
                logger.info("API Key set successfully.")
                return redirect(url_for('chat'))  # Redirect to chat page
            
            except Exception as e:
                logger.error(f"Error setting API Key: {e}")
                error_message = "Error setting API Key. Please try again."
        
        return render_template('index.html', error_message=error_message)

    @app.route('/chat')
    def chat():
        """Render the chat interface."""
        if 'groq_api_key' not in session:
            return redirect(url_for('index'))  # Redirect if no API key is set

        return render_template('chat.html')

    @app.route('/ask', methods=['POST'])
    def ask():
        """Handle user questions and return responses."""
        question = request.json.get('question')
        
        try:
            api_key = session.get('groq_api_key')
            if not api_key:
                return jsonify({"response": "API Key is not set."}), 500
            
            chatbot_instance = Chatbot(api_key)  # Create a new instance for each request
            
            response = chatbot_instance.ask(question)
            logger.info(f"User asked: {question}")
            return jsonify({"response": response})
        
        except Exception as e:
            logger.error(f"Error processing question '{question}': {e}")
            return jsonify({"response": "An error occurred while processing your request."}), 500

    @app.route('/logout', methods=['POST'])
    def logout():
        """Clear the GROQ API key and reset chatbot instance."""
        session.pop('groq_api_key', None)  # Clear the API key from session
        session.pop('chatbot_instance', None)  # Clear the chatbot instance from session
        
        logger.info("API Key and Chatbot instance cleared.")
        
        return redirect(url_for('index'))  # Redirect back to index page
    
    return app  # Return the configured app instance
