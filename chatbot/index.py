import re
import time
from fuzzywuzzy import process

responses = {
    "hello": "Hello!",
    "how are you": "I'm just a bunch of code, but thanks for asking! How about you?",
    "bye": "Bye, have a great time!",
    "status": "I'm a teapot",
    "your name": "I'm a simple chatbot, built by you! How about you give a name to me?",
    "hobbies": "I enjoy helping people to automate simple stuff in Python, like creating bots like me! :]",
    "help": "I'm here to chat with you. Try asking me about my hobbies, my status, or say hello!",
    "default": "I'm not sure how to respond to that. Could you ask me something else?",
}

# Fuzzywuzzy para deteção de 'familiaridade'
def get_response(user_input):
    best_match, score = process.extractOne(user_input, responses.keys())
    if score > 70:
        return responses[best_match]
    return responses["default"]

def chatbot():
    print("Welcome to the chatbot! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        
        if re.search("bye", user_input, re.IGNORECASE):
            print("Chatbot:", responses["bye"])
            break
        
        response = get_response(user_input)
        time.sleep(0.5)
        
        print("Chatbot:", response)

chatbot()

