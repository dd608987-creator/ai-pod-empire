from web3 import Web3

class BlockchainLedger:
    def __init__(self, rpc_url="https://rpc.ankr.com/eth"):
        self.web3 = Web3(Web3.HTTPProvider(rpc_url))
        self.chain = []

    def record(self, event_type, data):
        """
        Records an event in the blockchain ledger (local simulation).
        """

        entry = {
            "event": event_type,
            "data": data
        }

        self.chain.append(entry)

        return {
            "status": "recorded",
            "event": event_type,
            "data": data
        }

    def get_chain(self):
        return self.chain
