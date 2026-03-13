
import argparse
import os
import sys
from dotenv import load_dotenv

from bot.client import BinanceFuturesClient
from bot.orders import OrderManager
from bot.logging_config import setup_logger

# Load environment variables from .env file
load_dotenv()

logger = setup_logger("cli")


def parse_arguments():
    parser = argparse.ArgumentParser(description='Binance Futures Trading Bot CLI')
    parser.add_argument('--symbol', required=True, help='Trading pair symbol (e.g., BTCUSDT)')
    parser.add_argument('--side', required=True, choices=['BUY', 'SELL'], help='Order side')
    parser.add_argument('--type', required=True, choices=['MARKET', 'LIMIT'], dest='order_type', help='Order type')
    parser.add_argument('--quantity', required=True, type=float, help='Order quantity')
    parser.add_argument('--price', type=float, help='Price for LIMIT orders')
    args = parser.parse_args()
    
    if args.order_type == 'LIMIT' and args.price is None:
        parser.error('--price is required for LIMIT orders')
    return args

def main():
    args = parse_arguments()

    # Get API credentials from environment variables
    api_key = os.getenv('BINANCE_TESTNET_API_KEY')
    api_secret = os.getenv('BINANCE_TESTNET_API_SECRET')
    if not api_key or not api_secret:
        logger.error("API credentials not found. Please set BINANCE_TESTNET_API_KEY and BINANCE_TESTNET_API_SECRET in .env file.")
        sys.exit(1)

    # Initialize client and order manager
    try:
        client = BinanceFuturesClient(api_key, api_secret, testnet=True)
        manager = OrderManager(client)
    except Exception as e:
        logger.error(f"Failed to initialize client: {e}")
        sys.exit(1)

    # Place order
    try:
        response = manager.place_order(
            symbol=args.symbol,
            side=args.side,
            order_type=args.order_type,
            quantity=args.quantity,
            price=args.price
        )
        # Print clear output
        print("\n=== ORDER PLACED SUCCESSFULLY ===")
        print(f"Order ID: {response['orderId']}")
        print(f"Symbol: {response['symbol']}")
        print(f"Side: {response['side']}")
        print(f"Type: {response['type']}")
        print(f"Quantity: {response['origQty']}")
        print(f"Executed Quantity: {response.get('executedQty', 'N/A')}")
        print(f"Price: {response.get('price', 'N/A')}")
        print(f"Status: {response['status']}")
        if 'avgPrice' in response:
            print(f"Average Price: {response['avgPrice']}")
        print("==================================\n")
    except ValueError as e:
        logger.error(f"Validation error: {e}")
        sys.exit(1)
    except Exception as e:
        logger.error(f"Order failed: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()