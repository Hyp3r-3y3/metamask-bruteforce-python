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
        else:
            return False
    else:
        print("Request Error.")

