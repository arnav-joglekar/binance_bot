import click
from src.market_orders import place_market_order
from src.limit_orders import place_limit_order
from src.advanced.stop_limit import place_stop_limit_order
from src.advanced.oco import place_oco_orders
from src.advanced.twap import execute_twap
from src.advanced.grid import place_grid_orders
from src.logger import logger

@click.group()
def cli():
    """Binance Futures Trading Bot CLI"""
    pass

@cli.command()
@click.option('--symbol', required=True, help='Trading pair symbol (e.g., BTCUSDT)')
@click.option('--side', required=True, type=click.Choice(['BUY', 'SELL'], case_sensitive=False), help='Order side')
@click.option('--quantity', required=True, type=float, help='Order quantity')
def market(symbol, side, quantity):
    """Place a Market Order"""
    place_market_order(symbol, side, quantity)

@cli.command()
@click.option('--symbol', required=True, help='Trading pair symbol')
@click.option('--side', required=True, type=click.Choice(['BUY', 'SELL'], case_sensitive=False), help='Order side')
@click.option('--quantity', required=True, type=float, help='Order quantity')
@click.option('--price', required=True, type=float, help='Limit price')
def limit(symbol, side, quantity, price):
    """Place a Limit Order"""
    place_limit_order(symbol, side, quantity, price)

@cli.command()
@click.option('--symbol', required=True, help='Trading pair symbol')
@click.option('--side', required=True, type=click.Choice(['BUY', 'SELL'], case_sensitive=False), help='Order side')
@click.option('--quantity', required=True, type=float, help='Order quantity')
@click.option('--price', required=True, type=float, help='Limit price')
@click.option('--stop-price', required=True, type=float, help='Stop trigger price')
def stop_limit(symbol, side, quantity, price, stop_price):
    """Place a Stop-Limit Order"""
    place_stop_limit_order(symbol, side, quantity, price, stop_price)

@cli.command()
@click.option('--symbol', required=True, help='Trading pair symbol')
@click.option('--side', required=True, type=click.Choice(['BUY', 'SELL'], case_sensitive=False), help='Order side (for the position to close)')
@click.option('--quantity', required=True, type=float, help='Order quantity (not used if closing position, but good for validation)')
@click.option('--stop-price', required=True, type=float, help='Stop Loss trigger price')
@click.option('--take-profit-price', required=True, type=float, help='Take Profit trigger price')
def oco(symbol, side, quantity, stop_price, take_profit_price):
    """Place OCO (TP/SL) Orders"""
    place_oco_orders(symbol, side, quantity, stop_price, take_profit_price)

@cli.command()
@click.option('--symbol', required=True, help='Trading pair symbol')
@click.option('--side', required=True, type=click.Choice(['BUY', 'SELL'], case_sensitive=False), help='Order side')
@click.option('--total-quantity', required=True, type=float, help='Total quantity to trade')
@click.option('--duration', required=True, type=int, help='Duration in minutes')
@click.option('--orders', required=True, type=int, help='Number of orders to split into')
def twap(symbol, side, total_quantity, duration, orders):
    """Execute TWAP Strategy"""
    execute_twap(symbol, side, total_quantity, duration, orders)

@cli.command()
@click.option('--symbol', required=True, help='Trading pair symbol')
@click.option('--lower-price', required=True, type=float, help='Lower price of the grid')
@click.option('--upper-price', required=True, type=float, help='Upper price of the grid')
@click.option('--levels', required=True, type=int, help='Number of grid levels')
@click.option('--quantity-per-grid', required=True, type=float, help='Quantity per grid order')
def grid(symbol, lower_price, upper_price, levels, quantity_per_grid):
    """Place Grid Orders"""
    place_grid_orders(symbol, lower_price, upper_price, levels, quantity_per_grid)

if __name__ == '__main__':
    cli()
