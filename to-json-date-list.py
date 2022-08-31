from distutils import filelist
import json

from asyncio.windows_events import NULL
from turtle import title

from datetime import date, datetime, timedelta
import tqdm

file_list = ['trs\szwb-0.txt', 'trs\szwb-1.txt']

json_filename = 'json\szwb-dict-list.json'
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

json_file = open(json_filename, "a", encoding='UTF-8')
for filename in file_list:
    with open(filename, encoding='UTF-8') as open_file:
        print('begin scan {}'.format(filename))
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
        file = open_file.readlines()
        for i, line in tqdm.tqdm(enumerate(file)):

            test_condition = '<REC>\n'
            if line == '<REC>\n' and data_record != null_record:
                
                date_num = data_record['date'].replace('-', '')
                if date_num in record_dict.keys(): 
                    if not(data_record in record_dict[date_num]):
                        record_dict[date_num].append(data_record)
                else:
                    record_dict[date_num] = []
                    record_dict[date_num].append(data_record)
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
                data_record['title'] = line.removeprefix('<title>=').strip() 
            if line.startswith('<authors>='):
                data_record['author'] = line.removeprefix('<authors>=').strip() 
            if line.startswith('<pub_time>='):
                data_record['date'] = line[11:21].replace('/', '-') 
            if line.startswith('<content>='):
                data_record['content'] = line.removeprefix('<content>=').strip() 
                temp_i = i + 1
                while not(file[temp_i].startswith('<')):
                    data_record['content'] = data_record['content'] + file[temp_i].strip() 
                    temp_i = temp_i + 1
            if line.startswith('<category1>='):
                data_record['category1'] = line.removeprefix('<category1>=').strip() 
            if line.startswith('<category2>='):
                data_record['category2'] = line.removeprefix('<category2>=').strip() 
            if line.startswith('<bc>='):
                data_record['page'] = line.removeprefix('<bc>=').strip()  
            if line.startswith('<bm>='):
                data_record['page_name'] = line.removeprefix('<bm>=').strip()  

print('begin dumping to json')
json.dump(record_dict, json_file, ensure_ascii=False, sort_keys=True, indent= 4, separators=(',' ':'))