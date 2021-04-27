#Coded by Om3gaOfficial

#Importing the needed liberies
import requests
import json


#BitPanda Documentation: "https://developers.bitpanda.com/platform/#bitpanda-public-api"
#URL to gernerate your Bitpanda API-Key: "https://web.bitpanda.com/apikey"

#BitPandaPro Documentation "https://developers.bitpanda.com/exchange/#bitpanda-pro-api"
#URL to gernerate your Bitpanda-Pro API-Key: "https://exchange.bitpanda.com/account/keys"


#The normal Bitpanda Api is in this class
class BitPanda:

    #Function to get all your trades of your Bitpanda-Account
    def getTrades(APIKey):
        response = requests.get('https://api.bitpanda.com/v1/trades', headers = {'X-API-KEY' : APIKey}).json()
        data = response['data']

        output = []
        for i in range(len(data)):
            output.append({'type': data[i]['attributes']['type'], 'id': data[i]['id'], 'cryptocoin_id': data[i]['attributes']['cryptocoin_id'], 'amount_fiat': data[i]['attributes']['amount_fiat'], 'amount_cryptocoin': data[i]['attributes']['amount_cryptocoin'], 'crypto_price': data[i]['attributes']['price'], 'crypto_wallet_id': data[i]['attributes']['wallet_id'], 'date': data[i]['attributes']['time']['date_iso8601']})
        return output

    #Function where all your crypto-wallet info will be returned | The "showAll" argument decides whether only the wallets with a 'balance > 0' are displayed 
    def getWallets(APIKey, showAll):
        response = requests.get('https://api.bitpanda.com/v1/wallets', headers = {'X-API-KEY' : APIKey}).json()
        data = response['data']

        output = []
        for i in range(len(data)):
            if showAll or float(data[i]['attributes']['balance']) != 0:
                output.append({'name': data[i]['attributes']['name'], 'id': data[i]['id'], 'cryptocoin_symbol': data[i]['attributes']['cryptocoin_symbol'], 'balance': data[i]['attributes']['balance']})
        return output

    #Function to get info about your fiat-wallets | The "showAll" argument decides whether only the wallets with a 'balance > 0' are displayed
    def getFiatWallets(APIKey, showAll):
        response = requests.get('https://api.bitpanda.com/v1/fiatwallets', headers = {'X-API-KEY' : APIKey}).json()
        data = response['data']

        output = []
        for i in range(len(data)):
            if showAll or float(data[i]['attributes']['balance']) != 0:
                output.append({'name': data[i]['attributes']['name'], 'id': data[i]['id'], 'fiat_symbol': data[i]['attributes']['fiat_symbol'], 'balance': data[i]['attributes']['balance']})
        return output


#Class where all Bitpanda-Pro requests are
class BitPandaPro:

    #Returing all currents crypto-prices
    def getCurrentPrices():
        response = requests.get('https://api.exchange.bitpanda.com/public/v1/market-ticker', headers = {'Accept': 'application/json'}).json()

        output = []
        for i in range(len(response)):
            output.append({'instrument_code': response[i]['instrument_code'], "state": response[i]['state'], "quote_volume": response[i]['quote_volume'], "base_volume": response[i]['base_volume'], "last_price": response[i]['last_price'], "high": response[i]['high'], "low": response[i]['low'], "price_change_percentage": response[i]['price_change_percentage']})
        return output

    #Getting the current price of a specific crypto-currency
    def getCurrentPrice(instrument_code):
        response = requests.get('https://api.exchange.bitpanda.com/public/v1/market-ticker/{instrument_code}', headers = {'Accept': 'application/json'}).json()

        try:
            if response['error']:
                return response

        except:
            output = []
            output.append({'instrument_code': response['instrument_code'], "state": response['state'], "quote_volume": response['quote_volume'], "base_volume": response['base_volume'], "last_price": response['last_price'], "high": response['high'], "low": response['low'], "price_change_percentage": response['price_change_percentage']})
            return output

