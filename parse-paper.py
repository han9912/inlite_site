from asyncio.windows_events import NULL
from turtle import title
import mysql.connector
from datetime import date, datetime, timedelta
import tqdm

if __name__ == "__main__":
    filename = 'trs\szwb-0.trs'
    cnx = mysql.connector.connect(user = 'root', 
                                  password = 'admins', 
                                  host = 'localhost', 
                                  database = 'paper')
    cursor = cnx.cursor()
    add_record = ("INSERT INTO record "
            "(title, author, time, content) "
            "VALUES (%(title)s, %(author)s, %(time)s, %(content)s)")
    
    null_record = {
        'title': NULL,
        'author': NULL,
        'time': NULL,
        'content': NULL,
    }
    print('before with open method')
    with open(filename, encoding='UTF-8') as file:
        print('open with success')
        data_record = null_record
        for line in tqdm.tqdm(file):
            # add_employee = ("INSERT INTO record "
            #    "(title, author, time, content) "
            #    "VALUES (%s, %s, %s, %s)")
            # data_employee = ('Geert', 'Vanderkelen', tomorrow, 'M', date(1977, 6, 14))
            if line == '<REC>' and data_record != null_record:
                cursor.execute(add_record, data_record)
                data_record = null_record
            
            if line.startswith('<title>='):
                data_record['title'] = line.removeprefix('<title>=') 
            if line.startswith('<authors>='):
                data_record['author'] = line.removeprefix('<authors>=') 
            if line.startswith('<pub_data>='):
                data_record['time'] = line.removeprefix('<pub_data>=') 
            if line.startswith('<content>='):
                data_record['content'] = line.removeprefix('<content>=')[11:21].replace('/', '-') 

            # emp_no = cursor.lastrowid
  

            # Make sure data is committed to the database
else:
    print('fail to name equals main')
cnx.commit()

cursor.close()
cnx.close()
