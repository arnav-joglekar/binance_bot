from src.limit_orders import place_limit_order
from src.client import BinanceClient
from src.logger import logger

def place_grid_orders(symbol, lower_price, upper_price, grid_levels, quantity_per_grid):
    try:
        client = BinanceClient().get_client()
        current_price = float(client.get_symbol_ticker(symbol=symbol)['price'])
        
        step = (upper_price - lower_price) / (grid_levels - 1)
        
        logger.info(f"Starting Grid Strategy for {symbol}: Range {lower_price}-{upper_price}, Levels {grid_levels}, Current Price {current_price}")
        
        for i in range(grid_levels):
            price = lower_price + (i * step)
            price = round(price, 2) # Adjust precision as needed
            
            if price < current_price:
                side = 'BUY'
            else:
                side = 'SELL'
                
            logger.info(f"Grid Level {i+1}: Placing {side} Limit at {price}")
            place_limit_order(symbol, side, quantity_per_grid, price)
            
    except Exception as e:
        logger.error(f"Grid Strategy Error: {e}")
