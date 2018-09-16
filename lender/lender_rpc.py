import requests
import json

ORACLE_URL = 'http://localhost:8546/jsonrpc'
HEADERS = {'content-type': 'application/json'}

def showLoans():
    payload = {
        'method': 'getLoans',
        'params': [],
        'jsonrpc': '2.0',
        'id': 0,
    }

    response = requests.post(
        ORACLE_URL,
        data=json.dumps(payload),
        headers=HEADERS).json()

    print(response)
