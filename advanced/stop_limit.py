import argparse
import logging
from binance.client import Client
from binance.enums import *

logging.basicConfig(filename='bot.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

API_KEY = "YOUR_API_KEY"
API_SECRET = "YOUR_SECRET_KEY"
client = Client(API_KEY, API_SECRET, testnet=True)

def place_stop_limit(symbol, side, quantity, stop_price, limit_price):
    """Triggers a limit order when stop price is hit"""
    try:
        logging.info(f"Placing Stop-Limit {side} Order: {symbol}, Stop: {stop_price}, Limit: {limit_price}")
        order = client.futures_create_order(
            symbol=symbol,
            side=SIDE_BUY if side.upper() == 'BUY' else SIDE_SELL,
            type=ORDER_TYPE_STOP,
            quantity=quantity,
            stopPrice=stop_price,
            price=limit_price,
            timeInForce=TIME_IN_FORCE_GTC
        )
        logging.info(f"Stop-Limit Order Successful: {order}")
        print("✅ Stop-Limit Order placed successfully!")
    except Exception as e:
        logging.error(f"Error placing stop-limit order: {e}")
        print(f"❌ Failed: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Binance Stop-Limit Order Bot")
    parser.add_argument("symbol", help="Trading symbol (e.g. BTCUSDT)")
    parser.add_argument("side", help="BUY or SELL")
    parser.add_argument("quantity", type=float)
    parser.add_argument("stop_price", type=float)
    parser.add_argument("limit_price", type=float)
    args = parser.parse_args()

    place_stop_limit(args.symbol, args.side, args.quantity, args.stop_price, args.limit_price)
