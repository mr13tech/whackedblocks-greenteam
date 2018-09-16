import argparse

from lender_rpc import showLoans
from lender_web3 import takeLoan, paybackLoan

PROG_DESC = 'Loan Lender client'

parser = argparse.ArgumentParser(PROG_DESC)

parser.add_argument('loans', help='Show loans', nargs='?')
parser.add_argument('-t', '--take', help='Take loan from `loans` list')
parser.add_argument('-r', '--return', help='Return loan amount')

args = vars(parser.parse_args())

if (args['loans'] == 'loans'):
    showLoans()

if (args['take']):
    loanAddress = args['take']
    takeLoan(loanAddress)

if (args['return']):
    loanAddress = args['return']
    paybackLoan(loanAddress)
