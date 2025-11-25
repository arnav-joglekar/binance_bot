from src.client import BinanceClient
from src.logger import logger
from binance.exceptions import BinanceAPIException

def place_limit_order(symbol, side, quantity, price, time_in_force='GTC'):
    try:
        client = BinanceClient().get_client()
        logger.info(f"Placing LIMIT {side} order for {quantity} {symbol} at {price}...")
        order = client.create_order(
            symbol=symbol,
            side=side.upper(),
            type='LIMIT',
            timeInForce=time_in_force,
            quantity=quantity,
            price=price
        )
        logger.info(f"Order placed successfully: {order}")
        return order
    except BinanceAPIException as e:
        logger.error(f"Binance API Error: {e}")
        return None
    except Exception as e:
        logger.error(f"Unexpected Error: {e}")
        return None
