import json

with open('json\szwb-dict-list.json', encoding='UTF-8') as f:
    
    dest_dict = {}
    source_dict = json.load(f)
    for date in source_dict:
        index_in_date = 0
        for record in source_dict[date]:
            index_all = record['date'].replace('-', '') + format(index_in_date, '02d')
            dest_dict[index_all] = record
            index_in_date = index_in_date + 1

with open('json\szwb-delist.json', 'a', encoding='UTF-8') as df:
    json.dump(dest_dict, df, ensure_ascii=False, indent=4, separators=(',', ':'))