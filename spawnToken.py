import json
import web3
from web3 import Web3, HTTPProvider
from solc import compile_source
from web3.contract import ConciseContract

cotract_path = './contracts/DAIMock.sol'
contract_name = 'DAIMock'

LOAN_ADDRESS = '0x668ed30aacc7c7c206aaf1327d733226416233e2'


with open(cotract_path) as contract_file:
    w3 = Web3(Web3.HTTPProvider('http://localhost:8545'))
    w3.eth.defaultAccount = w3.eth.accounts[0]

    contract_source_code = contract_file.read()
    compiled_sol = compile_source(contract_source_code,
                                  import_remappings=['=./contracts/', '-'])
    contract_interface = compiled_sol['<stdin>:'+contract_name]

    Token = w3.eth.contract(abi=contract_interface['abi'],
                            bytecode=contract_interface['bin'])

    # ============Top up borrower token balance in constructor=================
    initialAddress = Web3.toChecksumAddress(w3.eth.accounts[1])
    initialBalance = 1000000
    name = 'DAI DENEG'
    symbol = 'DAI'
    decimals = 18

    tx_hash = Token.constructor(initialAddress,
                                initialBalance,
                                name,
                                symbol,
                                decimals).transact()

    tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)

    token = w3.eth.contract(address=tx_receipt.contractAddress,
                            abi=contract_interface['abi'])
    #===============================================================

    #=================Invoke approve for `tranferFrom`==============    
    # Allow Loan contract to spend borrower tokens
    spender = Web3.toChecksumAddress(LOAN_ADDRESS) 
    amount = 100 
    w3.eth.defaultAccount = w3.eth.accounts[1]
    approve_hash = token.functions.approve(spender, amount).transact()
    approve_receipt = w3.eth.waitForTransactionReceipt(approve_hash)

