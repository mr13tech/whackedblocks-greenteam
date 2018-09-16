## Dependencies

### Python >=3.5.3 

* Install pip if it is not available
* Install virtualenv if it is not available
* Create a virtual environment
* Activate your new virtual environment
* Install dependencies

``` bash
which pip || curl https://bootstrap.pypa.io/get-pip.py | python
which virtualenv || sudo pip install --upgrade virtualenv
virtualenv -p python3 ~/.venv-py3
source ~/.venv-py3/bin/activate
pip install -r ./requirements.txt
```

### ganache-cli 

```bash
npm install -g ganache-cli
```

#### Available Accounts within ganache blockchain (mnemonic)
* (0) 0x959fd7ef9089b7142b6b908dc3a8af7aa8ff0fa1 -- Contracts Deployer
* (1) 0x4e90a36b45879f5bae71b57ad525e817afa54890 -- Borrower
* (2) 0xb6a8490101a0521677b66866b8052ee9f9975c17 -- Lender
* (3) 0xb0201641d9b936eb20155a38439ae6ab07d85fbd -- Oracle

#### Contract Address 
* (0) 0x668ed30aacc7c7c206aaf1327d733226416233e2 -- Loan 
* (1) 0xd2e8d9173584d4daa5c8354a79ef75cec2dfa228 -- DAIMock   


## Usage 
### Borrower Client 
```
usage: Loan Borrower client [-h] [-o amountGive amountReturn time token]

optional arguments:
  -h, --help            show this help message and exit
  -o amountGive amountReturn time token, --open amountGive amountReturn time token
                        Open Loans publicly visible on eth blockchain
```

### Lender Client
```
usage: Loan Lender client [-h] [-t loan_address] [-r loan_address] [loans]

positional arguments:
  loans                 Show loans

optional arguments:
  -h, --help            show this help message and exit
  -t TAKE, --take TAKE  Take loan from `loans` list
  -r RETURN, --return loan_address
                        Return loan amount

```