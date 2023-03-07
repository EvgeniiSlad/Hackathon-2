import requests
from binance.client import Client
import json
import time
import psycopg2


class Dal:
    def __init__(self, table_name: str) -> None:
        HOSTNAME = 'localhost'
        USERNAME = 'postgres'
        PASSWORD = 'popova129'
        DATABASE = 'hackathon2'
        self.table_name = table_name
        self.connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE)
        self.cursor = self.connection.cursor() 
        self._create_table_if_not_exists()

    def _create_table_if_not_exists(self):
        query = f"create table if not exists {self.table_name} (id serial primary key, time float,price float)"
        print("table created")
        self._run_query(query)
    
    def save(self, price: int) -> None:
        insert_time = time.time()
        query = f"insert into {self.table_name} (time, price) values ('{insert_time}', {price})"
        self._run_query(query)
        print(f'{price} inserted to {self.table_name}')

    def _run_query(self, query: str) -> None:
        self.cursor.execute(query)
        self.connection.commit()

class Parser():
    def __init__(self, pair):
        self.HOSTS = ['https://api.binance.com', 'https://api1.binance.com', 'https://api2.binance.com', 'https://api3.binance.com','https://api4.binance.com']
        self.pair = pair
        self.dal = Dal(pair)

    def run_forever(self):
        while True:
            for host in self.HOSTS:
                response = requests.get(f'{host}/api/v3/klines?symbol={self.pair}&interval=1m')
                if response.status_code == 200:
                    content = json.loads(response.content.decode('utf-8'))
                    # print(content[-1][4])
                    price = float(content[-1][4])
                    self.dal.save(price)
                    break
            time.sleep(60)


if __name__ == '__main__':
    parser = Parser('XRPUSDT')
    parser.run_forever()

# for k in content[-1]:
#     print(type(k))
# print(c.content)
# print(content[-1][4])
# print(response.status_code == 200)

