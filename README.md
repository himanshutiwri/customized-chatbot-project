## Overview

This project is a customized chatbot . It provides real-time, interactive support, making it easier for us to understand challenging concepts and apply them in practical scenarios. Using advanced language models, the chatbot offers personalized guidance and explanations, creating an engaging learning experience that helps simplify complex topics.

## Features

- **Real-Time Knowledge Access**: Instant answers to questions related to Data Science and AI.
- **Personalized Assistance**: Tailored responses based on the user's level of understanding.
- **Practical Application Guidance**: Coding examples and implementation advice for various algorithms and models.
- **Engaging Interaction**: A conversational interface that allows users to explore topics in depth.
- **Memory Management**: Retains context from previous interactions for coherent conversations.

## Requirements

Before running the chatbot, ensure you have the following installed:

- Python 3.10 or higher
- Conda (Anaconda or Miniconda)

## Installation Instructions

Follow these steps to set up the chatbot:

1. **Create a Conda Environment**:
   Open your terminal or command prompt and run the following command to create a new Conda environment:
   ```bash
   conda create -p ./chatbotenv python=3.10 -y
   ```

2. **Activate the Conda Environment**:
    Activate the newly created environment with the following command:
    ```bash
    conda activate ./chatbotenv
    ```

3. **Install Required Packages**:
    Install the necessary dependencies by running:
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the Chatbot**:
    Start the chatbot application by executing:
    ```bash
    python main.py
    ```

## Usage

Once the chatbot is running, you can interact with it through the command line. You will be prompted to enter your Groq API key and questions related to Data Science and AI. The chatbot will provide responses based on its training and memory of previous interactions.