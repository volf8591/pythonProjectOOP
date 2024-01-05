import requests
from bs4 import BeautifulSoup
import pandas
import data_client
class Parser:
    links_to_parse = [
        'https://www.kufar.by/l/mebel',
        'https://www.kufar.by/l/stulya',
        'https://www.kufar.by/l/mebel?elementType=popular_categories',
        'https://www.kufar.by/l/kuhni'
    ]
    data_client_imp = data_client.Sqlite3Client()

    @staticmethod
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

    def save_to_csv(self, mebel_items):
        pandas.DataFrame(mebel_items).to_csv('mebel.csv', index=False)

    def save_to_postgres(self, mebel_items):
        connection = self.data_client_imp.get_connection()
        self.data_client_imp.create_mebel_table(connection)
        for item in mebel_items:
            self.data_client_imp.insert(connection, item[0], item[1], item[2])

    def run(self):
        mebel_items = []
        for link in Parser.links_to_parse:
            mebel_items.extend(self.get_mebel_by_link(link))
        self.save_to_postgres(mebel_items)

    def run(self):
        mebel_items =[]
        for link in Parser.links_to_parse:
            mebel_items.extend(self.get_mebel_by_link(link))
        self.save_to_csv(mebel_items)


Parser().run()



