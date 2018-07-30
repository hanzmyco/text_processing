import json
from pprint import pprint
import sys
from pathlib import Path
from pathlib import PureWindowsPath
p=Path(sys.argv[1])
file_names=list(p.glob('*.txt'))
documents={}

for file_name in file_names:
    file_name=str(file_name)
    with open(file_name,encoding='utf-8') as f:
        data = json.load(f)
        for vid in data:
            ite = ''
            for text in data[vid].split('\n'):
                words = text.strip().split(']')
                if len(words) > 1 and (words[1] != '\n' or words[1] != '\r'):
                    # print(words[1])
                    for token in words[1]:
                        if token !='' and token !=' ':
                            ite += token+' '
            documents[vid] = ite

#,encoding='utf-8'
with open(sys.argv[2], 'w',encoding='utf-8') as fp:
    limit=0
    for ite in documents:
        if limit>10:
            break
        limit+=1
        fp.write(documents[ite]+'\n')

    #json.dump(documents, fp)

'''
with open(sys.argv[2],encoding='utf-8') as f:
    data_recover = json.load(f)
pprint(data_recover)
'''
#pprint(data)