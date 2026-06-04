import json
from web3 import Web3

# Kết nối Ganache
GANACHE_URL = "http://127.0.0.1:7545"
w3 = Web3(Web3.HTTPProvider(GANACHE_URL))

print("Connected:", w3.is_connected())

CONTRACT_ADDRESS = "0xeA9E52f0CC2a589F1EB0487C569574f9Fc2A3a8C"
print("CODE AT ADDRESS:", w3.eth.get_code(CONTRACT_ADDRESS))

with open("abi/contract_abi.json", "r") as f:
    abi = json.load(f)

contract = w3.eth.contract(
    address=CONTRACT_ADDRESS,
    abi=abi
)

account = w3.eth.accounts[0]


# ======================
# FIX: chuẩn hóa KEY blockchain
# ======================
def build_key(student_code, subject, semester):
    return f"{student_code}|{subject}|{semester}"


def add_score_hash(key, hash_value):
    tx = contract.functions.addScoreHash(
        key,
        hash_value
    ).transact({
        "from": account
    })

    receipt = w3.eth.wait_for_transaction_receipt(tx)
    return receipt


def get_score_hash(key):
    return contract.functions.getScoreHash(key).call()