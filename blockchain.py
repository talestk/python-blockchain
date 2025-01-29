class Block:
    """
    Block: a unit of storage
    Store transactions in a blockchain that supports a crypto currency.
    """
    def __init__(self, data):
        self.data = data

class Blockchain:
    """
    Blockchain: a public ledger of transactions.
    Implemented as a list of blocks - data sets of transactions
    """
    
    def __init__(self):
        self.chain = []

