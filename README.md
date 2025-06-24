# binance_trading_bot
A simplified Python trading bot built for the Binance USDT-M Futures Testnet. This bot allows you to place market and limit buy/sell orders securely using the Binance API.



# Features

- Place **Market** and **Limit** orders
- Support for both **Buy** and **Sell** order sides
- Connects to Binance **Futures Testnet**
- Command-line based user input
- **Logging** of API responses and errors
- Clean, modular codebase for easy extension
- Environment-based configuration management



# Prerequisites

- Python 3.7+
- Binance Futures Testnet Account  
    [Sign up here](https://testnet.binancefuture.com/en/futures/BTCUSDT)



# Installation

1. **Clone this repository** : 

    git clone https://github.com/your-username/binance_trading_bot.git

    cd binance_trading_bot

2. **Install Dependencies** : 

    pip install -r requirements.txt

3. **Configure your .env file** :

    Create a .env file in the root folder and add your Binance Testnet API keys:

    API_KEY=your_testnet_api_key

    API_SECRET=your_testnet_api_secret

    BASE_URL=https://testnet.binancefuture.com



# Usage

Run the bot using command line

python main.py


You’ll be prompted to enter:

- Trading symbol (e.g., BTCUSDT)
- Order type (market or limit)
- Order side (buy or sell)
- Quantity
- Limit price (if applicable)



# Logging 

All actions (connectivity, order placement, errors) are logged to:

logs/bot.log



# Tests

Unit tests are available in the tests/ folder. To run tests:

python -m unittest discover tests