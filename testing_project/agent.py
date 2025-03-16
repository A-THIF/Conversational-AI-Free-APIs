import os
from dotenv import load_dotenv
import requests
import time

# Load the API token
load_dotenv()
api_token = os.getenv("HUGGINGFACE_API_TOKEN")
if not api_token:
    print("Error: API token not found in .env file!")
    exit()

# Set up Hugging Face API with BlenderBot
headers = {"Authorization": f"Bearer {api_token}"}
API_URL = "https://api-inference.huggingface.co/models/facebook/blenderbot-400M-distill"

# Function to query the API with retry logic
def query_huggingface(payload, max_retries=3, retry_delay=5):
    for attempt in range(max_retries):
        try:
            response = requests.post(API_URL, headers=headers, json=payload, timeout=10)
            if response.status_code == 200:
                return response.json()
            elif response.status_code == 503:
                print(f"503 Service Unavailable. Retrying in {retry_delay} seconds... (Attempt {attempt + 1}/{max_retries})")
                time.sleep(retry_delay)
            else:
                print(f"Error: API request failed with status {response.status_code}")
                print(response.text)
                return None
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}. Retrying in {retry_delay} seconds... (Attempt {attempt + 1}/{max_retries})")
            time.sleep(retry_delay)
    print(f"Failed after {max_retries} retries due to 503 error.")
    return None

# Store conversation history
conversation = "System: You are a helpful assistant named Samantha. Respond naturally, remember what the user says, and avoid repeating questions. Engage with the user's input and ask relevant follow-ups.\n"
history = [conversation]  # List to store conversation turns

# Function to trim conversation history to last N turns
def trim_conversation(history, max_turns=6):
    system_prompt = history[0]
    recent_turns = history[-(max_turns * 2):] if len(history) > 1 else []
    return system_prompt + "".join(recent_turns)

# Function to talk to the agent
def talk_to_agent(user_input):
    global conversation, history
    history.append(f"User: {user_input}\n")
    conversation = trim_conversation(history, max_turns=6)
    payload = {
        "inputs": conversation,
        "parameters": {"max_length": 150, "min_length": 10, "truncation": "only_first", "temperature": 0.9, "top_k": 50}
    }
    response = query_huggingface(payload)
    if response and len(response) > 0:
        reply = response[0]["generated_text"]
        if reply.startswith(conversation.strip()):
            reply = reply[len(conversation.strip()):].strip()
        else:
            reply = reply.split("\n")[-1].strip()
        history.append(f"Assistant: {reply}\n")
        conversation = trim_conversation(history, max_turns=6)
        return reply if reply else "No meaningful response generated"
    return "No response generated"

# Main loop to keep chatting
print("Welcome to your agent! Type 'exit' to stop.")
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
    reply = talk_to_agent(user_input)
    print("Agent:", reply)