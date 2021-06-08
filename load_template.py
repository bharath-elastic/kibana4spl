# export data from an index into ndjson or bulk index format
# support for cloud-id using api-key only

import argparse, json 
from elasticsearch import Elasticsearch
from config import esconfig
from elasticsearch.client import IndicesClient

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('file', help='name of the file')
    parser.add_argument('template_name', help='name of the template')
    args = parser.parse_args()
    return args

def get_clients():
    endpoint = esconfig[0]['endpoint']
    user = esconfig[0]['user']
    password = esconfig[0]['password']
    es = Elasticsearch([endpoint], http_auth=(user,password))
    ic = IndicesClient(es)
    return es,ic

def get_template():
    with open(args.file) as f:
        return json.load(f)

def load_template(ic, template):
    ic.put_template(args.template_name, template)

args = parse_args()
es,ic = get_clients()
load_template(ic, get_template())
