import requests

def eth_scan(_api, _address):

    api_key = _api

    address = _address

    url = f"https://api.etherscan.io/api?module=account&action=txlist&address={address}&apikey={api_key}"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if data["status"] == "1" and len(data["result"]) > 0:
            return True
        elif data["result"] == "Invalid API Key":
            print("INVALID ETH API KEY !!!")
        elif data["result"] == "Max rate limit reached, please use API Key for higher rate limit":
            print("ERROR: Max rate limit reached, please use API Key for higher rate limit. HOW TO SOLVE: Try to reduce the number of cores OR upgrade the API KEY calls per second. (Standard rate: 5 per second)")
        elif data["message"] == "NOTOK":
            print("Some errors on Etherscan. Message = 'NOTOK'")
        elif data["message"] == "NOTOK-Missing/Invalid API Key, rate limit of 1/5sec applied":
            print("Some errors on Etherscan. Message = 'NOTOK-Missing/Invalid API Key, rate limit of 1/5sec applied'")
        else:
            return False
    else:
        print("Request Error.")

def bsc_scan(_api, _address):

    api_key = _api

    address = _address

    url = f"https://api.bscscan.com/api?module=account&action=txlist&address={address}&apikey={api_key}"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if data["status"] == "1" and len(data["result"]) > 0:
            return True
        elif data["result"] == "Invalid API Key":
            print("INVALID BSC API KEY !!!")
        elif data["result"] == "Max rate limit reached, please use API Key for higher rate limit":
            print("ERROR: Max rate limit reached, please use API Key for higher rate limit. HOW TO SOLVE: Try to reduce the number of cores OR upgrade the API KEY calls per second. (Standard rate: 5 per second)")
        elif data["message"] == "NOTOK":
            print("Some errors on Bscscan. Message = 'NOTOK'")
        elif data["message"] == "NOTOK-Missing/Invalid API Key, rate limit of 1/5sec applied":
            print("Some errors on Bscscan. Message = 'NOTOK-Missing/Invalid API Key, rate limit of 1/5sec applied'")
        else:
            return False
    else:
        print("Request Error.")

def poly_scan(_api, _address):

    api_key = _api

    address = _address

    url = f"https://api.polygonscan.com/api?module=account&action=txlist&address={address}&apikey={api_key}"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if data["status"] == "1" and len(data["result"]) > 0:
            return True
        elif data["result"] == "Invalid API Key":
            print("INVALID POLY API KEY !!!")
        elif data["result"] == "Max rate limit reached, please use API Key for higher rate limit":
            print("ERROR: Max rate limit reached, please use API Key for higher rate limit. HOW TO SOLVE: Try to reduce the number of cores OR upgrade the API KEY calls per second. (Standard rate: 5 per second)")
        elif data["message"] == "NOTOK":
            print("Some errors on Polyscan. Message = 'NOTOK'")
        elif data["message"] == "NOTOK-Missing/Invalid API Key, rate limit of 1/5sec applied":
            print("Some errors on Polyscan. Message = 'NOTOK-Missing/Invalid API Key, rate limit of 1/5sec applied'")
        else:
            return False
    else:
        print("Request Error.")

def apto_scan(_address):

    address = _address

    url = f"https://api.aptoscan.com/api?module=account&action=totaltxsreceived&address={address}"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

    if response.status_code == 200:
        data = response.json()
        if data["status"] == "1" and len(data["result"]) > 0:
            return True
        elif data["result"] == "Invalid API Key":
            print("INVALID APTO API KEY !!!")
        elif data["result"] == "Max rate limit reached, please use API Key for higher rate limit":
            print("ERROR: Max rate limit reached, please use API Key for higher rate limit. HOW TO SOLVE: Try to reduce the number of cores OR upgrade the API KEY calls per second. (Standard rate: 5 per second)")
        elif data["message"] == "NOTOK":
            print("Some errors on Aptoscan. Message = 'NOTOK'")
        elif data["message"] == "NOTOK-Missing/Invalid API Key, rate limit of 1/5sec applied":
            print("Some errors on Aptoscan. Message = 'NOTOK-Missing/Invalid API Key, rate limit of 1/5sec applied'")
        else:
            return False
    else:
        print("Request Error.")

def cro_scan(_api, _address):

    api_key = _api

    address = _address

    url = f"https://api.cronoscan.com/api?module=account&action=txlist&address={address}&startblock=1&endblock=99999999&sort=asc&apikey={api_key}"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if data["status"] == "1" and len(data["result"]) > 0:
            return True
        elif data["result"] == "Invalid API Key":
            print("INVALID CRO API KEY !!!")
        elif data["result"] == "Max rate limit reached, please use API Key for higher rate limit":
            print("ERROR: Max rate limit reached, please use API Key for higher rate limit. HOW TO SOLVE: Try to reduce the number of cores OR upgrade the API KEY calls per second. (Standard rate: 5 per second)")
        elif data["message"] == "NOTOK":
            print("Some errors on Croscan. Message = 'NOTOK'")
        elif data["message"] == "NOTOK-Missing/Invalid API Key, rate limit of 1/5sec applied":
            print("Some errors on Croscan. Message = 'NOTOK-Missing/Invalid API Key, rate limit of 1/5sec applied'")
        else:
            return False
    else:
        print("Request Error.")

