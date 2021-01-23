import json
import hashlib
import sys
from web3 import Web3, HTTPProvider, IPCProvider
from pprint import pprint

web3 = Web3 (HTTPProvider ("http://localhost:9545"))

with open ("abi.json") as f:
    abi = json.load (f)

if len (sys.argv) == 2:
    contract_address = sys.argv[1]
else:
    block_number = web3.eth.blockNumber
    contract_address = None
    while contract_address == None and block_number >= 0:
        block = web3.eth.getBlock (block_number)
        for tx_hash in block.transactions:
            tx = web3.eth.getTransactionReceipt (tx_hash)
            contract_address = tx.get ("contractAddress") 
            if contract_address != None:
                break
        block_number = block_number - 1
contract = web3.eth.contract (abi = abi, address = contract_address)
print ("Using contract address {:s}\n".format (contract_address))
