print("Welcome to Simple Chatbot!")
print("Type 'bye' to end the chat.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "hello":
        print("Bot: Hi there!")
    elif user_input.lower() == "how are you":
        print("Bot: I'm good, thank you!")
    elif user_input.lower() == "what is your name":
        print("Bot: I'm a simple chatbot.")
    elif user_input.lower() == "bye":
        print("Bot: Goodbye!")
        break
    else:
        print("Bot: I don't understand.")
