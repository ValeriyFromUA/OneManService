from random import choice
from typing import NoReturn

from db.db_engine import get_session
from db.fake_data_generator import generate_order_data, create_fake_customers, add_customer_to_order_id
from models import Order, Customer

session = get_session()
ORDER_DATA = generate_order_data()
CUSTOMERS_DATA = create_fake_customers()
ORDER_ID, CUSTOMER_ID = add_customer_to_order_id()


def add_orders_to_db() -> NoReturn:
    orders = []
    for data in ORDER_DATA:
        random_customer = 1
        order = Order(
            device=data['device'],
            serial_number=data['serial_number'],
            defect=data['defect'],
            shape=data['shape'],
            kit=data['kit'],
            diagnosis=data['diagnosis'],
            status=data['status'],
            customer_id=random_customer
        )
        random_customer += 1
        print(random_customer)
        orders.append(order)
    session.add_all(orders)
    session.commit()


def add_customers_to_db() -> NoReturn:
    customers = []
    for data in CUSTOMERS_DATA:
        customer = Customer(
            first_name=data['first_name'],
            last_name=data['last_names'],
            phone=data['phone'],
            email=data['email'],
            address=data['address']
        )
        customers.append(customer)
    session.add_all(customers)
    session.commit()


def add_fake_data_to_db():
    add_orders_to_db()
    add_customers_to_db()
