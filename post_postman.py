import requests
import os
import json
from datetime import date

'''
weather api allows for one request per day,
we will save it as a timestamp in json_data dir


## READ THE API DOC to change query param

'''

key = 'C2REQFLYJ8L2B9TKC595H7TTZ'
address = 'Tarifa,Es'
address = 'jarandilla de la vera'
address = 'Barcelona'
address = 'Santander'
address = 'Sevilla'
address = 'London'
address = 'Tarifa'
address = 'Vancouver'
address = 'Lisbon'


def get_json_call():
    tmp_date = str(date.today()) + '.json'
    tmp_dir = '/json_data/'
    tmp_file = str(os.path.dirname(os.path.abspath(__file__))) + tmp_dir + tmp_date
    
    try:
        url = f'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{address}/last30days?unitGroup=us&key={key}'
        response = requests.get(url)
        data = response.json()
        with open(tmp_file, 'w') as file:
            json.dump(data, file)
            print('get_json_call: ', response.status_code)
    except:
        print('no data to show: ', response.status_code)


if __name__ == '__main__':
    get_json_call()
