import json, time, requests
from web3 import Web3

# === CONFIG ===
RPC = "https://mainnet.infura.io/v3/YOUR_INFURA_KEY"
PRIVATE_KEY = "YOUR_PRIVATE_KEY"
WALLET = "YOUR_WALLET"
TOKEN = "PASTE_TOKEN_ADDRESS"
BUY_ETH = 0.05
SLIPPAGE = 15
TARGET_X = 3

w3 = Web3(Web3.HTTPProvider(RPC))
ROUTER = "0x5C69bEe701ef814a2B6a3EDD4B1652CB9cc5aA6f"
WETH = "0xC02aaA39b223FE8D0A0E5C4F27eAD9083C756Cc2"

def buy():
    router = w3.eth.contract(address=w3.toChecksumAddress(ROUTER), abi=json.loads(requests.get(
        f"https://api.etherscan.io/api?module=contract&action=getabi&address={ROUTER}").json()["result"]))
    path = [Web3.toChecksumAddress(WETH), Web3.toChecksumAddress(TOKEN)]
    tx = router.functions.swapExactETHForTokensSupportingFeeOnTransferTokens(
        0, path, WALLET, int(time.time()) + 10000
    ).buildTransaction({
        'from': WALLET,
        'value': w3.toWei(BUY_ETH, 'ether'),
        'gas': 300000,
        'gasPrice': w3.toWei('40', 'gwei'),
        'nonce': w3.eth.getTransactionCount(WALLET)
    })
    signed = w3.eth.account.sign_transaction(tx, PRIVATE_KEY)
    tx_hash = w3.eth.sendRawTransaction(signed.rawTransaction)
    print(f"TX sent: https://etherscan.io/tx/{tx_hash.hex()}")

def monitor():
    print("Watching price to 3x... (mock)")
    time.sleep(20)
    print("Sell triggered")

buy()
monitor()
