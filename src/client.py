from binance.client import Client
from src.config import API_KEY, API_SECRET
from src.logger import logger

class BinanceClient:
    _instance = None

    def __new__(cls, testnet=True):
        if cls._instance is None:
            cls._instance = super(BinanceClient, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self, testnet=True):
        if self._initialized:
            return
            
        self.testnet = testnet
        if not API_KEY or not API_SECRET:
             logger.error("API credentials missing. Please check .env file.")
             raise ValueError("API credentials missing.")

        try:
            self.client = Client(API_KEY, API_SECRET, testnet=testnet)
            if testnet:
                self.client.API_URL = 'https://testnet.binance.vision/api'
            logger.info("Binance Client initialized successfully.")
            self._initialized = True
        except Exception as e:
            logger.error(f"Failed to initialize Binance Client: {e}")
            raise

    def get_client(self):
        return self.client
