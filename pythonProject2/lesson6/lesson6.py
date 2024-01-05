import requests
from bs4 import BeautifulSoup
import pandas
import postgresql_client
# pip install beautifulsoup4
# pip install pandas



def save_to_csv(mebel_items):
    pandas.DataFrame(mebel_items).to_csv('mebel.csv', index=False)


def save_to_postgres(mebel_items):
    connection = postgresql_client.get_connection()
    for item in mebel_items:
        postgresql_client.insert(connection, item[0], item[1], item[2])

def run():
    mebel_items = []
    for link in links_to_parce:
        mebel_items.extend(get_mebel_by_link(link))
    save_to_postgres(mebel_items)

run()