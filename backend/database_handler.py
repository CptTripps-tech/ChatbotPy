import os
import sqlite3


def create_connection():
    path = os.path.dirname(os.path.realpath('backend/database/ChatbotDB.db'))
    return sqlite3.connect(os.path.join(path, "ChatbotDB.db"))


create_logs_table = """
        CREATE TABLE IF NOT EXISTS logs (
        Request TEXT(20), 
        Response TEXT(30), 
        Created at DATE
        );"""

insert_into_log_table = """
        INSERT INTO logs values(
        ?, 
        ?, 
        ?
        );"""


def create_log_db():
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute(create_logs_table)
    connection.commit()


def get_jira_status(number):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute('SELECT status from jira where id_ticket = ?', [number])
    return cursor.fetchone()[0]


def get_code_label(code):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute('SELECT label from error_codes where code = ?', [code])
    return cursor.fetchone()[0]


def log(in_response_to, answer, created_at):
    connection = create_connection()
    cursor = connection.cursor()
    create_log_db()
    cursor.execute(insert_into_log_table, (in_response_to, answer, created_at))
    connection.commit()
