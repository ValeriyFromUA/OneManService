from typing import NoReturn

from db.db_engine import get_session
from db.fake_data_generator import generate_order_data, create_fake_customers, add_customer_to_order_id
from models import OrderModel, CustomerOrder, CustomerModel

session = get_session()
ORDER_DATA = generate_order_data()
CUSTOMERS_DATA = create_fake_customers()
ORDER_ID, CUSTOMER_ID = add_customer_to_order_id()


def add_orders_to_db() -> NoReturn:
    orders = []
    for data in ORDER_DATA:
        order = OrderModel(
            device=data['device'],
            serial_number=data['serial_number'],
            defect=data['defect'],
            shape=data['shape'],
            kit=data['kit'],
            diagnosis=data['diagnosis'],
            status=data['status']
        )
        orders.append(order)
    session.add_all(orders)
    session.commit()


def add_customers_to_db() -> NoReturn:
    customers = []
    for data in CUSTOMERS_DATA:
        customer = CustomerModel(
            first_name=data['first_name'],
            last_name=data['last_names'],
            phone=data['phone'],
            email=data['email'],
            address=data['address']
        )
        customers.append(customer)
    session.add_all(customers)
    session.commit()


def add_customers_to_orders() -> NoReturn:
    customer_and_orders_id = []
    for _ in range(len(ORDER_ID)):
        customer_order = CustomerOrder(
            order_id=ORDER_ID[_],
            customer_id=CUSTOMER_ID[_]
        )
        customer_and_orders_id.append(customer_order)
    session.add_all(customer_and_orders_id)
    session.commit()


def add_fake_data_to_db():
    add_orders_to_db()
    add_customers_to_db()
    add_customers_to_orders()
