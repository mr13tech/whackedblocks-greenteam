pragma solidity 0.4.25;

import "./Ownable.sol";
import "./ERC20.sol";

contract Loan is Ownable 
{

    string public lenderCred;
    string public borowerCred;
    uint256 public amountGive; 
    uint256 public amountReturn;
    address public lender;
    address public oracle;
    uint public minPeriod; 
    uint public dateReturn;
    ERC20 token;
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
        uint256 _amountGive, 
        uint256 _amountReturn,
        uint _minPeriod,
        uint _dateReturn, 
        ERC20 _token) 
        external
    {
        require (_token.balanceOf(msg.sender) >= _amountGive, 
                "Not sufficient amount of tokens");
        
        amountGive = _amountGive;
        amountReturn = _amountReturn;
        minPeriod = _minPeriod;
        dateReturn = _dateReturn;
        token = _token;

        // make sure to send approve before claim
        token.transferFrom(
            msg.sender,
            this,
            _amountGive);

        state = STATE.OPEN;
    }

    function takeLoan() external
    {
        require(state == STATE.OPEN,
                "Loan is already taken, pardon me");

        lender = msg.sender;
        state = STATE.TAKEN;
    }

    function confirmLoan() external
    {
        require(state == STATE.TAKEN,
                "Loan is not taken yet, fuck off oracle");
        require(msg.sender == oracle,
                "Only oracle can confirm loan, pardon me");

        token.transfer(lender, amountGive);
        state = STATE.CONFIRMED;
    } 

    function openReturn(ERC20 _token) external
    {
        require (_token.balanceOf(msg.sender) >= amountGive, 
                "Not sufficient amount of tokens");
        
        // make sure to send approve before claim
        token.transferFrom(
            msg.sender,
            this,
            amountGive);
    }

    function rollBack() external 
    {
        token.transfer(owner, amountGive);
        selfdestruct(owner);
    }

}