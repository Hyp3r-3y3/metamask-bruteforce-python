![brute](https://user-images.githubusercontent.com/68604388/232552949-1bd03b4a-2392-4007-8dd0-568bac6ae21a.PNG)
# Metamask mnemonic bruteforce in python
Test valid mnemonics according to the BIP32 standard and check if the corresponding public address has any transactions on the Ethereum, Binance and Polygon blockchains. If the wallet hasn't had any transactions on these chains, it adds it to empty.txt, if it did, it adds it to valid.txt.

# Instruction
- pip install requests
- pip install eth_account
- pip install mnemonic

On the brute.py file add your API Keys for Etherscan, Bscscan and Polyscan, also add your PATHs for empty.txt and valid.txt files. Then choose how many accounts you want to test for each mnemonic (1 recommended by default) and run brute.py. If the variable Multicore_Booster is set to True it will use all cores of your CPU to run faster.
