#Coded by Om3gaOfficial

#Importing the needed liberies
import requests
import json


#BitPanda Documentation: "https://developers.bitpanda.com/platform/#bitpanda-public-api"
#URL to generate your Bitpanda API-Key: "https://web.bitpanda.com/apikey"

#BitPandaPro Documentation "https://developers.bitpanda.com/exchange/#bitpanda-pro-api"
#URL to generate your Bitpanda-Pro API-Key: "https://exchange.bitpanda.com/account/keys"


#The normal Bitpanda API is in this class
class BitPandaClass:

    #Function to get all your trades of your Bitpanda-Account | The "APIKey" argument is required
    def getTrades(APIKey):
        response = requests.get('https://api.bitpanda.com/v1/trades', headers = {'X-API-KEY' : APIKey}).json()
        
        try:
            data = response['data']
            output = []
            for i in range(len(data)):
                output.append({'type': data[i]['attributes']['type'], 'id': data[i]['id'], 'cryptocoin_id': data[i]['attributes']['cryptocoin_id'], 'amount_fiat': data[i]['attributes']['amount_fiat'], 'amount_cryptocoin': data[i]['attributes']['amount_cryptocoin'], 'crypto_price': data[i]['attributes']['price'], 'crypto_wallet_id': data[i]['attributes']['wallet_id'], 'date': data[i]['attributes']['time']['date_iso8601']})
            return output

        except:
            return response

    #Function where all your crypto-wallet info will be returned | The "APIKey" and the "showAll" arguments are required and the "showAll" argument decides whether only the wallets with a 'balance > 0' are displayed
    def getWallets(APIKey, showAll):
        response = requests.get('https://api.bitpanda.com/v1/wallets', headers = {'X-API-KEY' : APIKey}).json()

        try:
            data = response['data']
            output = []
            for i in range(len(data)):
                if showAll or float(data[i]['attributes']['balance']) != 0:
                    output.append({'name': data[i]['attributes']['name'], 'id': data[i]['id'], 'cryptocoin_symbol': data[i]['attributes']['cryptocoin_symbol'], 'balance': data[i]['attributes']['balance']})
            return output

        except:
            return response

    #Function to get info about your fiat-wallets | The "APIKey" and the "showAll" arguments are required and the "showAll" argument decides whether only the wallets with a 'balance > 0' are displayed
    def getFiatWallets(APIKey, showAll):
        response = requests.get('https://api.bitpanda.com/v1/fiatwallets', headers = {'X-API-KEY' : APIKey}).json()

        try:
            data = response['data']
            output = []
            for i in range(len(data)):
                if showAll or float(data[i]['attributes']['balance']) != 0:
                    output.append({'name': data[i]['attributes']['name'], 'id': data[i]['id'], 'fiat_symbol': data[i]['attributes']['fiat_symbol'], 'balance': data[i]['attributes']['balance']})
            return output

        except:
            return response


#Class where all Bitpanda-Pro requests are in
class BitPandaProClass:

    #Returing all currents crypto-prices | No arguments are required
    def getCurrentPrices():
        response = requests.get('https://api.exchange.bitpanda.com/public/v1/market-ticker', headers = {'Accept': 'application/json'}).json()

        try:
            output = []
            for i in range(len(response)):
                output.append({'instrument_code': response[i]['instrument_code'], "state": response[i]['state'], "quote_volume": response[i]['quote_volume'], "base_volume": response[i]['base_volume'], "last_price": response[i]['last_price'], "high": response[i]['high'], "low": response[i]['low'], "price_change_percentage": response[i]['price_change_percentage']})
            return output

        except:
            return response

    #Getting the current price of a specific crypto-currency | The "instrument_code" arguments is requiert and you must input a valid crypto-currency-symbol
    def getCurrentPrice(instrument_code):
        response = requests.get('https://api.exchange.bitpanda.com/public/v1/market-ticker/{instrument_code}', headers = {'Accept': 'application/json'}).json()

        try:
            if response['error']:
                return response

        except:
            output = []
            output.append({'instrument_code': response['instrument_code'], "state": response['state'], "quote_volume": response['quote_volume'], "base_volume": response['base_volume'], "last_price": response['last_price'], "high": response['high'], "low": response['low'], "price_change_percentage": response['price_change_percentage']})
            return output

