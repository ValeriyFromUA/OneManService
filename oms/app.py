from flask import Flask, render_template, request
from .controllers import get_all_orders, get_order_by_id

app = Flask(__name__)


@app.route('/')
@app.route('/orders', methods=['GET', 'POST', 'DELETE', 'PUT'])
@app.route('/orders/<int:_id>')
def orders():
    all_orders = get_all_orders()
    return render_template('orders.html', headr='Orders', data=all_orders)
