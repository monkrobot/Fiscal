import requests
from datetime import datetime
from time import time


def trip_post():
    data = {
        'datetime': str(datetime.now()),
        'inn': 11,
        'kpp': 21,
        'price': 150
    }
    r = requests.post('http://127.0.0.1:8000/data/trip', json=data)
    return r.text


if __name__ == "__main__":
    start = time()
    for i in range(1):
        print(trip_post())
    print(time() - start)
