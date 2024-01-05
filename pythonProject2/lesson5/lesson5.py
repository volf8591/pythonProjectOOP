import requests
from bs4 import BeautifulSoup
import pandas
import sqlite_client
# pip install beautifulsoup4
# pip install pandas


links_to_parce = [
    'https://www.kufar.by/l/mebel',
    'https://www.kufar.by/l/stulya',
    'https://www.kufar.by/l/mebel?elementType=popular_categories',
    'https://www.kufar.by/l/kuhni'
]
def get_mebel_by_link(link):
    response = requests.get(link)
    mebel_data = response.text

    mebel_items = []
    to_parse = BeautifulSoup(mebel_data, 'html.parser')
    for elem in to_parse.find_all('a', class_='styles_wrapper__5FoK7'):
        try:
            price, decription = elem.text.split('р.')
            mebel_items.append((
                elem['href'],
                int(price.replace('  ', '')),
                decription
            ))
        except:
            print(f'Цена не указана.{elem.text}')
    return mebel_items

def save_to_csv(mebel_items):
    pandas.DataFrame(mebel_items).to_csv('mebel.csv', index=False)


def save_to_sqlite(mebel_items):
    connection = sqlite_client.get_connection()
    for item in mebel_items:
        sqlite_client.insert(connection, item[0], item[1], item[2])

def run():
    mebel_items = []
    for link in links_to_parce:
        mebel_items.extend(get_mebel_by_link(link))
    save_to_sqlite(mebel_items)

run()