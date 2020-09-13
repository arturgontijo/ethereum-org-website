# ERC-20 Token Standard (!!!DRAFT!!!)

## Introduction

What is a Token?

Tokens can virtually represent anything in Ethereum, from reputation points in an online platform, skills of a character 
in a game, lottery tickets till a financial asset bond to a real good like a share in a company, a fiat currency or a 
gold ounce, and so on! Such a powerful feature deserves and must be handled by a robust standard, right? That's exactly 
where the ERC-20 plays its role!

What is ERC-20?

The ERC-20 introduces a standard for Fungible Tokens, in other words, they have a property that makes each Token be exactly 
the same (in type and value) of another Token. For example, an ERC-20 Token acts just like the ETH, meaning that 1 Token 
is and will always be equal to all the other Tokens.

## Prerequisites

- Accounts
- Smart Contracts
- Tokens

## Body

The ERC-20 (Ethereum Request for Comments 20), proposed by Fabian Vogelsteller in November 2015, is a Token Standard that 
implements an API for tokens within Smart Contracts.

It provides functionalities like to transfer tokens from one account to another, to get the current token balance of an 
account and also the total supply of the token available on the network. Besides these it also has some other functionalities 
like to approve that an amount of token from an account can be spent by a third party account.

If a Smart Contract implements the following methods and events it can be called an ERC-20 Token Contract and, once deployed, it 
will be responsible to keep track of the created tokens on Ethereum.

