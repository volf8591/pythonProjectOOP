import sqlite3
from bs4 import BeautifulSoup
from sqlite3 import Error
from

def sql_connection():
    try:
        conn = sqlite3.connect('kufar.db')
        return conn
    except Error:
        print(Error)


def create_mebel_table(conn):
    cursor_object = conn.cursor()
    cursor_object.execute(
        """
            CREATE TABLE IF NOT EXISTS mebel
            (
                id integer PRIMARY KEY autoincrement, 
                link text, 
                price integer,
                description text
            )
        """
    )
    conn.commit()

def get_items(conn):
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM mebel')
    return cursor.fetchall()


def insert(conn, link, price, description):
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO mebel('{link}', '{price}', '{description}')")
    return cursor.fetchall()

def sqlite_test():
    # conn = sql_connection()
    # create_mebel_table(conn)
    # print(get_items(conn))
    # conn.close()
    pass

# sqlite_test()