pragma solidity 0.4.25;

import "./Ownable.sol";
import "./ERC20/IERC20.sol";

contract Loan is Ownable 
{

    string public lenderCred;
    string public borowerCred;
    uint256 public amountGive; 
    uint256 public amountReturn;
    address public borrower;
    address public oracle;
    uint public minPeriod; 
    uint public dateReturn;
    IERC20 public token;
    enum STATE {EMPTY, OPEN, TAKEN, CONFIRMED, RETURNED}
    STATE public state;

    constructor() public 
    {
        owner = msg.sender;
        state = STATE.EMPTY;
    }

    function setOracle(address _oracle) external 
    {
        require (msg.sender == owner);
        oracle = _oracle;
    }

    function openLoan(
        string _lenderCred,
        uint256 _amountGive, 
        uint256 _amountReturn,
        uint _dateReturn, 
        IERC20 _token) 
        public
    {
        require (_token.balanceOf(msg.sender) >= _amountGive, 
                'Not sufficient amount of tokens');
        
        lenderCred = _lenderCred;
        amountGive = _amountGive;
        amountReturn = _amountReturn;
        dateReturn = _dateReturn;
        token = _token;
        
        token.transferFrom(
            msg.sender,
            this,
            amountGive);

        state = STATE.OPEN;
    }

    function takeLoan() external
    {
        require(state == STATE.OPEN,
                'Loan is not opened, pardon me');

        borrower = msg.sender;
        state = STATE.TAKEN;
    }

    function confirmLoan() external
    {
        require(msg.sender == oracle,
                'Only oracle can confirm loan, pardon me');
        require(state == STATE.TAKEN,
                'Loan is not taken yet, fuck off oracle');

        token.transfer(borrower, amountGive);
        state = STATE.CONFIRMED;
    } 

    function paybackLoan(IERC20 _token) external
    {   
        require(state == STATE.CONFIRMED,
                'Loan is not confirmed yet');
        require (_token.balanceOf(msg.sender) >= amountReturn, 
                'Not sufficient amount of tokens');
        
        // make sure to send approve before claim
        token.transferFrom(
            msg.sender,
            this,
            amountGive);
        
        state = STATE.RETURNED;
    }

    function confirmPayback() external 
    {
        require(msg.sender == oracle,
       'Only oracle can confirm loan, pardon me');
        require(state == STATE.RETURNED, 
                'Loan is not returned yet');

        token.transfer(owner, amountReturn);
        selfdestruct(owner);        
    }

    function rollBack() external 
    {
        require(msg.sender == owner,
                'Only loan creator can revoke loan');
        token.transfer(owner, amountGive);
        selfdestruct(owner);
    }
}