# Stable Tool-Augmented Chatbot

A robust FastAPI-based chatbot application designed with tool augmentation capabilities, conversation summarization, and persistent memory using Redis.

## Features

- **OpenAI Integration**: Powered by OpenAI's GPT models for intelligent conversational abilities.
- **Tool Augmentation**: Capable of using external tools to enhance response generation (found in `tools/` and `services/tool_service.py`).
- **Session Management**: Uses Redis for handling session data and conversation history.
- **Summarization**: Built-in service for summarizing conversations.
- **FastAPI Framework**: High-performance, easy-to-use API framework.

## Project Structure

```
Stable_chatbot/
├── core/           # Core configurations
├── memory/         # Session and memory management
├── models/         # Pydantic models
├── routes/         # API routes (chat, etc.)
├── services/       # Business logic (chat, summarization, tools)
├── tools/          # External tool definitions
├── main.py         # Application entry point
├── requirements.txt # Project dependencies
└── .env            # Environment variables
```

## Prerequisites

- Python 3.8+
- Redis Server (ensure Redis is running locally or provide a connection URL)
- OpenAI API Key (or Azure OpenAI Service Credentials)

## Installation

1. **Clone the repository**

   ```bash
   git clone <repository-url>
   cd Stable_chatbot
   ```

2. **Create a virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Configuration**
   Create a `.env` file in the root directory based on your needs. Use the provided `.env.example` as a template:
   ```bash
   AZURE_OPENAI_API_KEY=your_azure_openai_api_key
   AZURE_OPENAI_ENDPOINT=https://your-resource-name.openai.azure.com/
   AZURE_OPENAI_DEPLOYMENT_NAME=your_deployment_name
   AZURE_OPENAI_API_VERSION=2023-05-15
   REDIS_URL=redis://localhost:6379  # or your Redis URL
   ```

## Usage

Start the application using Uvicorn:

```bash
uvicorn main:app --reload
```

The API will be available at `http://127.0.0.1:8000`.

### API Documentation

Once the server is running, you can access the interactive API documentation at:

- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`
