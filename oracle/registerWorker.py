import argparse
import requests
import json

PROG_DESC = 'Deposit Register worker'
ORACLE_URL = 'http://localhost:8546/jsonrpc'
HEADERS = {'content-type': 'application/json'}


def addDepositRegister(deposit):

    payload = {
        'method': 'setDeposit',
        'params': [True],
        'jsonrpc': '2.0',
        'id': 0,
    }

    response = requests.post(
        ORACLE_URL,
        data=json.dumps(payload),
        headers=HEADERS).json()

    print(response)


parser = argparse.ArgumentParser(PROG_DESC)
parser.add_argument('-a', '--add', help='Add deposit register', nargs=3)
args = vars(parser.parse_args())

if (args['add']):
    arguments = args['add']
    addDepositRegister(arguments)