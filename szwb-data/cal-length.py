import json
max_content = 0
max_title = 0
max_author = 0
with open('szwb-data\json\szwb-delist.json', encoding='UTF-8') as f:

    source_dict = json.load(f)
    for record in source_dict:
        if len(str(source_dict[record]['content'])) > max_content:
            max_content = len(str(source_dict[record]['content']))
            ic = source_dict[record]['content']
        if len(str(source_dict[record]['title'])) > max_title:
            max_title = len(str(source_dict[record]['title']))
            it = source_dict[record]['title']
        if len(str(source_dict[record]['author'])) > max_author:
            max_author = len(str(source_dict[record]['author']))
            ia = source_dict[record]['author']
    print(max_content, max_title, max_author)
    print('max content:{}\n max title{}\n max author{}'.format(ic, it, ia))

