import os
import sys
import json

from models import *

def open_file(file_name):
    with open(file_name, 'r') as file:
        data = json.load(file)
        return data

def open_json(directory_path):
    files = os.listdir(directory_path)
    json_files = [f for f in files if f.endswith('.json')]
    data = []
    for file in json_files:
        ptr = open_file(directory_path + file)
        data.append(ptr)

    return data if len(data) > 0 else sys.exit('EXIT: no json files found')


def init_json():
    directory_path = 'json_data/'
    return open_json(directory_path)
