from typing import NoReturn

from db.db_engine import get_session
from db.fake_data_generator import (generate_order_data, create_fake_customers,
                                    create_fake_comments)
from models import Order, Customer, Comment
from oms.logger import get_logger

logger = get_logger(__name__)
session = get_session()
ORDER_DATA = generate_order_data()
CUSTOMERS_DATA = create_fake_customers()
COMMENTS_DATA = create_fake_comments()


def add_orders_to_db() -> NoReturn:
    orders = []
    random_customer = 1
    for data in ORDER_DATA:
        order = Order(
            device=data['device'],
            serial_number=data['serial_number'],
            defect=data['defect'],
            shape=data['shape'],
            kit=data['kit'],
            status=data['status'],
            customer_id=random_customer
        )
        random_customer += 1
        orders.append(order)
    session.add_all(orders)
    session.commit()
    logger.info(f"Fake orders added to db")


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
    logger.info(f"Fake customers added to db")


def add_comments_to_db() -> NoReturn:
    comments = []
    order_id = 1
    for data in COMMENTS_DATA:
        order = Comment(
            diagnosis=data['diagnosis'],
            price=data['price'],
            comment=data['comment'],
            order_id=1
        )
        order_id += 1
        comments.append(order)
    session.add_all(comments)
    session.commit()
    logger.info(f"Fake comments added to db")


def add_fake_data_to_db():
    add_orders_to_db()
    add_customers_to_db()
    add_comments_to_db()
    logger.info(f"All fake data added to db")
