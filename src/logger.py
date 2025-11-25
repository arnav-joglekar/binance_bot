import logging
import os

def setup_logger(name="binance_bot", log_file="bot.log", level=logging.INFO):
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    
    # Ensure log file is in the project root if not specified otherwise
    # If log_file is just a filename, it will be in CWD. 
    # The requirement says "Log all actions... in a structured log file."
    
    handler = logging.FileHandler(log_file)
    handler.setFormatter(formatter)
    
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    
    logger = logging.getLogger(name)
    logger.setLevel(level)
    
    # Avoid adding handlers multiple times if logger is reused
    if not logger.handlers:
        logger.addHandler(handler)
        logger.addHandler(console_handler)
    
    return logger

logger = setup_logger()
