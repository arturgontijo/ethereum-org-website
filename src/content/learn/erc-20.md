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
# It will expose only the methods: balanceOf(address), decimals(), symbol() and totalSupply()
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
        'name': 'symbol',
        'outputs': [{'internalType': 'string', 'name': '', 'type': 'string'}],
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
symbol = dai_contract.functions.symbol().call()
decimals = dai_contract.functions.decimals().call()
totalSupply = dai_contract.functions.totalSupply().call() / 10**decimals
addr_balance = dai_contract.functions.balanceOf(acc_address).call() / 10**decimals

#  DAI
print("===== %s =====" % symbol)
print("Total Supply:", totalSupply)
print("Addr Balance:", addr_balance)

weth_contract = w3.eth.contract(address=w3.toChecksumAddress(weth_token_addr), abi=simplified_abi)
symbol = weth_contract.functions.symbol().call()
decimals = weth_contract.functions.decimals().call()
totalSupply = weth_contract.functions.totalSupply().call() / 10**decimals
addr_balance = weth_contract.functions.balanceOf(acc_address).call() / 10**decimals

#  WETH
print("===== %s =====" % symbol)
print("Total Supply:", totalSupply)
print("Addr Balance:", addr_balance)
```

### TODO: Is the following too heavy to be here? Maybe! =/

No let's dive into a more interesting usage of an ERC-20 Token Contract, it's time to send and receive them!

To do that we will use the Kovan Ethereum Testnet and the Infure API as a provider.

##### 1.  Get an Infura API Key (Project ID) [here](https://infura.io/register).

```python
INFURA_API_KEY = "<<32_LENGTH_KEY>>"

w3 = Web3(Web3.HTTPProvider("https://kovan.infura.io/v3/%s" % INFURA_API_KEY))

# Creating the first account, if you don't have one
acc_1 = w3.eth.account.create()
print("Addr: %s" % acc_1.address)
print(" PK : %s" % acc_1.privateKey.hex()) # You can Import this in your Metamask

# Creating the second account, if you don't have one
acc_2= w3.eth.account.create()
print("Addr: %s" % acc_2.address)
print(" PK : %s" % acc_2.privateKey.hex()) # You can Import this in your Metamask

