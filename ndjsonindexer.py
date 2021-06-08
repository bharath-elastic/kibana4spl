# load ndjson data into elasticsearch
import argparse, json
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
from config import esconfig

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('file', help='name of the csv file')
    parser.add_argument('index', help='elasticsearch index name')
    args = parser.parse_args()
    return args

def docs(file_name):
    with open(file_name, 'r') as f:
        for doc in f:
            yield json.loads(doc)

def make_actions(docs, index_name):
    for doc in docs:
        action =  { "_index": index_name }
        action["_source"] = doc
        yield action

def get_credentials():
    user = input('Username: ')
    if user:
        pwd = getpass.getpass()
        return (user, pwd)
    else:
        return(None,None)

def get_clients():
    es = Elasticsearch(endpoint, http_auth=(user,password))
    return es

args = parse_args()
user = esconfig[0]['user']
endpoint = esconfig[0]['endpoint']
password = esconfig[0]['password']
es = get_clients()
actions = make_actions(docs(args.file), args.index)
b = bulk(es, actions)
