# 🪙 Binance Futures Order Bot


## 📘 Project Overview
This project is a **CLI-based Binance USDT-M Futures Trading Bot** built using Python.  
It supports **market**, **limit**, and advanced orders (**OCO**, **TWAP**) with proper **validation**, **error handling**, and **structured logging**.

---

## 🧩 Features

### Core Orders
| Order Type | Description | Example Command |
|------------|-------------|----------------|
| Market Order | Executes immediately at the best available price | `python src/market_orders.py BTCUSDT BUY 0.01` |
| Limit Order | Executes when the price reaches the specified level | `python src/limit_orders.py BTCUSDT SELL 0.01 68000` |

### Advanced Orders
| Order Type | Description | Example Command |
|------------|-------------|----------------|
| OCO (One Cancels Other) | Places take-profit and stop-loss simultaneously | `python src/advanced/oco.py BTCUSDT BUY 0.01 68500 66700` |
| TWAP (Time-Weighted Average Price) | Splits a large order into smaller chunks at intervals | `python src/advanced/twap.py BTCUSDT BUY 0.05 --interval 10` |

---

## ⚙️ Setup Instructions

### 1. Clone or Extract the Repository
```bash
git clone https://github.com/rishee10/rishee_binance_bot.git
cd rishee_binance_bot
```

Or extract your .zip file:

```
unzip rishee_binance_bot.zip

cd rishee_binance_bot
```

### 2. Create and Activate a Virtual Environment
```
python -m venv venv

venv\Scripts\activate   # Windows or

source venv/bin/activate   # macOS/Linux
```

### 3. Install Dependencies
```
pip install -r requirements.txt
```

### 4. Create a .env File or you can direct add in the main file also

```
BINANCE_API_KEY=your_api_key_here
BINANCE_SECRET_KEY=your_secret_key_here
```

### How to Run the Bot

All scripts are CLI-based and accept command-line arguments.

#### Market Orders
```
python src/market_orders.py <SYMBOL> <BUY/SELL> <QUANTITY>
```

#### Example:

```
python src/market_orders.py BTCUSDT BUY 0.01
```

#### Limit Orders
```
python src/limit_orders.py <SYMBOL> <BUY/SELL> <QUANTITY> <PRICE>
```
#### Example:
```
python src/limit_orders.py BTCUSDT SELL 0.01 68000
```

#### OCO Orders

```
python src/advanced/oco.py <SYMBOL> <BUY/SELL> <QUANTITY> <TAKE_PROFIT> <STOP_LOSS>
```
#### Example:
```
python src/advanced/oco.py BTCUSDT BUY 0.01 68500 66700
```

#### TWAP Strategy
```
python src/advanced/twap.py <SYMBOL> <BUY/SELL> <TOTAL_QTY> --interval <SECONDS>
```

#### Example:
```
python src/advanced/twap.py BTCUSDT BUY 0.05 --interval 10
```
