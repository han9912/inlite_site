from asyncio.windows_events import NULL
from turtle import title
import mysql.connector
from datetime import date, datetime, timedelta
import tqdm
import json


filename = 'szwb-data\json\szwb-delist.json'
cnx = mysql.connector.connect(user = 'root', 
                                password = 'admins', 
                                host = 'localhost', 
                                database = 'paper')
cursor = cnx.cursor()
add_record = ("INSERT INTO record "
        "(title, author, date, content, category1, category2, page, page_name) "
        "VALUES (%(title)s, %(author)s, %(date)s, %(content)s, %(category1)s, %(category2)s, %(page)s, %(page_name)s)")

print('before with open method')
with open(filename, encoding='UTF-8') as file:
    record_dict = json.load(file)
    print('open with success')
    for record in tqdm.tqdm(record_dict):
        cursor.execute(add_record, record_dict[record])
        cnx.commit()

cursor.close()
cnx.close()
