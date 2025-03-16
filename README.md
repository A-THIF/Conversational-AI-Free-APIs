# FreeAIChatAgent

A personal journey of building a conversational AI agent, starting with OpenAI's Assistants API and pivoting to the Hugging Face Inference API to avoid costs. The agent, named Samantha, uses the `facebook/blenderbot-400M-distill` model for free dialogue. This project was a learning experience about APIs, model limitations, and AI integration challenges.

## Features
- Free API usage with Hugging Face Inference API.
- Retry logic to handle 503 Service Unavailable errors.
- Context retention (up to 6 user/assistant turns).
- Adjustable generation parameters (`temperature`, `top_k`) for response variety.

## Installation
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/FreeAIChatAgent.git
   cd FreeAIChatAgent
   ```
2. **Set Up a Virtual Environment**:
   ```bash
   python -m venv venv
   .\venv\Scripts\activate  # On Windows
   source venv/bin/activate  # On macOS/Linux
   ```
3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
4. **Set Up Your API Token**:
   - Sign up at [Hugging Face](https://huggingface.co) and get an API token.
   - Create a `.env` file in the project root:
     ```bash
     echo HUGGINGFACE_API_TOKEN=your_token_here > .env
     ```
   - Replace `your_token_here` with your actual token (do not share it publicly).

## Usage
1. **Run the Agent**:
   ```bash
   python agent.py
   ```
2. **Interact**:
   - The agent will prompt you for input.
   - Type your messages (e.g., "hello", "i am fine").
   - Type `exit` to stop the conversation.

## Example Interaction
```
Welcome to your agent! Type 'exit' to stop.
You: hello
Agent: Hello, how are you today? I am well, thank you.
You: nice
Agent: Hello, nice to meet you. What do you do for a living?
You: plumber
Agent: What do you do for a living? I'm an accountant.
You: exit
```

## Journey
This project was a three-day learning experience:
- **Day 1**: Explored OpenAI's Assistants API but struggled with implementation.
- **Day 2**: Faced cost barriers with OpenAI and integration challenges.
- **Day 3**: Pivoted to Hugging Face's free Inference API, tested `facebook/blenderbot-400M-distill`, and learned about API and model limitations.

## Challenges
- **API Errors**: Encountered 503 errors, mitigated with retry logic.
- **Context Retention**: The model struggled to remember user inputs (e.g., repeating "What do you do for a living?" after being told).
- **Response Quality**: Responses were often repetitive or off-topic despite prompt tweaks.

## Future Improvements
- Test `microsoft/DialoGPT-medium` for potentially better dialogue performance.
- Explore a local setup with `transformers` to avoid API instability (though this requires more storage).
- Improve context retention by experimenting with prompt engineering or larger models.

## Project Structure
- `agent.py`: Main script for the conversational agent.
- `requirements.txt`: Lists necessary dependencies (`requests`, `python-dotenv`).
- `.env.example`: Template for the `.env` file with your API token.
- `.gitignore`: Excludes sensitive files (e.g., `.env`, `venv/`).
- `LICENSE`: MIT License for the project.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments
- Thanks to [Hugging Face](https://huggingface.co) for providing a free Inference API.
- Inspired by the need for cost-free AI solutions and the desire to learn by doing.

