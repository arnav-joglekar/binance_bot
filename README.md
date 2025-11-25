# Binance Futures Trading Bot

A CLI-based trading bot for Binance Futures Testnet (USDT-M).

## Setup

1.  Clone the repository.
2.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3.  Create a `.env` file with your API credentials (see `.env.example`).
    ```
    BINANCE_TESTNET_API_KEY=your_key
    BINANCE_TESTNET_API_SECRET=your_secret
    ```

## Usage

### Market Order
```bash
python main.py market --symbol BTCUSDT --side BUY --quantity 0.001
```

### Limit Order
```bash
python main.py limit --symbol BTCUSDT --side SELL --quantity 0.001 --price 50000
```

### Stop-Limit Order
```bash
python main.py stop-limit --symbol BTCUSDT --side SELL --quantity 0.001 --price 49000 --stop-price 49500
```

### OCO (TP/SL)
```bash
python main.py oco --symbol BTCUSDT --side BUY --quantity 0.001 --stop-price 45000 --take-profit-price 55000
```

### TWAP Strategy
```bash
python main.py twap --symbol BTCUSDT --side BUY --total-quantity 0.01 --duration 5 --orders 5
```

### Grid Strategy
```bash
python main.py grid --symbol BTCUSDT --lower-price 40000 --upper-price 50000 --levels 5 --quantity-per-grid 0.001
```

## Logs
Logs are saved to `bot.log`.
