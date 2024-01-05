from sqlite3 import Error
# pip install psycopg2
import psycopg2


def get_connection():
    try:
        connection = psycopg2.connect(
            user="postgres",
            # пароль, который указали при установке PostgreSQL
            password="postgres",
            host="127.0.0.1",
            port="5432")
        return connection
    except Error:
        print(Error)


def create_mebel_table(conn):
    cursor_object = conn.cursor()
    cursor_object.execute(
        """
            CREATE TABLE IF NOT EXISTS mebel
            (
                id serial PRIMARY KEY, 
                link text, 
                price integer,
                description text
            )
        """
    )
    conn.commit()

def get_items(conn, price_from=0, price_to=100000 ):
    cursor = conn.cursor()
    cursor.execute(f'SELECT * FROM mebel WHERE price >= {price_from} and price <= {price_to}')
    return cursor.fetchall()


def insert(conn, link, price, description):
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO mebel(link, price, description) VALUES ('{link}', '{price}', '{description}')")
    conn.commit()


def run():
    conn = get_connection()
    create_mebel_table(conn)
    items = get_items(conn, price_from=100, price_to=200)
    for item in items:
        print(item)
    conn.close()

run()