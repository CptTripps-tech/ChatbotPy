from chatterbot import ChatBot
from chatterbot.trainers import *
import backend.logging_handler as logging_handler

chatbot = ChatBot('ServiceBot',
                  storage_adapter='chatterbot.storage.SQLStorageAdapter',
                  database_uri='sqlite:///backend/database/training_db.sqlite3'
                  )


def create_log(response):
    logging_handler.log(response.in_response_to, response.text, response.created_at)


def train_bot():
    # Create a new trainer for the chatbot
    trainer = ChatterBotCorpusTrainer(chatbot)

    # Train the chatbot based on the custom corpus
    trainer.train('backend/training_data')


def get_response(text):
    response = chatbot.get_response(text)
    create_log(response)
    return response.text

