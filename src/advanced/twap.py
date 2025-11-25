import time
from src.market_orders import place_market_order
from src.logger import logger

def execute_twap(symbol, side, total_quantity, duration_minutes, num_orders):
    if num_orders <= 0:
        logger.error("Number of orders must be greater than 0")
        return

    interval = (duration_minutes * 60) / num_orders
    qty_per_order = round(total_quantity / num_orders, 3) # Rounding to 3 decimal places for safety
    
    logger.info(f"Starting TWAP: {total_quantity} {symbol} {side} over {duration_minutes} min in {num_orders} orders.")
    
    for i in range(num_orders):
        logger.info(f"TWAP Execution {i+1}/{num_orders}")
        place_market_order(symbol, side, qty_per_order)
        
        if i < num_orders - 1:
            logger.info(f"Waiting {interval} seconds...")
            time.sleep(interval)
    
    logger.info("TWAP Execution completed.")