print("Acc1 Kovan ETH: %f" % w3.fromWei(w3.eth.getBalance(acc_1.address), "ether"))
print("Acc2 Kovan ETH: %f" % w3.fromWei(w3.eth.getBalance(acc_2.address), "ether"))
```

##### 2.  Get a Kovan ETH [here](https://faucet.kovan.network/) for the first account.

```python
# Checking again your first account balance
print("Acc1 Kovan ETH: %f" % w3.fromWei(w3.eth.getBalance(acc_1.address), "ether"))
```

##### 3.  Set your Metamask to the Kovan Network (and import your first account there).
##### 4.  Use Uniswap to swap part of your ETH (eg. 0.1) to some DAI tokens [here](https://app.uniswap.org/#/swap).

```python
transfer_abi = [
    {
        'inputs': [{'internalType': 'address', 'name': 'recipient', 'type': 'address'}, 
                   {'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}], 
        'name': 'transfer',
        'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 
        'stateMutability': 'nonpayable', 'type': 'function'
    }
]

final_abi = simplified_abi + transfer_abi

dai_token_addr="0x4f96fe3b7a6cf9725f59d353f723c1bdb64ca6aa"  # DAI (Kovan)
dai_contract = w3.eth.contract(address=w3.toChecksumAddress(dai_token_addr), abi=final_abi)

symbol = dai_contract.functions.symbol().call()
decimals = dai_contract.functions.decimals().call()
addr_balance = dai_contract.functions.balanceOf(acc_1.address).call() / 10**decimals

print("Acc1 Kovan %s: %f" % (symbol, addr_balance))
print("Acc1 Kovan ETH: %f" % w3.fromWei(w3.eth.getBalance(acc_1.address), "ether"))

# Transferring 1 DAI from the first to the second account, but first we have to approve it:
transfer_method = dai_contract.functions.transfer(acc_2.address, 1*10**decimals)

txn = transfer_method.buildTransaction(
    {
        "from": acc_1.address,
        "nonce": w3.eth.getTransactionCount(acc_1.address),
        "gas": 500000,
        "chainId": int(w3.version.network)
    }
)

raw_transaction = w3.eth.account.signTransaction(txn, acc_1.privateKey).rawTransaction
txn_hash = w3.eth.sendRawTransaction(raw_transaction)
w3.eth.waitForTransactionReceipt(txn_hash)  # This can last few seconds or even minutes...

# You can inspect the transaction receipt
receipt = w3.eth.getTransactionReceipt(txn_hash)
print(receipt)

# Finally, let's check the second account DAI balance
acc2_balance = dai_contract.functions.balanceOf(acc_2.address).call() / 10**decimals
print("Acc1 Kovan %s: %f" % (symbol, acc2_balance))

# You can now exercise what you've learned by sending the 1 DAI back to the first account.
# Remember that you will need some Kovan ETH in your second account to pay the gas of the transaction.
```

### TODO: What about using an Interface to make things easier?

```python
class SimpleContractInterface:
    def __init__(self, w3, user_pk, contract_addr, contract_abi):
        self.w3 = w3
        self.account = self.w3.eth.account.privateKeyToAccount(user_pk)
        self.last_txn = ""
        self.gas = 500000
        self.contract = self.w3.eth.contract(address=self.w3.toChecksumAddress(contract_addr), abi=contract_abi)
        self.functions = self.contract.functions
        self.abi = contract_abi
    def _build_txn(self, method, *args):
        return getattr(self.functions, method)(*args).buildTransaction({
            "from": self.account.address,
            "nonce": self.w3.eth.getTransactionCount(self.account.address),
            "gas": self.gas,
            "chainId": int(self.w3.version.network)})
    def _sign_send_wait(self, txn):
        raw_txn = self.w3.eth.account.signTransaction(txn, self.account.privateKey).rawTransaction
        self.last_txn = self.w3.eth.sendRawTransaction(raw_txn)
        print("Transaction sent, please wait...")
        self.w3.eth.waitForTransactionReceipt(self.last_txn)
        print("Done!")
        return self.w3.eth.getTransactionReceipt(self.last_txn)
    def transact(self, method, *args):
        txn = self._build_txn(method, *args)
        return self._sign_send_wait(txn)
    def call(self, method, *args):
        return getattr(self.functions, method)(*args).call()


contract = SimpleContractInterface(w3, acc_1.privateKey, dai_token_addr, final_abi)

r = contract.transact("transfer", acc_2.address, 1 * (10**contract.call("decimals")))
contract.call("balanceOf", acc_2.address)
```

#### Web3.js Example

Let's now do the same thing we did before but using the Javascript's library 
[Web3.js](https://web3js.readthedocs.io/en/v1.2.11/getting-started.html#getting-started).

First make sure you have [Metamask](https://metamask.io/download.html) plugin installed in your Browser. 
Metamask injects an Ethereum Provider at `window.ethereum`.

```
var dai_token_addr="0x6B175474E89094C44Da98b954EedeAC495271d0F"     // DAI
var weth_token_addr="0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2"    // Wrapped Ether (WETH)

var acc_address="0xA478c2975Ab1Ea89e8196811F51A7B7Ade33eB11"        // Uniswap V2: DAI 2

// This is a simplified Contract Application Binary Interface (ABI) of an ERC-20 Token Contract.
// It will expose only the methods: balanceOf(address), decimals(), symbol() and totalSupply()
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
        'name': 'symbol',
        'outputs': [{'internalType': 'string', 'name': '', 'type': 'string'}],
        'stateMutability': 'view', 'type': 'function', 'constant': true
    }, 
    {
        'inputs': [], 
        'name': 'totalSupply', 
        'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 
        'stateMutability': 'view', 'type': 'function', 'constant': true
    }
]

async function inspectTokens() {
    var _web3;
    if(window.web3) { _web3 = window.web3; }
    else if (window.ethereum) { _web3 = new Web3(window.ethereum); };

    var printInfo;

    // Web3js >= 1.0.0
    if(_web3 && _web3.eth.Contract) {
        printInfo = async function printInfo(_abi, _add) {
            let _contract = new _web3.eth.Contract(_abi, _add);
            let symbol = await _contract.methods.symbol().call()
            let decimals = await _contract.methods.decimals().call()
            let total_supply = await _contract.methods.totalSupply().call()
            let balance = await _contract.methods.balanceOf(acc_address).call()
            console.log("===== " + symbol + " =====");
            console.log("Total Supply: " + total_supply / 10**decimals);
            console.log("Addr Balance: " + balance / 10**decimals);
        }
    }
    // Web3js < 1.0.0
    else if(_web3 && _web3.eth.contract) {
        printInfo = async function printInfo(_abi, _add) {
            let promise = new Promise((resolve, reject) => {
                let _contract = _web3.eth.contract(_abi).at(_add);
                _contract.symbol((err, s) => {
                    _contract.totalSupply((err, t) => {
                        _contract.decimals((err, d) => {
                            console.log("===== " + s + " =====");
                            console.log("Total Supply: " + t.div(10**d));
                            _contract.balanceOf(acc_address, (err, b) => {
                                console.log("Addr Balance: " + b.div(10**d));
                                resolve();
                            });
                        });
                    });
                });
            });
            await promise;
        }
    }

    if(printInfo) {
        // DAI
        await printInfo(simplified_abi, dai_token_addr);
        // WETH
        await printInfo(simplified_abi, weth_token_addr);
    }
}

await inspectTokens();
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

It's recommended to use a Testnet to deploy and test any contract before moving forward to the Mainnet. Just make sure that 
you have some ETH to pay the gas of the deployment transaction.

The contract above will create a new ERC-20 Token, called "MyToken", with a total supply of 100 HIX (its symbol).
The `_mint` function will set the balance of the `msg.sender` to the total supply. So anyone who deploys this contract 
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
