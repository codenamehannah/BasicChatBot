def get_response(user_input):
    user_input = user_input.lower()

    if "hello" or "hey" or "hi" in user_input:
        return "Hi there!"
    elif "how are you" in user_input:
        return "I'm a chatbot. I'm here to help you!"
    elif "bye" in user_input:
        return "Goodbye! Have a great day."
    else:
        return "I'm sorry, I don't understand that."

def chat():
    print("Chatbot: Hi! I'm a Hannah, a First Grade ChatBot. You can start talking to me but please understand that I am only in First Grade. Type 'bye' to exit.")

    while True:
        user_input = input("You: ")

        if user_input.lower() == 'bye':
            print("Chatbot:", get_response(user_input))
            break

        print("Chatbot:", get_response(user_input))

if __name__ == "__main__":
    chat()
