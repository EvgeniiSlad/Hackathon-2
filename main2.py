import psycopg2
import pandas 
import numpy
import matplotlib.pyplot as plt


HOSTNAME = 'localhost'
USERNAME = 'postgres'
PASSWORD = 'popova129'
DATABASE = 'hackathon2'

connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE)
cursor = connection.cursor() 
database_name = input("Plese write name of database like 'btcbusd':") 
query = f"SELECT time FROM {database_name}"
cursor.execute(query)
time = cursor.fetchall()
print(time)
query1 = f"SELECT price FROM {database_name}"
cursor.execute(query1)
price = cursor.fetchall()
print(price)
connection.close()

x = time
y = price
plt.plot(x,y)
plt.xlabel('Price of BTC')
plt.ylabel('Time')
plt.show()
