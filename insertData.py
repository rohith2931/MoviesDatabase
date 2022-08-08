import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


def main():
    database = r"C:\sqlite3\MoviesDb"

    # create a database connection
    conn = create_connection(database)
    with conn:
        # create a new movie
        
        multiple_columns=[('RRR', 'Ram Charan', 'Alia Bhatt', 'Rajamouli SS', '2022' ),('Arjun Reddy', 'Vijay Devarakonda', 'Shalini Pandey', 'Sandeep Reddy Vanga', '2017'),('Pushpa: The Rise', 'Allu Arjun', 'Rashmika Mandanna', 'Sukumar', '2021')]
        sql = ''' INSERT INTO Movies(name,actor,actress,director,year_of_release) VALUES(?,?,?,?,?) '''
        cur = conn.cursor()
        cur.executemany(sql, multiple_columns)
        print("rows inserted")
#main fctn
main()