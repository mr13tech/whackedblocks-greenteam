pragma solidity 0.4.25;

import "./ERC20/ERC20.sol";

contract DAIMock is ERC20 
{
    string public name;
    string public symbol;
    uint8  public decimals;    
    
    constructor(
        address initialAccount,
        uint256 initialBalance, 
        string _name,
        string _symbol,
        uint8 _decimals)
        public
    {
        _mint(initialAccount, initialBalance);
        name = _name;
        symbol = _symbol;
        decimals = _decimals;
    }

    function mint(
        address account,
        uint256 amount)
        public 
    {
        _mint(account, amount);
    }
    
    function burn(
        address account,
        uint256 amount)
        public 
    {
        _burn(account, amount);
    }

    function burnFrom(
        address account,
        uint256 amount) 
        public 
    {
        _burnFrom(account, amount);
    }
}