from backend.blockchain.block import Block

class Blockchain:
    """
    Blockchain: a public ledger of transactions.
    Implemented as a list of blocks - data sets of transactions
    """
    
    def __init__(self):
        self.chain = [Block.genesis()]

    def add_block(self, data):
        #last entry on the chain [-1]
        self.chain.append(Block.mine_block(self.chain[-1], data))

    def __repr__(self):
        return f'Blockchain: {self.chain}'
    
def main():
    blockchain = Blockchain()
    blockchain.add_block('one')
    blockchain.add_block('two')
    
    genesis_block = Block.genesis()
    block = Block.mine_block(genesis_block, 'foo')
    print(block)
    print(blockchain)

if __name__ == '__main__':
    main()


