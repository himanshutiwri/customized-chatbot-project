# chatbot/__init__.py
from .model import ChatbotModel

class Chatbot:
    """Main chatbot class to handle user interactions."""
    
    def __init__(self, api_key):
        self.model = ChatbotModel(api_key)

    def ask(self, question):
        """Ask a question to the chatbot model."""
        return self.model.ask_chatbot(question)
