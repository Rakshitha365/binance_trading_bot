from binance.client import Client
from binance.enums import (
    ORDER_TYPE_MARKET,
    ORDER_TYPE_LIMIT,
    TIME_IN_FORCE_GTC,
    SIDE_BUY,
    SIDE_SELL
)
from config import API_KEY, API_SECRET, BASE_URL
from logger import logger
import os


class BasicBot:
    def __init__(self, api_key=API_KEY, api_secret=API_SECRET, testnet=True):
        self.client = Client(api_key, api_secret)
        if testnet:
            self.client.FUTURES_URL = BASE_URL + "/fapi"
        if not os.getenv("TESTING"):
            try:
                self.client.ping()
                logger.info("Connected to Binance Futures Testnet")
            except Exception as e:
                logger.error(f"Connection error: {e}")
                raise

    def place_market_order(self, symbol, side, quantity):
        try:
            order = self.client.futures_create_order(
                symbol=symbol,
                side=SIDE_BUY if side.lower() == "buy" else SIDE_SELL,
                type=ORDER_TYPE_MARKET,
                quantity=quantity
            )
            logger.info(f"Market order placed: {order}")
            return order
        except Exception as e:
            logger.error(f"Market order error: {e}")
            raise

    def place_limit_order(self, symbol, side, quantity, price):
        try:
            order = self.client.futures_create_order(
                symbol=symbol,
                side=SIDE_BUY if side.lower() == "buy" else SIDE_SELL,
                type=ORDER_TYPE_LIMIT,
                quantity=quantity,
                price=str(price),
                timeInForce=TIME_IN_FORCE_GTC
            )
            logger.info(f"Limit order placed: {order}")
            return order
        except Exception as e:
            logger.error(f"Limit order error: {e}")
            raise

    def place_order(self, symbol, order_type, side, quantity, price=None):
        if order_type == "limit" and price is None:
            raise ValueError("Price must be specified for limit orders.")
        if order_type == "market":
            return self.place_market_order(symbol, side, quantity)
        elif order_type == "limit":
            return self.place_limit_order(symbol, side, quantity, price)
        else:
            raise ValueError("Unsupported order type.")