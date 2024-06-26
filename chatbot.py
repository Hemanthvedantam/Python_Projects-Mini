# -*- coding: utf-8 -*-
"""ChatBot.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ik_9HRlMQv4uAgAW-oYXMuVuaAryXhUh
"""



import nltk
from nltk.chat.util import Chat, reflections
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today?",]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there",]
    ],
    [
        r"what is your name?",
        ["I am a chatbot created by OpenAI. You can call me Chatbot.",]
    ],
    [
        r"how are you?",
        ["I'm doing good. How about you?",]
    ],
    [
        r"sorry (.*)",
        ["It's okay", "No problem",]
    ],
    [
        r"quit",
        ["Bye, take care. See you soon :) ",]
    ],
]

chatbot = Chat(pairs, reflections)

print("Hi, I'm Chatbot. How can I help you today?")

chatbot.converse()