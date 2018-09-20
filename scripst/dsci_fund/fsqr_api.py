import requests
import json


def get_places(query, ll='40.7243,-74.0018'):
    url = 'https://api.foursquare.com/v2/venues/explore'
    with open('config.json', 'r') as f:
        file_str = f.read()
        file_str = json.loads(file_str)
        CLIENT_ID = file_str['CLIENT_ID']
        CLIENT_SECRET = file_str['CLIENT_SECRET']

    params = {
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'v': '20180323',
        'll': ll,
        'query': query,
    }
    res = requests.get(url, params=params)
    return res.json()


print(get_places("coffee"))
