# chatbot/model.py
from groq import Groq
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.memory import ConversationBufferMemory
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from chatbot.prompt import CUSTOM_PROMPT

class ChatbotModel:
    """Chatbot model class to manage the LLM and interactions."""

    def __init__(self, api_key):
        self.llm = self.initialize_llm(api_key)
        self.memory = ConversationBufferMemory(input_key="question", memory_key="history")
        self.prompt = PromptTemplate(template=CUSTOM_PROMPT, input_variables=['history', 'question'])
        self.chain = self.create_chain()

    def initialize_llm(self, api_key):
        """Initialize the ChatGroq model with the provided API key."""
        return ChatGroq(
            api_key=api_key,
            model="llama-3.3-70b-versatile",
            temperature=0,
            max_tokens=None,
            timeout=None,
            max_retries=2,
        )
    def create_chain(self):
        """Create the LLM chain with memory."""
        return LLMChain(
            llm=self.llm,
            prompt=self.prompt,
            memory=self.memory,
        )

    def ask_chatbot(self, question):
        """Handle user questions and return responses."""
        
        response = self.chain.run({"history": self.memory, "context":"", "question": question})
        
        return response