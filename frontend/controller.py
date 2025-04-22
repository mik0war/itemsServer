import requests
import json

BASE_URL = 'http://127.0.0.1:5000'


def load_items():
    try:
        response = requests.get(BASE_URL + '/get_items')

    except Exception as exception:
        print(exception)
        return

    if response.status_code == 200:
        return json.loads(response.text)

