import argparse
import logging
import time
from binance.client import Client
from binance.enums import *

logging.basicConfig(filename='bot.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

API_KEY = "YOUR_API_KEY"
API_SECRET = "YOUR_SECRET_KEY"
client = Client(API_KEY, API_SECRET, testnet=True)

def execute_twap(symbol, side, total_quantity, parts, interval):
    """Executes a TWAP strategy"""
    chunk = total_quantity / parts
    logging.info(f"Starting TWAP {side} for {symbol}: Total={total_quantity}, Parts={parts}, Interval={interval}s")

    for i in range(parts):
        try:
            order = client.futures_create_order(
                symbol=symbol,
                side=SIDE_BUY if side.upper() == 'BUY' else SIDE_SELL,
                type=ORDER_TYPE_MARKET,
                quantity=chunk
            )
            logging.info(f"TWAP Chunk {i+1}/{parts} executed: {order}")
            print(f"✅ Executed chunk {i+1}/{parts}")
        except Exception as e:
            logging.error(f"TWAP Chunk {i+1} failed: {e}")
            print(f"❌ Chunk {i+1} failed: {e}")
        time.sleep(interval)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Binance TWAP Bot")
    parser.add_argument("symbol", help="Trading symbol (e.g. BTCUSDT)")
    parser.add_argument("side", help="BUY or SELL")
    parser.add_argument("total_quantity", type=float)
    parser.add_argument("parts", type=int)
    parser.add_argument("interval", type=int, help="Seconds between each order")
    args = parser.parse_args()

    execute_twap(args.symbol, args.side, args.total_quantity, args.parts, args.interval)
