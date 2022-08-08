import sqlite3
from sqlite3 import Error


def createConnection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print("Database created!!")
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


#main fctn
createConnection(r"C:\sqlite3\MoviesDb")