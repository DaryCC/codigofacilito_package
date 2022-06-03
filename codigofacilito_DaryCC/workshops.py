import requests


def unreleased():
    response = requests.get('https://codigofacilito.com/api/v2/workshops/unreleased')
    # response = requests.get('https://jsonplaceholder.typicode.com/users')
    if response.status_code == 200:
        payload = response.json()
        return payload
