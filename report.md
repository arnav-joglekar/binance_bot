# Project Report

## Overview
This project implements a CLI trading bot for Binance Futures Testnet. It supports core order types (Market, Limit) and advanced strategies (Stop-Limit, OCO, TWAP, Grid).

## Features
- **Core**: Market and Limit orders with validation.
- **Advanced**:
    - **Stop-Limit**: Triggers a limit order when a stop price is reached.
    - **OCO**: Places Stop Loss and Take Profit orders simultaneously (using `reduceOnly` for position closing).
    - **TWAP**: Splits large orders over time to minimize market impact.
    - **Grid**: Places multiple limit orders across a price range.
- **Logging**: Comprehensive logging to `bot.log` and console.

## Architecture
- `src/client.py`: Singleton wrapper for Binance Client.
- `src/market_orders.py` / `limit_orders.py`: Core logic.
- `src/advanced/`: Advanced strategy implementations.
- `main.py`: CLI entry point using `click`.

## Verification
The bot has been tested against the Binance Futures Testnet.
- API connection verified.
- Order placement verified for all types.
- Error handling verified (invalid symbols, API errors).

## Future Improvements
- Add WebSocket support for real-time updates.
- Implement a full-fledged Grid Bot with running loop.
- Add unit tests.
