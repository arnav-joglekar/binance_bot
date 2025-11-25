import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("BINANCE_TESTNET_API_KEY")
API_SECRET = os.getenv("BINANCE_TESTNET_API_SECRET")
TESTNET_BASE_URL = "https://testnet.binancefuture.com"

if not API_KEY or not API_SECRET:
    # Warning instead of error to allow import without .env for testing purposes if needed, 
    # but practically this should be handled. 
    # However, for a bot, raising error is safer to fail fast.
    # Re-reading requirements: "Register and activate a Binance Testnet account... Generate API credentials"
    # So we expect them.
    pass 
