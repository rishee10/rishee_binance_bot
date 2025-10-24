import argparse
import logging
from binance.client import Client
from binance.enums import *

# Logging
logging.basicConfig(filename='bot.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

API_KEY = "YOUR_API_KEY"
API_SECRET = "YOUR_SECRET_KEY"
client = Client(API_KEY, API_SECRET, testnet=True)

def place_limit_order(symbol, side, quantity, price):
    """Places a Limit Order"""
    try:
        logging.info(f"Placing Limit {side} Order: {symbol}, Qty: {quantity}, Price: {price}")
        order = client.futures_create_order(
            symbol=symbol,
            side=SIDE_BUY if side.upper() == 'BUY' else SIDE_SELL,
            type=ORDER_TYPE_LIMIT,
            quantity=quantity,
            price=price,
            timeInForce=TIME_IN_FORCE_GTC
        )
        logging.info(f"Limit Order Successful: {order}")
        print("✅ Limit Order placed successfully!")
    except Exception as e:
        logging.error(f"Error placing limit order: {e}")
        print(f"❌ Failed: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Binance Limit Order Bot")
    parser.add_argument("symbol", help="Trading symbol (e.g. BTCUSDT)")
    parser.add_argument("side", help="BUY or SELL")
    parser.add_argument("quantity", type=float, help="Order quantity")
    parser.add_argument("price", type=float, help="Limit price")
    args = parser.parse_args()

    place_limit_order(args.symbol, args.side, args.quantity, args.price)