From [EIP-20](https://eips.ethereum.org/EIPS/eip-20):

#### Methods:

```
# Returns the name of the token - e.g. "MyToken".
function name() public view returns (string)
```

```
# Returns the symbol of the token. E.g. “HIX”.
function symbol() public view returns (string)
```

```
# Returns the number of decimals the token uses - e.g. 8, means to divide the token amount by 100000000 to get its user representation.
function decimals() public view returns (uint8)
```

```
# Returns the total token supply.
function totalSupply() public view returns (uint256)
```

```
# Returns the account balance of another account with address _owner.
function balanceOf(address _owner) public view returns (uint256 balance)
```

```
# Transfers _value amount of tokens to address _to.
function transfer(address _to, uint256 _value) public returns (bool success)
```

```
# Transfers _value amount of tokens from address _from to address _to
function transferFrom(address _from, address _to, uint256 _value) public returns (bool success)
```

```
# Allows _spender to withdraw from your account multiple times, up to the _value amount.
function approve(address _spender, uint256 _value) public returns (bool success)
```

```
# Returns the amount which _spender is still allowed to withdraw from _owner.
function allowance(address _owner, address _spender) public view returns (uint256 remaining)
```

#### Events:
```
# MUST trigger when tokens are transferred, including zero value transfers.
event Transfer(address indexed _from, address indexed _to, uint256 _value)
```

```
# MUST trigger on any successful call to approve().
event Approval(address indexed _owner, address indexed _spender, uint256 _value)
```

### Examples

Let's see how a Standard is so important to make things simple for us to inspect any ERC-20 Token Contract on Ethereum. 
We just need the Contract Application Binary Interface (ABI) to instantiate an interface to any ERC-20 Token. As you can 
see below we will use a simplified ABI, to make it a low friction example.

#### Web3.py Example

First, make sure you have installed [Web3.py](https://web3py.readthedocs.io/en/stable/quickstart.html#installation) Python library:

```
$ pip install web3
```

```python
from web3 import Web3


w3 = Web3(Web3.HTTPProvider("https://cloudflare-eth.com"))

dai_token_addr="0x6B175474E89094C44Da98b954EedeAC495271d0F"     # DAI
weth_token_addr="0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2"    # Wrapped Ether (WETH)

acc_address="0xA478c2975Ab1Ea89e8196811F51A7B7Ade33eB11"        # Uniswap V2: DAI 2

# This is a simplified Contract Application Binary Interface (ABI) of an ERC-20 Token Contract.
# It will expose only the methods: balanceOf(address), decimals() and totalSupply()
simplified_abi = [
    {
        'inputs': [{'internalType': 'address', 'name': 'account', 'type': 'address'}], 
        'name': 'balanceOf', 
        'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 
        'stateMutability': 'view', 'type': 'function', 'constant': True
    }, 
    {
        'inputs': [], 
        'name': 'decimals', 
        'outputs': [{'internalType': 'uint8', 'name': '', 'type': 'uint8'}], 
        'stateMutability': 'view', 'type': 'function', 'constant': True
    }, 
    {
        'inputs': [], 
        'name': 'totalSupply', 
        'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 
        'stateMutability': 'view', 'type': 'function', 'constant': True
    }
]

dai_contract = w3.eth.contract(address=w3.toChecksumAddress(dai_token_addr), abi=simplified_abi)
decimals = dai_contract.functions.decimals().call()
totalSupply = dai_contract.functions.totalSupply().call() / 10**decimals
addr_balance = dai_contract.functions.balanceOf(acc_address).call() / 10**decimals

#  ===== DAI =====
print("Total Supply:", totalSupply)
print("Addr Balance:", addr_balance)

weth_contract = w3.eth.contract(address=w3.toChecksumAddress(weth_token_addr), abi=simplified_abi)
decimals = weth_contract.functions.decimals().call()
totalSupply = weth_contract.functions.totalSupply().call() / 10**decimals
addr_balance = weth_contract.functions.balanceOf(acc_address).call() / 10**decimals

#  ===== WETH =====
print("Total Supply:", totalSupply)
print("Addr Balance:", addr_balance)
```

#### Web3.js Example

Let's now do the same thing we did before but using Javascript.
First make sure you have [Metamask](https://metamask.io/download.html) plugin installed in your Browser.

```
dai_token_addr="0x6B175474E89094C44Da98b954EedeAC495271d0F"     // DAI
weth_token_addr="0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2"    // Wrapped Ether (WETH)

acc_address="0xA478c2975Ab1Ea89e8196811F51A7B7Ade33eB11"        // Uniswap V2: DAI 2

// This is a simplified Contract Application Binary Interface (ABI) of an ERC-20 Token Contract.
// It will expose only the methods: balanceOf(address), decimals() and totalSupply()
simplified_abi = [
    {
        'inputs': [{'internalType': 'address', 'name': 'account', 'type': 'address'}], 
        'name': 'balanceOf', 
        'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 
        'stateMutability': 'view', 'type': 'function', 'constant': true
    }, 
    {
        'inputs': [], 
        'name': 'decimals', 
        'outputs': [{'internalType': 'uint8', 'name': '', 'type': 'uint8'}], 
        'stateMutability': 'view', 'type': 'function', 'constant': true
    }, 
    {
        'inputs': [], 
        'name': 'totalSupply', 
        'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 
        'stateMutability': 'view', 'type': 'function', 'constant': true
    }
]

function totalSupply(_contract) {
  _contract.totalSupply((err, total) => {
    _contract.decimals((err, decimals) => {
      total = total.div(10**decimals);
      console.log(total.toString());
    });
  });
}

function balanceOf(_contract, _address) {
  _contract.balanceOf(_address, (err, balance) => {
    _contract.decimals((err, decimals) => {
      balance = balance.div(10**decimals);
      console.log(balance.toString());
    });
  });
}

// DAI
let dai_contract = web3.eth.contract(simplified_abi).at(dai_token_addr);
totalSupply(dai_contract)
balanceOf(dai_contract, acc_address)

// WETH
let weth_contract = web3.eth.contract(simplified_abi).at(weth_token_addr);
totalSupply(weth_contract)
balanceOf(weth_contract, acc_address)
```

#### Creating a Token

Let's create an ERC-20 Token using [Remix](https://remix.ethereum.org/) and the [OpenZeppelin's ERC-20](
https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/token/ERC20/ERC20.sol) implementation.

First, create a new file with this code (yeah, only that! The ERC20.sol will hold all the heavy code):

```
pragma solidity ^0.6.10;

import "http://github.com/OpenZeppelin/openzeppelin-solidity/contracts/token/ERC20/ERC20.sol";

contract UniAuctionToken is ERC20 {
    constructor() ERC20("MyToken", "HIX") public {
        _mint(msg.sender, 100);
    }
}
```

Its recommended to use a Testnet to deploy and test any contract before move forward to the Mainnet. Just make sure that 
you have some ETH to pay the gas of the deployment transaction.

The contract above will create a new ERC-20 Token, called "MyToken", with a total supply of 100 HIX (its symbol).
The `_mint` function will set the balance of the `msg.sender` to the total supply. So anyone how deploys this contract 
will receive all the tokens in their account.

As soon as the contact is deployed, you will be able to use the Remix interface to interact with it, to keep track of 
the accounts balances, just like we did in the previous examples.


- TODO: How can I use one in a dapp or smart contract?
- TODO: (A-HA Moment) Stuff you can do with ERC-20 in DeFi, like interest earning...


## Further reading

- https://eips.ethereum.org/EIPS/eip-20
- https://docs.openzeppelin.com/contracts/3.x/tokens#ERC20
- https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/token/ERC20/ERC20.sol
- https://github.com/ConsenSys/Tokens/blob/master/contracts/eip20/EIP20.sol

## Related topics

- ERC721
- ERC777
- ERC1155
