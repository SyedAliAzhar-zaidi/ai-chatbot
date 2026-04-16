print("AI Chatbot is running... Type 'exit' to stop.\n")

def get_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you today?"

    elif "how are you" in user_input:
        return "I'm doing great! Thanks for asking."

    elif "your name" in user_input:
        return "I'm a simple AI chatbot built in Python."

    elif "help" in user_input:
        return "You can ask me simple questions like greetings or my name."

    elif "bye" in user_input:
        return "Goodbye! Have a great day."

    else:
        return "Sorry, I don't understand that yet."

while True:
    user = input("You: ")

    if user.lower() == "exit":
        print("Chatbot: Goodbye!")
        break

    response = get_response(user)
    print("Chatbot:", response)