import sqlite3
from sqlite3 import Error


def createConnection(db_file):
    """ create a database connection to the SQLite database specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn


def createTable(conn, createTable_sql):
    """ create a table from the createTable_sql statement
    :param conn: Connection object
    :param createTable_sql: a CREATE TABLE statement
    :return:
    """
    try:
        cursor = conn.cursor()
        cursor.execute(createTable_sql)
        print("Table Created!!")
    except Error as e:
        print(e)


def main():
    database = r"C:\sqlite3\MoviesDb"
    sql_create_movies_table = """ CREATE TABLE IF NOT EXISTS Movies (
                                        name text NOT NULL,
                                        actor text NOT NULL,
                                        actress text NOT NULL,
                                        director text NOT NULL,
                                        year_of_release smallint NOT NULL
                                    ); """

    # create a database connection
    conn = createConnection(database)

    # create tables
    if conn:
        # create movies table
        createTable(conn, sql_create_movies_table)
    else:
        print("Error in Creating Database Connection....!!!")

#main fctn
main()