import os
from web3 import Web3
from web3.middleware import (SignAndSendRawMiddlewareBuilder, ExtraDataToPOAMiddleware)
from dotenv import load_dotenv

from eth_account import Account
from eth_account.signers.local import LocalAccount

from contracts/slp_abi import slp_token_abi

load_dotenv()
privateKey = os.getenv("PRIVATE_KEY") #dev account

#ronin_rpc = "https://api.roninchain.com/rpc" #mainnet
ronin_rpc = "https://saigon-testnet.roninchain.com/rpc" #saigon

w3 = Web3(Web3.HTTPProvider(ronin_rpc))

assert privateKey is not None, "You must set PRIVATE_KEY environment variable"
assert privateKey.startswith("0x"), "Private key must start with 0x hex prefix"
account: LocalAccount = Account.from_key(privateKey)
w3.middleware_onion.inject(ExtraDataToPOAMiddleware, layer=0)
w3.middleware_onion.inject(SignAndSendRawMiddlewareBuilder.build(account), layer=0)


slpTokenAddress = '0xa8754b9fa15fc18bb59458815510e40a12cd2014'  #contract address SLP mainnet
axsTokenAddress = '0x97a9107c1793bc407d6f527b77e7fff4d812bece' #contract address AXS mainnet
usdcTokenAddress = '0x0b7007c13325c48911f73a2dad5fa5dcbf808adc'
wethTokenAddress = '0xc99a6a985ed2cac1ef41640596c5a5f9f4e19ef5'
kokuTokenAddress = '0x361d8623dc1d91e04ebc148687719aace282249a'
dhTokenAddress = '0x22c9f9616d1141a6be432151d31fab472e7b19f8'
drogTokenAddress = '0xce153b8cc253b3a3a84225fb4931a77ab4fbee45'

slpSaigonTokenAddress = '0x82f5483623d636bc3deba8ae67e1751b6cf2bad2' #Saigon SLP
axsSaigonTokenAddress = '0x3c4e17b9056272ce1b49f6900d8cfd6171a1869d' #Saigon AXS

abi = slp_token_abi

vault = '0xb6616e7c9B0dD989f5951f57c6E97ab6D0FeEe1c' #vault treasury
wiggly = '0xF57a14a0A2C9e1836f8CFC249516Ec2b01b80182' #wiggly
meme = '0x1A84B883fE03FD8b698DDb1D34238d89bed8F608' #meme
dev = '0x5886Dc1c4F14C5ab8e0E77eb50A3aFE4B0b06761'


address = slpSaigonTokenAddress


def showBalance(address,abi, wallet_address):
    checksumAddress = Web3.to_checksum_address(address)
    contract = w3.eth.contract(address=checksumAddress, abi=abi)

    balance = contract.functions.balanceOf(wallet_address).call()
    decimals = contract.functions.decimals().call()
    result = balance / 10**decimals
    print(f"Balance: {result}")
    return result

#showBalance(slpTokenAddress, abi, vault)


def send_token(_from=account.address, _to, amount):
    checksumAddress = Web3.to_checksum_address(slpSaigonTokenAddress)
    contract = w3.eth.contract(address=checksumAddress, abi=abi)
    converted_amount = w3.to_wei(amount, 'wei')
    tx_hash = contract.functions.transfer(_to, converted_amount).transact({'from': _from})
    tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    print(f"hash:{tx_hash}")
    print(f"Send: {amount} Tokens to {_to}")
    print("-"*50)



if __name__ == "__main__":
    print(f"Starting...")

    # payouts automatic
    # define amount SLP, AXS to send to another address
    # input amount, address (share -> amount, also totalshare needs to be 100%)


