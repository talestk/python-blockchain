import pytest

from backend.blockchain.blockchain import Blockchain
from backend.blockchain.block import GENESIS_DATA

def test_blockchain_instance():
    blockchain = Blockchain()

    assert blockchain.chain[0].hash == GENESIS_DATA['hash']

def test_add_block():
    blockchain = Blockchain()
    data = 'test-data'
    blockchain.add_block(data)

    # assert that the last added data to the chain matches {data}
    assert blockchain.chain[-1].data == data

@pytest.fixture
def block_chain_three_blocks():
    blockchain = Blockchain()
    
    for i in range(3):
        blockchain.add_block(i)
    
    return blockchain

def test_is_valid_chain(block_chain_three_blocks):
    Blockchain.is_valid_chain(block_chain_three_blocks.chain)

def test_is_valid_chain_bad_genesis(block_chain_three_blocks):
    block_chain_three_blocks.chain[0].hash = 'evil _hash'

    with pytest.raises(Exception, match='genesis block must be valid'):
        Blockchain.is_valid_chain(block_chain_three_blocks.chain)

def test_replace_chain(block_chain_three_blocks):
    blockchain = Blockchain()
    blockchain.replace_chain(block_chain_three_blocks.chain)

    assert blockchain.chain == block_chain_three_blocks.chain

def test_replace_chain_not_longer(block_chain_three_blocks):
    blockchain = Blockchain()

    with pytest.raises(Exception, match='The incoming chain must be longer'):
        block_chain_three_blocks.replace_chain(blockchain.chain)

def est_replace_chain_bad_chain(block_chain_three_blocks):
    blockchain = Blockchain()
    block_chain_three_blocks[1].hash = 'evil_hash'

    with pytest.raises(Exception, match='The incoming chain is invalid'):
        blockchain.replace_chain(block_chain_three_blocks.chain)