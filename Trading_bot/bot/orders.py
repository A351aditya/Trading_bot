import logging
from .client import BinanceFuturesClient
from .validators import validate_symbol, validate_quantity, validate_price

logger = logging.getLogger(__name__)

class OrderManager:
    def __init__(self, client: BinanceFuturesClient):
        self.client = client
    
    def place_order(self, symbol, side, order_type, quantity, price=None):
        """Place futures order with validation."""
        logger.info(f"Placing {order_type} {side} order for {symbol}: qty={quantity}, price={price}")
        
        # Validate inputs
        validate_symbol(symbol)
        validate_quantity(symbol, quantity)
        if order_type == 'LIMIT':
            if price is None:
                raise ValueError("Price required for LIMIT orders")
            validate_price(symbol, price)
        
        # Prepare order params
        order_params = {
            'symbol': symbol,
            'side': side,
            'type': order_type,
            'quantity': quantity,
        }
        if price:
            order_params['price'] = price
            order_params['timeInForce'] = 'GTC'
        
        # Place order
        try:
            order = self.client.new_order(**order_params)
            logger.info(f"Order placed successfully: {order['orderId']}")
            return order
        except Exception as e:
            logger.error(f"Order failed: {str(e)}")
            raise
