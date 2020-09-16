class SimpleContractInterface:
    def __init__(self, w3, user_pk, contract_addr, contract_abi):
        self.w3 = w3
        self.user_pk = self.w3.eth.account.privateKeyToAccount(user_pk).privateKey
        self.user_addr = self.w3.eth.account.privateKeyToAccount(user_pk).address
        self.address = self.w3.toChecksumAddress(contract_addr)
        self.last_txn = ""
        self.gas = 500000
        self.contract = self.w3.eth.contract(address=self.w3.toChecksumAddress(contract_addr), abi=contract_abi)
        self.functions = self.contract.functions
        self.abi = contract_abi
    def _build_txn(self, method, *args):
        return getattr(self.functions, method)(*args).buildTransaction({
            "from": self.user_addr,
            "nonce": self.w3.eth.getTransactionCount(self.user_addr),
            "gas": self.gas,
            "chainId": int(self.w3.version.network)})
    def _sign_send_wait(self, txn):
        raw_txn = self.w3.eth.account.signTransaction(txn, self.user_pk).rawTransaction
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


contract = SimpleContractInterface(w3, "0x0000000000000000000000000000000000000000000000000000000000000000", dai_token_addr, final_abi)

r = contract.transact("transfer", account_2.address, 1 * (10**contract.call("decimals")))
contract.call("balanceOf", account_2.address)
