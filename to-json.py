import json

from asyncio.windows_events import NULL
from turtle import title

from datetime import date, datetime, timedelta
import tqdm


filename = 'trs\szwb-0.txt'
json_filename = 'json\szwb-0-debug.json'
record_dict = {}
null_record = {
    'title': NULL,
    'author': NULL,
    'date': NULL,
    'content': NULL,
    'category1':NULL,
    'category2':NULL,
    'page':NULL,
    'page_name':NULL
}

with open(filename, encoding='UTF-8') as open_file:
    print('open with success')
    data_record = {
    'title': NULL,
    'author': NULL,
    'date': NULL,
    'content': NULL,
    'category1':NULL,
    'category2':NULL,
    'page':NULL,
    'page_name':NULL
    }
    json_file = open(json_filename, "a")
    last_date = '19000101'
    index_inday = 0
    file = open_file.readlines()
    for i, line in tqdm.tqdm(enumerate(file)):

        test_condition = '<REC>\n'
        if line == '<REC>\n' and data_record != null_record:
            
            date_num = data_record['date'].replace('-', '')
            if date_num == last_date: 
                index_inday +=1
            else:
                index_inday = 0
                last_date = date_num

            record_index = date_num + format(index_inday, '02d')
            record_dict[record_index] = data_record
            data_record = {
                'title': NULL,
                'author': NULL,
                'date': NULL,
                'content': NULL,
                'category1':NULL,
                'category2':NULL,
                'page':NULL,
                'page_name':NULL
            }
        if line.startswith('<title>='):
            data_record['title'] = line.removeprefix('<title>=') 
        if line.startswith('<authors>='):
            data_record['author'] = line.removeprefix('<authors>=') 
        if line.startswith('<pub_time>='):
            data_record['date'] = line[11:21].replace('/', '-') 
        if line.startswith('<content>='):
            data_record['content'] = line.removeprefix('<content>=')
            temp_i = i + 1
            while not(file[temp_i].startswith('<')):
                data_record['content'] = data_record['content'] + file[temp_i]
                temp_i = temp_i + 1
        if line.startswith('<category1>='):
            data_record['category1'] = line.removeprefix('<category1>=') 
        if line.startswith('<category2>='):
            data_record['category2'] = line.removeprefix('<category2>=') 
        if line.startswith('<bc>='):
            data_record['page'] = line.removeprefix('<bc>=') 
        if line.startswith('<bm>='):
            data_record['page_name'] = line.removeprefix('<bm>=') 
    print('begin dumping to json')
    json.dump(record_dict, json_file, indent= 4, separators=(',' ':'), )