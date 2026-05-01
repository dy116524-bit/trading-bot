import logging
from binance.client import Client
from binance.exceptions import BinanceAPIException

logger = logging.getLogger("trading_bot")

class BinanceTestnetClient:
    def __init__(self, api_key: str, api_secret: str):
        self.client = Client(api_key, api_secret, testnet=True)
        # Force the base URL for Futures Testnet
        self.client.FUTURES_URL = 'https://testnet.binancefuture.com/fapi/v1'

    def place_futures_order(self, **params):
        try:
            logger.info(f"Sending order request: {params}")
            response = self.client.futures_create_order(**params)
            logger.info(f"Order successful: {response.get('orderId')}")
            return response
        except BinanceAPIException as e:
            logger.error(f"Binance API Error: {e.message} (Code: {e.code})")
            raise
        except Exception as e:
            logger.error(f"Unexpected error: {str(e)}")
            raise
