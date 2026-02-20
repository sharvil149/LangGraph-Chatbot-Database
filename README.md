# LangGraph Multi-Thread AI Chatbot

🌐 **Live Application:**  
https://langgraph-chatbot-database-c4hvjemym5apzcmtlrenzm.streamlit.app

This project implements a stateful conversational AI system using LangGraph with SQLite checkpointing for thread management. It integrates Groq’s LLaMA 3.1 model for inference and is deployed on Streamlit Cloud.

## Key Features

- Multi-thread conversation support
- Streaming LLM responses
- LangGraph state machine architecture
- SQLite-based checkpointing
- Cloud deployment

This project implements a Streamlit-based conversational AI chatbot powered by LangGraph and Groq LLMs.  
It supports persistent conversation storage using a database backend and structured workflow-based message handling.

## Project Overview

The system combines:

- Streamlit frontend for user interaction
- LangGraph for workflow orchestration
- Groq LLM API for fast inference
- SQLite database for conversation persistence
- Thread-based session management

The architecture separates frontend UI logic from backend workflow and storage logic to maintain modularity and scalability.

## Architecture

Frontend Components:
- streamlit_frontend.py
- streamlit_frontend_threading.py
- streamlit_frontend_database.py

Backend Components:
- langgraph_backend.py
- langgraph_database_backend.py

The frontend collects user input and displays responses.  
The backend processes messages using a LangGraph workflow, sends prompts to Groq LLM, and stores conversation history in the database.

## Features

- Interactive chatbot interface built with Streamlit
- Workflow-driven message processing using LangGraph
- Integration with Groq LLM API
- Persistent chat history using SQLite
- Thread-based session handling
- Modular backend design

## Technologies Used

- Python
- Streamlit
- LangGraph
- LangChain
- Groq API
- SQLite
- python-dotenv

## Installation

Clone the repository:

```
git clone https://github.com/sharvil149/LangGraph-Chatbot-Database.git
cd LangGraph-Chatbot-Database
```

Create a virtual environment (recommended):

Windows:
```
python -m venv venv
venv\Scripts\activate
```

Install dependencies:

```
pip install -r requirements.txt
```

## Environment Setup

Create a `.env` file in the project root directory and add your Groq API key:

```
GROQ_API_KEY=your_api_key_here
```

Make sure `.env` is listed in `.gitignore` to avoid exposing secrets.

The application loads the API key using `python-dotenv`.

## Running the Application

Start the Streamlit application:

```
streamlit run streamlit_frontend_database.py
```

The chatbot will open in your browser.

## How It Works

1. User submits a message through the Streamlit interface.
2. The message is passed to the LangGraph workflow.
3. The workflow processes the input and calls the Groq LLM.
4. The response is generated and stored in the SQLite database.
5. Conversation history is retrieved and displayed in the UI.

## Learning Outcomes

This project demonstrates:

- Workflow orchestration using LangGraph
- Integration of Groq LLM API
- Persistent conversation storage
- Separation of frontend and backend logic
- Stateful session management
- Structured AI application development

## Future Improvements

- User authentication
- Cloud deployment
- UI enhancements
- Multi-user database support
- Conversation export functionality
