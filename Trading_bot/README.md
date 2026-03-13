# Binance Futures Trading Bot (Testnet) ✅ FIXED

A simple Python CLI application to place MARKET and LIMIT orders on Binance Futures Testnet.

## Features ✅
- Place MARKET and LIMIT orders (BUY/SELL) on Binance Futures Testnet.
- Command-line interface with argument parsing.
- Input validation for symbol, side, quantity, and price.
- Comprehensive logging to file and console.
- Error handling for API errors, network issues, and invalid inputs.

## Quick Start ✅

### 1. Prerequisites
- Python 3.7+
- Binance Futures Testnet account: [https://testnet.binancefuture.com](https://testnet.binancefuture.com)

### 2. Installation & Setup
```bash
cd Trading_bot
pip install -r requirements.txt
cp .env.example .env
# Edit .env with your Testnet API keys (Futures permissions required)
```

### 3. Test CLI
```bash
python cli.py --help
```

### 4. Place Test Order (MARKET)
```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

### 5. Place LIMIT Order
```bash
python cli.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.001 --price 60000
```

## API Keys Setup
1. Login to [Binance Testnet](https://testnet.binancefuture.com)
2. Go to Account > API Management
3. Create API with **Futures** permissions
4. Add to `.env`:
```
BINANCE_TESTNET_API_KEY=your_key
BINANCE_TESTNET_API_SECRET=your_secret
```

## Usage Examples ✅
```
# Market Buy
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001

# Limit Sell  
python cli.py --symbol ETHUSDT --side SELL --type LIMIT --quantity 0.01 --price 3000

# Help
python cli.py --help
```

## Logs
Check `logs/` directory for detailed logs with timestamps.

## Troubleshooting
- **ModuleNotFoundError**: Run `pip install -r requirements.txt`
- **SyntaxError**: All fixed ✅
- **API credentials**: Verify `.env` keys have Futures permissions
- **Invalid symbol**: Use BTCUSDT, ETHUSDT, etc.
- **Margin issues**: Use small quantities on testnet
