from binance.client import Client
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('BINANCE_TESTNET_API_KEY')
api_secret = os.getenv('BINANCE_TESTNET_API_SECRET')

print(f"API Key length: {len(api_key)}")
print(f"Secret length: {len(api_secret)}")

# Test connection to Futures Testnet
client = Client(api_key, api_secret, testnet=True)
try:
    # Try to get account info
    account = client.futures_account()
    print("✅ Connection successful!")
    print(f"Account balances: {account['totalWalletBalance']}")
except Exception as e:
    print(f"❌ Connection failed: {e}")
