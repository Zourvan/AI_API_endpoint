# AI API 🤖

A FastAPI-based API for AI chat interactions.

## Installation 🛠️

This project uses `uv` for dependency management.

```bash
# Install dependencies
uv pip install -r requirements.txt
```

## Running the Application 🚀

Start the application with:

```bash
uv run uvicorn main:app --host 0.0.0.0 --port 8010 --reload
```

## API Usage 📡

### Free Mode

```bash
curl -X POST "http://127.0.0.1:8000/chat" \
     -H "Content-Type: application/json" \
     -d '{"prompt": "Why is the sky blue?"}'
```

### Authenticated Mode (JWT)

```bash
curl -X POST "http://127.0.0.1:8000/chat" \
     -H "Content-Type: application/json" \
     -H "Authorization: Bearer YOUR_JWT_TOKEN" \
     -d '{"prompt": "Why is the sky blue?"}'
```

## Features ✨

- AI chat capabilities
- JWT authentication
- Free and premium access modes
