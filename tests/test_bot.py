import unittest
from unittest.mock import MagicMock, patch
from bot import BasicBot

@patch("bot.Client", autospec=True)
class TestTradingBot(unittest.TestCase):

    def setUp(self):
        self.api_key = "test_key"
        self.api_secret = "test_secret"

    def test_market_buy_order(self, MockClient):
        mock_client = MockClient.return_value
        mock_client.futures_create_order.return_value = {"status": "FILLED", "orderId": 1, "symbol": "BTCUSDT"}

        bot = BasicBot(self.api_key, self.api_secret)
        bot.client = mock_client
        order = bot.place_order("BTCUSDT", "market", "buy", 0.01)
        self.assertEqual(order["status"], "FILLED")

    def test_limit_sell_order(self, MockClient):
        mock_client = MockClient.return_value
        mock_client.futures_create_order.return_value = {"status": "NEW", "orderId": 2, "symbol": "BTCUSDT"}

        bot = BasicBot(self.api_key, self.api_secret)
        bot.client = mock_client
        order = bot.place_order("BTCUSDT", "limit", "sell", 0.01, 25000)
        self.assertEqual(order["status"], "NEW")

    def test_missing_price_for_limit(self, MockClient):
        bot = BasicBot(self.api_key, self.api_secret)
        with self.assertRaises(ValueError):
            bot.place_order("BTCUSDT", "limit", "buy", 0.01)

    def test_invalid_order_type(self, MockClient):
        bot = BasicBot(self.api_key, self.api_secret)
        with self.assertRaises(ValueError):
            bot.place_order("BTCUSDT", "invalid", "buy", 0.01)