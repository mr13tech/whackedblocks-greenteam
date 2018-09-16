LOAN_CONTRACT_ADDRESS = '0x668ed30aacc7c7c206aaf1327d733226416233e2'

EXISTS = False

def getLoans():
    loans = {
        'address': '0x668ed30aacc7c7c206aaf1327d733226416233e2',
        'amountGive': 100,
        'amountReturn': 110,
        'returnDate': '3 months',
        'token': 'DAI',
    }
    return loans

def depositExists(lenderCred):
    return EXISTS

def setDeposit(flag):
    EXISTS = flag
