# Project Report

## Overview
This project implements a trading bot for **Binance Spot Testnet**. It supports core order types (Market, Limit) and advanced strategies (Stop-Limit, OCO, TWAP, Grid). It includes both a CLI and a modern Web UI.

## Features
- **Core**: Market and Limit orders with validation.
- **Advanced**:
    - **Stop-Limit**: Triggers a limit order when a stop price is reached.
    - **OCO**: Places Stop Loss and Take Profit orders simultaneously.
    - **TWAP**: Splits large orders over time to minimize market impact.
    - **Grid**: Places multiple limit orders across a price range.
- **Interface**:
    - **CLI**: Robust command-line interface.
    - **Web UI**: Flask-based web dashboard for easy trading.
- **Logging**: Comprehensive logging to `bot.log` and console.

## Architecture
- `src/client.py`: Singleton wrapper for Binance Client (configured for Spot Testnet).
- `src/market_orders.py` / `limit_orders.py`: Core logic.
- `src/advanced/`: Advanced strategy implementations.
- `main.py`: CLI entry point using `click`.
- `app.py`: Flask backend for the Web UI.
- `templates/` & `static/`: Frontend assets.

## Verification
The bot has been tested against the **Binance Spot Testnet**.
- API connection verified (using `testnet.binance.vision`).
- Order placement verified for all types (Market, Limit, OCO, Stop-Limit).
- Strategies verified (TWAP, Grid).
- Web UI verified.

## Future Improvements
- Add WebSocket support for real-time updates.
- Implement a full-fledged Grid Bot with running loop.
- Add unit tests.
