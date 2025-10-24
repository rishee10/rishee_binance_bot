import argparse
import logging
from binance.client import Client

logging.basicConfig(filename='bot.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

API_KEY = "YOUR_API_KEY"
API_SECRET = "YOUR_SECRET_KEY"
client = Client(API_KEY, API_SECRET, testnet=True)

def place_oco_order(symbol, side, quantity, take_profit, stop_loss):
    """Places OCO order: take-profit + stop-loss"""
    try:
        logging.info(f"Placing OCO {side} Order: TP={take_profit}, SL={stop_loss}")
        order = client.create_oco_order(
            symbol=symbol,
            side=side.upper(),
            quantity=quantity,
            price=take_profit,
            stopPrice=stop_loss
        )
        logging.info(f"OCO Order Successful: {order}")
        print("✅ OCO order placed successfully!")
    except Exception as e:
        logging.error(f"Error placing OCO order: {e}")
        print(f"❌ Failed: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Binance OCO Order Bot")
    parser.add_argument("symbol", help="Trading symbol (e.g. BTCUSDT)")
    parser.add_argument("side", help="BUY or SELL")
    parser.add_argument("quantity", type=float)
    parser.add_argument("take_profit", type=float)
    parser.add_argument("stop_loss", type=float)
    args = parser.parse_args()

    place_oco_order(args.symbol, args.side, args.quantity, args.take_profit, args.stop_loss)
