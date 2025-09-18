# Streamlit Ollama Gemma3:4b Chatbot

A Streamlit-based chatbot that uses Ollama's `gemma3:4b` model for local AI chat, with optional image upload to request a short description.

## Features

- 🤖 Chat with local AI models via Ollama
- 🖼️ Upload an image and request a super short description
- 🎨 Clean and intuitive Streamlit UI
- 🔧 Configurable temperature settings
- 💾 Persistent chat history during session
- 🎯 Optional system prompts for customized behavior
- 📊 Real-time model availability checking

## Prerequisites

1. **Install Ollama**: Download and install from [ollama.ai](https://ollama.ai)
2. **Pull model**: 
    - `ollama pull gemma3:4b`
3. **Start Ollama**: Make sure the Ollama service is running

## Installation

1. Clone this repository:
```bash
git clone <repository-url>
cd streamlit-ollama-chatbot
```

2. Install Python dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Start the Streamlit app:
```bash
streamlit run chatbot.py
```

2. Open your browser to `http://localhost:8501`

3. For chat: Type your message and press Enter
4. For a short image description: Upload an image and click "🔍 Analyze Image"

## Available Models

This chatbot uses a single model:
- `gemma3:4b`

## Configuration

- **Temperature**: Controls response randomness (0.0 = focused, 2.0 = creative)
- **System Prompt**: Set custom instructions for the AI
- **Image Upload**: Supports PNG, JPG, JPEG, GIF, BMP formats

## Troubleshooting

- **"Model not found"**: Install the model with `ollama pull <model-name>`
- **"Ollama client not available"**: Make sure Ollama is installed and running
- **Connection errors**: Check that Ollama is running on localhost:11434
- **Image analysis not working**: Some models may have limited vision capabilities. If image inputs fail, try plain text prompts.

## Project Structure

```
streamlit-ollama-chatbot/
├── chatbot.py          # Main Streamlit application
├── requirements.txt    # Python dependencies
├── README.md          # This file
└── docs/              # Documentation
    ├── ollama-python.md
    ├── requirements.md
    └── streamlit-docs.md
```
