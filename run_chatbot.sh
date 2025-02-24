#!/bin/bash

# Prompt user for Groq API key
read -p "Enter your Groq API Key: " GROQ_API_KEY

# Save API key to .env file
echo "GROQ_API_KEY=$GROQ_API_KEY" > .env
echo "✅ .env file created successfully."

# Build the Docker image
echo "🚀 Building Docker image..."
docker build -t rag-chatbot .

# Check if port 8501 is in use
if lsof -i :8501 >/dev/null 2>&1; then
    echo "⚠️ Port 8501 is already in use. Please free the port and try again."
    exit 1
fi

# Run the container with .env file
echo "🔥 Running the chatbot..."
docker run -p 8501:8501 --env-file .env rag-chatbot