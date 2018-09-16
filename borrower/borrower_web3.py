import web3
from web3 import Web3, HTTPProvider
from web3.contract import ConciseContract
from solc import compile_source


CONTRACT_PATH = './contracts/Loan.sol'
LOAN_CONTRACT_NAME = 'Loan'
LOAN_CONTRACT_ADDRESS = '0x668ed30aacc7c7c206aaf1327d733226416233e2'
ORACLE_ADDRESS = '0xb0201641d9b936eb20155a38439ae6ab07d85fbd'
ETH_PROVIDER_URL = 'http://localhost:8545'


def openLoan(args):
    # =============================INIT LOAN==================================
    with open(CONTRACT_PATH) as contract_file:
        contract_source_code = contract_file.read()
        compiled_sol = compile_source(contract_source_code,
                                      import_remappings=['=./contracts/', '-'])
        contract_interface = compiled_sol['<stdin>:' + LOAN_CONTRACT_NAME]
        w3 = Web3(Web3.HTTPProvider(ETH_PROVIDER_URL))
        w3.eth.defaultAccount = w3.eth.accounts[1]
        address = Web3.toChecksumAddress(LOAN_CONTRACT_ADDRESS)
        loan = w3.eth.contract(address=address,
                               abi=contract_interface['abi'])
    # =========================================================================
    
    amountGive = int(args[0])
    amountReturn = int(args[1])
    months = int(args[2])
    tokenAddress = Web3.toChecksumAddress(args[3])

    loan.functions.openLoan(amountGive, amountReturn, months, tokenAddress).transact()