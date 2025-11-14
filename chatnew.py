import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables from .env file
load_dotenv()

# Get the API key from the environment
api_key = os.getenv("GEMINI_API_KEY")

if api_key is None:
    print("API key not found! Make sure you have the .env file with GEMINI_API_KEY.")
    exit()

# Configure the API key
genai.configure(api_key=api_key)

# Create the model
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-2.0-flash-exp",
    generation_config=generation_config,
    system_instruction=(
        "Adopt a friendly, enthusiastic, and engaging tone while teaching science to kids. "
        "Simplify complex concepts using storytelling, real-life examples, and relatable analogies. "
        "Keep the language simple and encourage curiosity with interactive questions and playful explanations. "
        "Use humor and excitement to maintain engagement, and suggest hands-on experiments or activities where applicable. "
        "Act as a supportive and encouraging guide to foster a love for science in young learners."
    ),
)

# Initialize chat history
history = []

# Start Chat Session (Move outside loop)
chat_session = model.start_chat(history=history)

print("Hello Mahesh! How can I help you?")

while True:
    user_input = input("You: ")  # Get user input

    if user_input.lower() in ["exit", "quit"]:  # Exit condition
        print("Goodbye! Have a great day!")
        break

    response = chat_session.send_message(user_input)  # Send message to AI
    model_response = response.text  # Get AI's response

    print("AI:", model_response)  # Print AI response
    print()

    # Append conversation to history
    history.append({"role": "user", "parts": [user_input]})
    history.append({"role": "model", "parts": [model_response]})
