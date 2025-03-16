# FreeAIChatAgent

A personal journey of building a conversational AI agent, starting with OpenAI's Assistants API and pivoting to the Hugging Face Inference API to avoid costs. The agent, named Samantha, uses the `facebook/blenderbot-400M-distill` model for free dialogue.

## Features
- Free API usage with Hugging Face Inference API.
- Retry logic to handle 503 errors.
- Context retention (up to 6 turns).
- Adjustable generation parameters for response variety.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/FreeAIChatAgent.git
   cd FreeAIChatAgent