from chatterbot import ChatBot
from chatterbot.trainers import *

chatbot = ChatBot('ServiceBot')

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot based on the custom corpus
trainer.train('training')

# Get a response to an input statement
response = chatbot.get_response('Here is my ticket number')

print("Bot Response:", response)
