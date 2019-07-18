import sys
import json
from pprint import pprint
from elasticsearch import Elasticsearch
es = Elasticsearch(
    ['localhost'],
    port=9200

)

MyFile= open('./emails/aimeeeng.json','r').read()
ClearData = MyFile.splitlines(True)
i=0
json_str=""
docs ={}
for line in ClearData:
    line = ''.join(line.split())
    if line != "},":
        json_str = json_str+line
    else:
        docs[i]=json_str+"}"
        json_str=""
        print(docs[i])
        es.index(index='ousd', doc_type='email', id=i, body=docs[i])
        i=i+1