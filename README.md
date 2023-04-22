![x](https://user-images.githubusercontent.com/68604388/233801368-78e070b1-6693-4c8d-aba6-e80c146c3436.PNG)
# Metamask mnemonic bruteforce in python
Test valid mnemonics according to the BIP32 standard and check if the corresponding public address has any transactions on the Ethereum, Binance and Polygon blockchains. If the wallet hasn't had any transactions on these chains, it adds it to empty.txt, if it did, it adds it to valid.txt.

# Instruction
- pip install requests
- pip install eth_account
- pip install mnemonic

On the brute.py file add your API Keys for Etherscan, Bscscan and Polyscan, also add your PATHs for empty.txt and valid.txt files. Then choose how many accounts you want to test for each mnemonic (1 recommended by default) and run brute.py. If the variable Multicore_Booster is set to True it will use all cores of your CPU to run faster.
