from binance.client import Client
from binance.exceptions import BinanceAPIException
from .logging_config import setup_logger

logger = setup_logger(__name__)

class BinanceFuturesClient:
    def __init__(self, api_key: str, api_secret: str, testnet: bool = True):
        """Initialize Binance client for Futures Testnet."""
        self.api_key = api_key
        self.api_secret = api_secret
        self.testnet = testnet

        # For testnet, we need to set the base URL manually if using python-binance
        # python-binance supports testnet via Client(..., testnet=True) for spot, but for futures we need to use the futures testnet URL.
        # Actually, python-binance's Client does not directly support futures testnet with testnet=True.
        # We'll use the base URL approach.
        if testnet:
            self.base_url = "https://testnet.binancefuture.com"
        else:
            self.base_url = "https://fapi.binance.com"  # production futures

        # Initialize client with the base URL
        self.client = Client(api_key, api_secret, base_url=self.base_url)
        # For futures, we need to use the futures endpoints; the client handles it.

        logger.info(f"Binance Futures client initialized (testnet={testnet})")

    def place_order(self, symbol: str, side: str, order_type: str, quantity: float, price: float = None):
        """
        Place an order on Binance Futures.
        :param symbol: e.g., 'BTCUSDT'
        :param side: 'BUY' or 'SELL'
        :param order_type: 'MARKET' or 'LIMIT'
        :param quantity: float
        :param price: required for LIMIT orders
        :return: order response dictionary
        """
        try:
            # Map order_type to Binance format
            if order_type.upper() == 'MARKET':
                order = self.client.futures_create_order(
                    symbol=symbol,
                    side=side,
                    type='MARKET',
                    quantity=quantity
                )
            elif order_type.upper() == 'LIMIT':
                if price is None:
                    raise ValueError("Price is required for LIMIT orders")
                order = self.client.futures_create_order(
                    symbol=symbol,
                    side=side,
                    type='LIMIT',
                    quantity=quantity,
                    price=str(price),
                    timeInForce='GTC'  # Good till cancelled
                )
            else:
                raise ValueError(f"Unsupported order type: {order_type}")

            logger.info(f"Order placed successfully: {order}")
            return order
        except BinanceAPIException as e:
            logger.error(f"Binance API error: {e.message}")
            raise
        except Exception as e:
            logger.error(f"Unexpected error: {str(e)}")
            raise