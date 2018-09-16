import time
import web3
from web3 import Web3, HTTPProvider
from web3.contract import ConciseContract
from solc import compile_source
import requests
import json

ORACLE_URL = 'http://localhost:8546/jsonrpc'
HEADERS = {'content-type': 'application/json'}
CONTRACT_PATH = './contracts/Loan.sol'
LOAN_CONTRACT_NAME = 'Loan'
LOAN_CONTRACT_ADDRESS = '0x668ed30aacc7c7c206aaf1327d733226416233e2'
ORACLE_ADDRESS = '0xb0201641d9b936eb20155a38439ae6ab07d85fbd'
ETH_PROVIDER_URL = 'http://localhost:8545'

# Loan state
TAKEN = 2 
RETURNED = 4

def depositExists(lenderCred, amount, active):
    payload = {
        'method': depositExists,
        'params': [lenderCred],
        'jsonrpc': '2.0',
        'id': 0,
    }

    response = requests.post(
        ORACLE_URL,
        data=json.dumps(payload),
        headers=HEADERS).json()

    return response['amount'] == amount and response['active'] == active


def checkConfirmLoan():
    lenderCred = 'Whacked John'
    amount = 100
    active = True
    return (depositExists(lenderCred, amount, active))


def confirmLoan():
    with open(CONTRACT_PATH) as contract_file:
        contract_source_code = contract_file.read()
        compiled_sol = compile_source(contract_source_code,
                                      import_remappings=['=./contracts/', '-'])
        contract_interface = compiled_sol['<stdin>:' + LOAN_CONTRACT_NAME]
        w3 = Web3(Web3.HTTPProvider(ETH_PROVIDER_URL))
        w3.eth.defaultAccount = w3.eth.accounts[3]
        address = Web3.toChecksumAddress(LOAN_CONTRACT_ADDRESS)
        loan = w3.eth.contract(address=address,
                               abi=contract_interface['abi'])
        loan.functions.confirmLoan().transact()


def checkPaybackLoan():
    lenderCred = 'Whacked John'
    amount = 100
    active = False
    return (depositExists(lenderCred, amount, active))

def paybackLoan():
    with open(CONTRACT_PATH) as contract_file:
        contract_source_code = contract_file.read()
        compiled_sol = compile_source(contract_source_code,
                                      import_remappings=['=./contracts/', '-'])
        contract_interface = compiled_sol['<stdin>:' + LOAN_CONTRACT_NAME]
        w3 = Web3(Web3.HTTPProvider(ETH_PROVIDER_URL))
        w3.eth.defaultAccount = w3.eth.accounts[3]
        address = Web3.toChecksumAddress(LOAN_CONTRACT_ADDRESS)
        loan = w3.eth.contract(address=address,
                               abi=contract_interface['abi'])
        loan.functions.confirmPayback().transact()

def loanTaken():
    return getLoanState() == TAKEN

def loanReturned():
    return getLoanState() == RETURNED

def getLoanState():
    with open(CONTRACT_PATH) as contract_file:
        contract_source_code = contract_file.read()
        compiled_sol = compile_source(contract_source_code,
                                      import_remappings=['=./contracts/', '-'])
        contract_interface = compiled_sol['<stdin>:' + LOAN_CONTRACT_NAME]
        w3 = Web3(Web3.HTTPProvider(ETH_PROVIDER_URL))
        w3.eth.defaultAccount = w3.eth.accounts[2]
        address = Web3.toChecksumAddress(LOAN_CONTRACT_ADDRESS)
        loan = w3.eth.contract(address=address,
                               abi=contract_interface['abi'])

        return loan.functions.state().call()


def start():
    print('Started oracle daemon')
    while (True):
        if (loanTaken() and checkConfirmLoan()):
            confirmLoan()

        if (loanReturned() and checkPaybackLoan()):
            paybackLoan()

        time.sleep(10)
