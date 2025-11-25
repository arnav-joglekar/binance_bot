# Binance Spot Testnet Trading Bot

A Python-based trading bot for the **Binance Spot Testnet**. It supports various order types and advanced trading strategies, and includes a modern Web UI.

## Features

- **Order Types**: Market, Limit, Stop-Limit, OCO (One-Cancels-the-Other).
- **Strategies**:
  - **TWAP (Time-Weighted Average Price)**: Execute large orders over time.
  - **Grid Trading**: Place a grid of buy/sell orders.
- **Interfaces**:
  - **CLI**: Command-line interface for quick execution.
  - **Web UI**: Modern Flask-based web interface.

## Prerequisites

1.  **Python 3.8+** installed.
2.  **Binance Spot Testnet Account**:
    - Go to [testnet.binance.vision](https://testnet.binance.vision/).
    - Login with your GitHub account.
    - Click **"Generate HMAC_SHA256 Key"**.
    - **Save your API Key and Secret immediately.**

## Installation

1.  Clone the repository:
    ```bash
    git clone https://github.com/arnav-joglekar/binance_bot.git
    cd binance_bot
    ```

2.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Configuration

1.  Create a `.env` file in the root directory:
    ```bash
    # Windows
    copy .env.example .env
    # Linux/Mac
    cp .env.example .env
    ```
    *(If `.env.example` doesn't exist, just create a new file named `.env`)*

2.  Add your API credentials to `.env`:
    ```env
    BINANCE_TESTNET_API_KEY=your_api_key_here
    BINANCE_TESTNET_API_SECRET=your_api_secret_here
    ```

## Usage

### Web Interface (Recommended)

1.  Start the Flask server:
    ```bash
    python app.py
    ```
2.  Open your browser and go to: **[http://127.0.0.1:5000](http://127.0.0.1:5000)**

### Command Line Interface (CLI)

You can also run the bot directly from the terminal.

**Market Order**
```bash
python main.py market --symbol BTCUSDT --side BUY --quantity 0.001
```

**Limit Order**
```bash
python main.py limit --symbol BTCUSDT --side SELL --quantity 0.001 --price 90000
```

**OCO Order (Take Profit / Stop Loss)**
```bash
python main.py oco --symbol BTCUSDT --side SELL --quantity 0.001 --take-profit-price 95000 --stop-price 85000
```

**Stop-Limit Order**
```bash
python main.py stop-limit --symbol BTCUSDT --side SELL --quantity 0.001 --price 84900 --stop-price 85000
```

**TWAP Strategy**
```bash
python main.py twap --symbol BTCUSDT --side BUY --total-quantity 0.01 --duration 5 --orders 5
```

**Grid Strategy**
```bash
python main.py grid --symbol BTCUSDT --lower-price 80000 --upper-price 90000 --levels 5 --quantity-per-grid 0.001
```

## Project Structure

- `main.py`: CLI entry point.
- `app.py`: Flask backend entry point.
- `src/`: Core trading logic and API wrappers.
- `templates/`: HTML templates for Web UI.
- `static/`: CSS and JS for Web UI.
- `bot.log`: Application logs.

