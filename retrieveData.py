import sqlite3
from sqlite3 import Error


def createConnection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


def select_all_movies(conn):
    """
    Query all rows in the movies table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM Movies")

    rows = cur.fetchall()

    for row in rows:
        print(row)


def select_task_by_actorName(conn, actorName):
    """
    Query movies by actorName
    :param conn: the Connection object
    :param actorName:
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM Movies WHERE actor=?", (actorName,))

    rows = cur.fetchall()

    for row in rows:
        print(row)


def main():
    database = r"C:\sqlite3\MoviesDb"

    # create a database connection
    conn = createConnection(database)
    with conn:
        print("1. Query all movies")
        select_all_movies(conn)

        print("2. Query task by actor name")
        select_task_by_actorName(conn, 'Allu Arjun')

#main fctn
main()