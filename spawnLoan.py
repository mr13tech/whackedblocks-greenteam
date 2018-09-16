import json
import web3
from web3 import Web3, HTTPProvider
from solc import compile_source
from web3.contract import ConciseContract

cotract_path = './contracts/Loan.sol'
contract_name = 'Loan'

with open(cotract_path) as contract_file:
    contract_source_code = contract_file.read()
    compiled_sol = compile_source(contract_source_code, import_remappings=[
                                  '=./contracts/', '-'])  # Compiled source
    contract_interface = compiled_sol['<stdin>:'+contract_name]
    w3 = Web3(Web3.HTTPProvider('http://localhost:8545'))
    w3.eth.defaultAccount = w3.eth.accounts[0]
    # Instantiate and deploy contract
    Loan = w3.eth.contract(abi=contract_interface['abi'],
                           bytecode=contract_interface['bin'])

    tx_hash = Loan.constructor().transact()
    tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)

    loan = w3.eth.contract(address=tx_receipt.contractAddress,
                           abi=contract_interface['abi'])

    # print ("{} ".format(loan.all_functions()))

    oracleAddress = Web3.toChecksumAddress('0x35e13c4870077f4610b74f23e887cbb10e21c19f')
    loan.functions.setOracle(oracleAddress).transact()
    oracleContract = loan.functions.oracle().call()