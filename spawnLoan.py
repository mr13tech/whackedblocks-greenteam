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
    contract_interface = compiled_sol['<stdin>:Loan']
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

    loan.functions.setOracle('0xc77eE2FA8D4173236d4565058b01dcFb7Ad3f81B').transact()
    assert(loan.functions.oracle().call() == '0xc77eE2FA8D4173236d4565058b01dcFb7Ad3f81B')
    print ("{} ".format(loan.functions.state().call()))