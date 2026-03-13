from .client import BinanceFuturesClient
import validators
from .logging_config import setup_logger

logger = setup_logger(__name__)

class OrderManager:
    def __init__(self, client: BinanceFuturesClient):
        self.client = client

    def place_order(self, symbol: str, side: str, order_type: str, quantity: float, price: float = None):
        """
        Validate inputs and place order.
        Returns order response.
        """
        # --- Input validation ---
        if not validators.validate_symbol(symbol):
            raise ValueError(f"Invalid symbol: {symbol}")
        if not validators.validate_side(side):
            raise ValueError(f"Invalid side: {side}. Must be BUY or SELL.")
        if not validators.validate_order_type(order_type):
            raise ValueError(f"Invalid order type: {order_type}. Must be MARKET or LIMIT.")
        if not validators.validate_quantity(quantity):
            raise ValueError(f"Quantity must be positive: {quantity}")
        if order_type.upper() == 'LIMIT' and not validators.validate_price(price):
            raise ValueError(f"Price must be positive for LIMIT orders: {price}")

        # Log request summary
        logger.info(f"Placing order: symbol={symbol}, side={side}, type={order_type}, qty={quantity}, price={price}")

        # Call client
        response = self.client.place_order(symbol, side.upper(), order_type.upper(), quantity, price)

        # Log response details
        logger.info(f"Order response: {response}")
        return response