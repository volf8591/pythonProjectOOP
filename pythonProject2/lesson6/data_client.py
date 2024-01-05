import sqlite3
from sqlite3 import Error
# pip install psycopg2
import pandas
import psycopg2
from abc import ABC, abstractmethod


class DataClient(ABC):
    @abstractmethod
    def get_connection(self):
        pass

    @abstractmethod
    def create_mebel_table(self, conn):
        pass
    @abstractmethod
    def get_items(self, conn, price_from=0, price_to=100000):
        pass

    @abstractmethod
    def insert(self, conn, link, price, description):
        pass

    def run_test(self):
        conn = self.get_connection()
        self.create_mebel_table(conn)
        items = self.get_items(conn, price_from=100, price_to=200)
        for item in items:
            print(item)
        conn.close()


class PostgresClient(DataClient):
    USER = "postgres"
    PASSWORD = "postdres"
    HOST = "localhost"
    PORT = "5432"
    def get_connection(self):
        try:
            connection = psycopg2.connect(
                user=self.USER,
                # пароль, который указали при установке PostgreSQL
                password=self.PASSWORD,
                host=self.HOST,
                port=self.PORT)
            return connection
        except Error:
            print(Error)


    def create_mebel_table(self, conn):
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

    def get_items(self, conn, price_from=0, price_to=100000 ):
        cursor = conn.cursor()
        cursor.execute(f'SELECT * FROM mebel WHERE price >= {price_from} and price <= {price_to}')
        return cursor.fetchall()


    def insert(self, conn, link, price, description):
        cursor = conn.cursor()
        cursor.execute(f"INSERT INTO mebel(link, price, description) VALUES ('{link}', '{price}', '{description}')")
        conn.commit()



class Sqlite3Client(DataClient):
    DB_NAME = "kufar.db"


    def get_connection(self):
        try:
            conn = sqlite3.connect(self.DB_NAME)
            return conn
        except Error:
            print(Error)

    def create_mebel_table(self, conn):
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

    def get_items(self, conn, price_from=0, price_to=100000):
        cursor = conn.cursor()
        cursor.execute(f'SELECT * FROM mebel WHERE price >= {price_from} and price <= {price_to}')
        return cursor.fetchall()

    def insert(self, conn, link, price, description):
        cursor = conn.cursor()
        cursor.execute(f"INSERT INTO mebel(link, price, description) VALUES ('{link}', '{price}', '{description}')")
        conn.commit()

class CSVClient(DataClient):

    def get_connection(self):
        self.get_connection = None


    def create_mebel_table(self, conn):
        pass

    @abstractmethod
    def get_items(self, mebel_items):
        csvframe = self.create_mebel_read_csv('mebel.csv')
        csvframe


    def insert(self, conn, link, price, description):
        pandas.DataFrame(mebel_items).to_csv('mebel.csv', index=False)



# data_client = PostgresClient()
# data_client = Sqlite3Client()
data_client = CSVClient()
data_client.run_test()

