from src.client import BinanceClient
from src.logger import logger
from binance.exceptions import BinanceAPIException

def place_market_order(symbol, side, quantity):
    try:
        client = BinanceClient().get_client()
        logger.info(f"Placing MARKET {side} order for {quantity} {symbol}...")
        order = client.create_order(
            symbol=symbol,
            side=side.upper(),
            type='MARKET',
            quantity=quantity
        )
        logger.info(f"Order placed successfully: {order}")
        return order
    except BinanceAPIException as e:
        logger.error(f"Binance API Error: {e}")
        return None
    except Exception as e:
        logger.error(f"Unexpected Error: {e}")
        return None
