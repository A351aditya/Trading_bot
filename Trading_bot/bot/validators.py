import re
from binance.client import Client

# Exchange info cache
_exchange_info = None

def get_exchange_info(client):
    """Get exchange info for symbol validation."""
    global _exchange_info
    if _exchange_info is None:
        _exchange_info = client.client.futures_exchange_info()
    return _exchange_info

def validate_symbol(symbol):
    """Validate trading symbol format (e.g., BTCUSDT)."""
    if not re.match(r'^[A-Z0-9]+USDT$', symbol):
        raise ValueError(f"Invalid symbol format: {symbol}. Use e.g., BTCUSDT")
    
    # Check if symbol exists
    # Note: Full validation requires client and API call
    common_symbols = ['BTCUSDT', 'ETHUSDT', 'ADAUSDT', 'BNBUSDT']
    if symbol not in common_symbols:
        print(f"Warning: {symbol} might not be available. Check testnet symbols.")

def validate_quantity(symbol, quantity):
    """Validate quantity (min 0.001, positive float)."""
    if quantity <= 0:
        raise ValueError("Quantity must be positive")
    if quantity < 0.001:
        raise ValueError("Minimum quantity is 0.001")

def validate_price(symbol, price):
    """Validate price (positive float > 0)."""
    if price <= 0:
        raise ValueError("Price must be positive")
