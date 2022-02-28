from chatterbot import ChatBot
from chatterbot.trainers import *
import backend.database_handler as database_handler
import datetime

chatbot = ChatBot('ServiceBot',
                  storage_adapter='chatterbot.storage.SQLStorageAdapter',
                  database_uri='sqlite:///backend/database/training_db.sqlite3'
                  )


def create_log(in_response_to, text):
    database_handler.log(in_response_to, text, datetime.datetime.now())


def train_bot():
    # Create a new trainer for the chatbot
    trainer = ChatterBotCorpusTrainer(chatbot)

    # Train the chatbot based on the custom corpus
    trainer.train('backend/training_data')


def get_error_label(errorcode):
    label = database_handler.get_code_label(errorcode)
    response = 'Error message means: ' + label
    return response


def get_jira_status(ticketnumber):
    status = database_handler.get_jira_status(ticketnumber)
    response = 'Ticket status is: ' + status
    return response


def get_response(text):
    if 'error code is' in text:
        code = text.strip('error code is')
        response = get_error_label(code)
        create_log(text, response)
        return response
    if 'ticket number is ' in text:
        ticketnumber = text.strip('ticket number is')
        response = get_jira_status(ticketnumber)
        create_log(text, response)
        return response
    else:
        response = chatbot.get_response(text)
        create_log(response.in_response_to, response.text)
        return response.text
