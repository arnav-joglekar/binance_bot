from flask import Flask, render_template, request, jsonify
from src.market_orders import place_market_order
from src.limit_orders import place_limit_order
from src.advanced.stop_limit import place_stop_limit_order
from src.advanced.oco import place_oco_orders
from src.advanced.twap import execute_twap
from src.advanced.grid import place_grid_orders
from src.logger import logger
import threading

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/market', methods=['POST'])
def market():
    data = request.json
    try:
        order = place_market_order(data['symbol'], data['side'], float(data['quantity']))
        if order:
            return jsonify({'status': 'success', 'order': order})
        else:
            return jsonify({'status': 'error', 'message': 'Order failed. Check logs.'}), 400
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

@app.route('/api/limit', methods=['POST'])
def limit():
    data = request.json
    try:
        order = place_limit_order(data['symbol'], data['side'], float(data['quantity']), float(data['price']))
        if order:
            return jsonify({'status': 'success', 'order': order})
        else:
            return jsonify({'status': 'error', 'message': 'Order failed. Check logs.'}), 400
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

@app.route('/api/oco', methods=['POST'])
def oco():
    data = request.json
    try:
        order, _ = place_oco_orders(
            data['symbol'], 
            data['side'], 
            float(data['quantity']), 
            float(data['stopPrice']), 
            float(data['takeProfitPrice'])
        )
        if order:
            return jsonify({'status': 'success', 'order': order})
        else:
            return jsonify({'status': 'error', 'message': 'Order failed. Check logs.'}), 400
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

@app.route('/api/stop-limit', methods=['POST'])
def stop_limit():
    data = request.json
    try:
        order = place_stop_limit_order(
            data['symbol'], 
            data['side'], 
            float(data['quantity']), 
            float(data['price']), 
            float(data['stopPrice'])
        )
        if order:
            return jsonify({'status': 'success', 'order': order})
        else:
            return jsonify({'status': 'error', 'message': 'Order failed. Check logs.'}), 400
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

@app.route('/api/twap', methods=['POST'])
def twap():
    data = request.json
    try:
        # Run TWAP in a separate thread to not block the response
        thread = threading.Thread(target=execute_twap, args=(
            data['symbol'], 
            data['side'], 
            float(data['totalQuantity']), 
            int(data['duration']), 
            int(data['orders'])
        ))
        thread.start()
        return jsonify({'status': 'success', 'message': 'TWAP started in background'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

@app.route('/api/grid', methods=['POST'])
def grid():
    data = request.json
    try:
        # Run Grid in a separate thread
        thread = threading.Thread(target=place_grid_orders, args=(
            data['symbol'], 
            float(data['lowerPrice']), 
            float(data['upperPrice']), 
            int(data['levels']), 
            float(data['quantityPerGrid'])
        ))
        thread.start()
        return jsonify({'status': 'success', 'message': 'Grid strategy started in background'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
