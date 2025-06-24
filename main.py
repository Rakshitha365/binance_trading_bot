from bot import BasicBot

def main():
    print("Welcome to Binance Futures Testnet Bot!")
    symbol = input("Enter symbol (e.g., BTCUSDT): ").upper()
    order_type = input("Order type (market/limit): ").lower()
    side = input("Order side (buy/sell): ").lower()
    quantity = float(input("Quantity: "))
    price = None

    if order_type == "limit":
        price = float(input("Price: "))

    bot = BasicBot()
    try:
        order = bot.place_order(symbol, order_type, side, quantity, price)
        print("\nOrder placed successfully!")
        print(f"Order ID: {order['orderId']}")
        print(f"Status: {order['status']}")
    except Exception as e:
        print(f"\nOrder failed: {e}")

if __name__ == "__main__":
    main()