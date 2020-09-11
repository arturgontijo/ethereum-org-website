# ERC-20 Token Standard (!!!DAFT!!!)

## Introduction

"A short intro that introduces the topic and explains what the user should learn by reading on"

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

"What should someone know before reading this page?"

- Accounts
- Smart Contracts
- Tokens

## Body

"The body is the main content on the page, it should explore the topic in detail and show plenty of examples (where appropriate)."

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

- TODO: What's an example?
- TODO: How can I use one in a dapp or smart contract?
- TODO: What's an example?

- TODO: (A-HA Moment) Stuff you can do with ERC-20 in DeFi, like interest earning...


## Further reading

"Is there some detail that you don't think is vital but some users may find interesting? Provide links here!"

- https://eips.ethereum.org/EIPS/eip-20
- https://docs.openzeppelin.com/contracts/3.x/tokens#ERC20
- https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/token/ERC20/ERC20.sol
- https://github.com/ConsenSys/Tokens/blob/master/contracts/eip20/EIP20.sol

## Related topics

- ERC721
- ERC777
- ERC1155