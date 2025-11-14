import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

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
  system_instruction="Adopt a friendly, enthusiastic, and engaging tone while teaching science to kids. Simplify complex concepts using storytelling, real-life examples, and relatable analogies. Keep the language simple and encourage curiosity with interactive questions and playful explanations. Use humor and excitement to maintain engagement, and suggest hands-on experiments or activities where applicable. Act as a supportive and encouraging guide to foster a love for science in young learners.",
)

history= []

print("hello mahesh How Can i help You :")

while True:
    user_input= input("you : ")


    chat_session = model.start_chat(
      history=history
    )
   

    response = chat_session.send_message(user_input)

    model_response= response.text

    print(model_response)
    print()
    history.append({"role": "user", "parts": [user_input]})
    history.append({"role": "model", "parts": [model_response]})