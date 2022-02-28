import os
import sqlite3


def create_connection():
    path = os.path.dirname(os.path.realpath('backend/database/ChatbotDB.db'))
    return sqlite3.connect(os.path.join(path, "ChatbotDB.db"))


create_table = """
        CREATE TABLE IF NOT EXISTS database (
        Request TEXT(20), 
        Response TEXT(30), 
        Created at DATE
        );"""

insert_into_log_table = """
        INSERT INTO database values(
        ?, 
        ?, 
        ?
        );"""


def create_log_db():
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute(create_table)
    connection.commit()


def log(in_response_to, answer, created_at):
    connection = create_connection()
    cursor = connection.cursor()
    create_log_db()
    cursor.execute(insert_into_log_table, (in_response_to, answer, created_at))
    connection.commit()
