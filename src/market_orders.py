import argparse
import logging
from binance.client import Client
from binance.enums import *

# Configure Logging
logging.basicConfig(filename='bot.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Initialize Binance Client (Use Testnet Keys for safety)
API_KEY = "YOUR_API_KEY"
API_SECRET = "YOUR_SECRET_KEY"
client = Client(API_KEY, API_SECRET, testnet=True)

def place_market_order(symbol, side, quantity):
    """Places a Market Order"""
    try:
        logging.info(f"Placing Market {side} Order: {symbol}, Qty: {quantity}")
        order = client.futures_create_order(
            symbol=symbol,
            side=SIDE_BUY if side.upper() == 'BUY' else SIDE_SELL,
            type=ORDER_TYPE_MARKET,
            quantity=quantity
        )
        logging.info(f"Market Order Successful: {order}")
        print("✅ Market Order placed successfully!")
    except Exception as e:
        logging.error(f"Error placing market order: {e}")
        print(f"❌ Failed: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Binance Market Order Bot")
    parser.add_argument("symbol", help="Trading symbol (e.g. BTCUSDT)")
    parser.add_argument("side", help="BUY or SELL")
    parser.add_argument("quantity", type=float, help="Order quantity")
    args = parser.parse_args()

    place_market_order(args.symbol, args.side, args.quantity)
