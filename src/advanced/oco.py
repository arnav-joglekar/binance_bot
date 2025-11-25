from src.client import BinanceClient
from src.logger import logger
from binance.exceptions import BinanceAPIException

import requests
import time
import hmac
import hashlib
from urllib.parse import urlencode
from src.config import API_KEY, API_SECRET

def get_timestamp():
    return int(time.time() * 1000)

def sign(params):
    query_string = urlencode(params)
    signature = hmac.new(API_SECRET.encode('utf-8'), query_string.encode('utf-8'), hashlib.sha256).hexdigest()
    return signature

def place_oco_orders(symbol, side, quantity, stop_price, take_profit_price):
    """
    Places a One-Cancels-the-Other (OCO) strategy using raw API request
    to bypass python-binance issues with Spot Testnet.
    """
    try:
        # Determine base URL based on client config (assuming Testnet for now as per context)
        # Ideally we should get this from the client instance, but for this fix we'll use the known working URL
        base_url = 'https://testnet.binance.vision/api'
        endpoint = '/v3/order/oco'
        url = base_url + endpoint
        
        params = {
            'symbol': symbol,
            'side': side.upper(),
            'quantity': quantity,
            'price': take_profit_price,
            'stopPrice': stop_price,
            'stopLimitPrice': stop_price, # Optional but good practice for OCO
            'stopLimitTimeInForce': 'GTC',
            'timestamp': get_timestamp()
        }
        
        params['signature'] = sign(params)
        
        headers = {
            'X-MBX-APIKEY': API_KEY
        }
        
        logger.info(f"Placing OCO (TP/SL) orders for {symbol} {side} via Raw Request...")
        
        response = requests.post(url, headers=headers, params=params)
        
        if response.status_code == 200:
            order = response.json()
            logger.info(f"OCO Order placed successfully: {order}")
            return order, None
        else:
            logger.error(f"Binance API Error (Raw): {response.text}")
            return None, None
            
    except Exception as e:
        logger.error(f"Unexpected Error: {e}")
        return None, None
