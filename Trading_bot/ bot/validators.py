import re

def validate_symbol(symbol: str) -> bool:
    """Validate symbol format (e.g., BTCUSDT)."""
    # Basic check: alphanumeric, 6-10 chars
    return bool(re.match(r'^[A-Z0-9]{6,10}$', symbol))

def validate_quantity(quantity: float) -> bool:
    """Quantity must be positive."""
    return quantity > 0

def validate_price(price: float) -> bool:
    """Price must be positive."""
    return price > 0

def validate_side(side: str) -> bool:
    return side.upper() in ['BUY', 'SELL']

def validate_order_type(order_type: str) -> bool:
    return order_type.upper() in ['MARKET', 'LIMIT']