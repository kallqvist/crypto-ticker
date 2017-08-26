from electrum.wallet import Wallet

class InMemoryWalletStorage(dict):
    def put(self, key, value, _save):
        self[key] = value

storage = InMemoryWalletStorage()
wallet = Wallet(storage)
# print(wallet)
wallet.synchronize()  # generates addresses up to the gap limit.
