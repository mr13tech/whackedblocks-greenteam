import argparse
from borrower_web3 import openLoan

PROG_DESC = 'Loan Borrower client'

parser = argparse.ArgumentParser(PROG_DESC)
parser.add_argument('-o', '--open', help='Open Loans publicly visible on eth blockchain', nargs=4)
args = vars(parser.parse_args())

if (args['open']):
    arguments = args['open']
    openLoan(arguments)
