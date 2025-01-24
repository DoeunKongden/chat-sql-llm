# SQL Database Chatbot with LangChain and Groq

![LangChain](https://img.shields.io/badge/LangChain-OpenAI-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white)
![Groq](https://img.shields.io/badge/Groq-Llama3-8B8192-green)

A conversational interface to interact with SQL databases using natural language, powered by LangChain and Groq's Llama3 LLM.

## Features

- **Natural Language to SQL**: Convert plain English questions into SQL queries
- **Multi-Database Support**:
  - SQLite (with included sample student database)
  - MySQL (external connections)
- **Groq Integration**: Leverage Llama3-8b-8192 model for high-speed inference
- **Streamlit Web Interface**: User-friendly GUI for database interactions
- **Security**: Read-only mode for SQLite, configurable privileges for MySQL
- **Conversational Memory**: Maintains chat history during session

## Prerequisites

- Python 3.8+
- [Groq API key](https://console.groq.com/)
- SQL database (either SQLite or MySQL)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/sql-chatbot.git
cd sql-chatbot
