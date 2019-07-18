from elasticsearch import Elasticsearch

es = Elasticsearch()

es.info()
#es.get(index='ousd', doc_type='email', id='1')