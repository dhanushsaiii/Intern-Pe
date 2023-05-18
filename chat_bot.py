# -*- coding: utf-8 -*-
"""chat bot.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1sIgfSvGilovilll3e7x7HbIx6BUCj8v3
"""

import random

def get_bot_response(user_input):
    responses = {
        "hi": "Hello there!",
        "hello": "Hi, how are you?",
        "how are you": "I'm doing well, thanks for asking!",
        "what is your name": "My name is ChatBot.",
        "what can you do": "I can answer some basic questions and chat with you.",
        "bye": "Goodbye, have a nice day!"
    }

    if user_input.lower() in responses:
        return responses[user_input.lower()]
    else:
        return "I'm sorry, I didn't understand what you said."

print("ChatBot: Hello, how can I help you?")

while True:
    user_input = input("User: ")
    if user_input.lower() == "bye":
        print("ChatBot:", get_bot_response(user_input))
        break
    else:
        print("ChatBot:", get_bot_response(user_input))