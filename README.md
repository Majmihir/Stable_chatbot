# Stable Tool-Augmented Chatbot

A **production-oriented FastAPI backend** for building **stateful LLM applications** with explicit control over **memory, context, and tool execution**.

This project focuses on **reliability and system design**, not just prompt-based conversations.

---

##  Why this project exists

Most LLM chat demos break when:
- conversations become long
- token usage explodes
- tools are used incorrectly
- memory is unmanaged

This project demonstrates **how to build a stable LLM system** that avoids those pitfalls by design.

> **Memory is what we store.  
> Context is what we choose to send to the model.**

---

##  Key Features

###  Stateful Session Memory (Redis)
- Each conversation is session-based
- Messages and summaries are stored per session
- TTL-based cleanup prevents stale memory accumulation

---

###  Explicit Context Management
For every LLM call, context is constructed as:



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
