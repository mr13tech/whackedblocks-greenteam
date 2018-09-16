import json
import web3
from web3 import Web3, HTTPProvider
from solc import compile_source
from web3.contract import ConciseContract

TOKEN_ADDRESS = '0xd2e8d9173584d4daa5c8354a79ef75cec2dfa228'
LOAN_ADDRESS = '0x668ed30aacc7c7c206aaf1327d733226416233e2'

LENDER_ADDRESS = '0xb6a8490101a0521677b66866b8052ee9f9975c17'
BORROWER_ADDRESS = '0x4e90a36b45879f5bae71b57ad525e817afa54890'
ORACLE_ADDRESS = '0xb0201641d9b936eb20155a38439ae6ab07d85fbd'

cotracts_path = './contracts/'
token_src = 'DAIMock'
loan_src = 'Loan'

w3 = Web3(Web3.HTTPProvider('http://localhost:8545'))
token_src_file = open(cotracts_path + token_src + '.sol')
token_src_code = token_src_file.read()
token_compiled = compile_source(token_src_code,
                                import_remappings=['=./contracts/', '-'])
token_interface = token_compiled['<stdin>:'+token_src]

token_address = Web3.toChecksumAddress(TOKEN_ADDRESS)
token = w3.eth.contract(address=token_address,
                        abi=token_interface['abi'])

loan_src_file = open(cotracts_path + loan_src + '.sol')
loan_src_code = loan_src_file.read()
loan_compiled = compile_source(loan_src_code,
                                import_remappings=['=./contracts/', '-'])
loan_interface = loan_compiled['<stdin>:'+loan_src]
loan_address = Web3.toChecksumAddress(LOAN_ADDRESS)
loan = w3.eth.contract(address = loan_address,
                      abi = loan_interface['abi'])

def showLoanMeta(loan):
    amountGive = loan.functions.amountGive().call()
    amountReturn = loan.functions.amountReturn().call()
    dateReturn = loan.functions.dateReturn().call()
    token = loan.functions.token().call()

    print ('amountGive:' + str(amountGive))
    print('amountReturn:' + str(amountReturn))
    print('dateReturn:' + str(dateReturn))
    print('token:' + token)


def logBalance(address, name, token):
    adr=Web3.toChecksumAddress(address)
    balance=token.functions.balanceOf(adr).call()
    symbol=token.functions.symbol().call()
    print (name + ':' + adr + ' ' + str(balance) + ' ' + symbol)


def logAllowance(owner, spender, owner_name, spender_name, token):
    owner_adr=Web3.toChecksumAddress(owner)
    spender_adr=Web3.toChecksumAddress(spender)
    allowance=token.functions.allowance(owner_adr, spender_adr).call()
    symbol=token.functions.symbol().call()

    print (owner_name+':'+owner_adr + ' approved '+str(allowance) + ' ' + symbol + ' for '
           + spender_name+':'+spender_adr)


logBalance(LENDER_ADDRESS, 'LENDER', token)
logBalance(BORROWER_ADDRESS, 'BORROWER', token)
logBalance(ORACLE_ADDRESS, 'ORACLE', token)
logBalance(LOAN_ADDRESS, 'LOAN', token)

print('\n')

logAllowance(LENDER_ADDRESS, LOAN_ADDRESS, 'LENDER',  'LOAN', token)
logAllowance(BORROWER_ADDRESS, LOAN_ADDRESS, 'BORROWER',  'LOAN', token)

print('\n')

showLoanMeta(loan)