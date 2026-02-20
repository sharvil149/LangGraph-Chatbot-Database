# LangGraph Chatbot with Database Integration

This project implements a Streamlit-based conversational AI chatbot powered by LangGraph.  
It supports persistent conversation storage using a database backend and manages chat sessions using structured workflow logic.

## Project Overview

The system combines:

- Streamlit frontend for user interaction
- LangGraph workflow for structured message handling
- Database backend for conversation persistence
- Thread-based session management

The architecture separates frontend UI logic from backend workflow and storage logic to maintain modularity.

## Architecture

Frontend Components:
- streamlit_frontend.py
- streamlit_frontend_threading.py
- streamlit_frontend_database.py

Backend Components:
- langgraph_backend.py
- langgraph_database_backend.py

The frontend collects user input and displays responses.  
The backend processes messages using a LangGraph workflow and stores conversation history in a database.

## Features

- Interactive chatbot interface
- Workflow-driven message processing
- Persistent chat history using SQLite
- Thread-based session handling
- Modular backend structure

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

## Running the Application

Start the Streamlit application:

```
streamlit run streamlit_frontend_database.py
```

The chatbot will open in your browser.

## Learning Outcomes

This project demonstrates:

- Workflow orchestration using LangGraph
- Separation of frontend and backend logic
- Persistent conversation storage
- Session state management
- Structured AI application development

## Future Improvements

- User authentication system
- Cloud deployment
- UI enhancements
- Multi-user support
