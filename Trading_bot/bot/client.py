import os
from binance.client import Client
from binance.exceptions import BinanceAPIException

class BinanceFuturesClient:
    def __init__(self, api_key, api_secret, testnet=True):
        self.testnet = testnet
        base_url = 'https://testnet.binancefuture.com' if testnet else 'https://fapi.binance.com'
        self.client = Client(api_key, api_secret, testnet=True)
    
    def get_account(self):
        """Get futures account information."""
        try:
            return self.client.futures_account()
        except BinanceAPIException as e:
            raise Exception(f"API error: {e.message}")
    
    def get_ticker(self, symbol):
        """Get ticker price for symbol."""
        try:
            return self.client.futures_symbol_ticker(symbol=symbol)
        except BinanceAPIException as e:
            raise Exception(f"API error: {e.message}")
    
    def new_order(self, **kwargs):
        """Place new futures order."""
        try:
            return self.client.futures_create_order(**kwargs)
        except BinanceAPIException as e:
            raise Exception(f"API error: {e.message}")
