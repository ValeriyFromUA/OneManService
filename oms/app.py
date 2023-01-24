from flask import Flask, render_template, request
from .controllers import get_all_orders, find_orders_by_device_name, get_order_by_id

app = Flask(__name__)


@app.route('/')
@app.route('/orders', methods=['GET', 'POST'])
@app.route('/orders/<string:device>')
def orders(device=None):
    if request.method == 'GET':
        all_orders = get_all_orders() if device is None else find_orders_by_device_name(device)
        return render_template('orders.html', headr='Orders', data=all_orders)


