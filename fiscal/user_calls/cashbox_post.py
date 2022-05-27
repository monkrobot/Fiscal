import requests

from time import time


def cashbox_post():
    data = {
        'inn': 111,
        'kpp': 121,
        'registration_num': 134
    }
    r = requests.post('http://127.0.0.1:8000/data/cashbox', json=data)
    return r.text

if __name__ == "__main__":
    start = time()
    for i in range(1):
        cashbox_post()
    print(cashbox_post())
    print(time() - start)
