import sqlite3
import os

DATABASE_PATH = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    "database",
    "employee.db"
)

"""
    Creates and returns a connection to the SQLite database.
    Every database operation in this project should use this function
    instead of creating a connection manually.
"""
def get_connection():
    connection = sqlite3.connect(DATABASE_PATH)
    connection.row_factory = sqlite3.Row    #Return rows like dictionaries instead of tuples
    connection.execute("PRAGMA foreign_keys = ON;")  #make sure foreign keys are enabled
    return connection