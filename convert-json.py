from asyncio.windows_events import NULL
import json
import tqdm

filename = 'trs\szwb-0.txt'
json_filename = 'json\szwb-0-record-dict-utf8.json'
null_record = {
    'title': NULL,
    'author': NULL,
    'time': NULL,
    'content': NULL,
}
record_list = []

with open(filename, encoding='UTF-8') as file:
    
    json_fp = open(json_filename, "a", encoding='UTF-8')
    print('open with success')
    data_record = {
        'title': NULL,
        'author': NULL,
        'time': NULL,
        'content': NULL,
    }
    for line in tqdm.tqdm(file):

        if line == '<REC>\n' and data_record != null_record:
            record_list.append(data_record)
            
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
    json.dump(record_list, json_fp, indent=4, separators=(',', ': '))