from asyncio.windows_events import NULL
from turtle import title
import mysql.connector
from datetime import date, datetime, timedelta
import tqdm


filename = 'trs\szwb-1.trs'
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
    data_record = {
    'title': NULL,
    'author': NULL,
    'time': NULL,
    'content': NULL,
    }
    for line in tqdm.tqdm(file):
        # add_employee = ("INSERT INTO record "
        #    "(title, author, time, content) "
        #    "VALUES (%s, %s, %s, %s)")
        # data_employee = ('Geert', 'Vanderkelen', tomorrow, 'M', date(1977, 6, 14))
        test_condition = '<REC>\n'
        if line == '<REC>\n' and data_record != null_record:
            cursor.execute(add_record, data_record)
            cnx.commit()
            print('the record is record in row', cursor.lastrowid)
            data_record = {
                'title': NULL,
                'author': NULL,
                'time': NULL,
                'content': NULL,
            }
        if line.startswith('<title>='):
            data_record['title'] = line.removeprefix('<title>=') 
        if line.startswith('<authors>='):
            data_record['author'] = line.removeprefix('<authors>=') 
        if line.startswith('<pub_time>='):
            data_record['time'] = line[11:21].replace('/', '-') 
        if line.startswith('<content>='):
            data_record['content'] = line.removeprefix('<content>=') 

        # emp_no = cursor.lastrowid         

# Make sure data is committed to the database

cursor.close()
cnx.close()
