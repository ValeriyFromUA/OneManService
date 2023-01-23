from operator import or_
from typing import Dict, List, Optional, Tuple

from db.db_engine import get_session
from models import Customer, Order
from oms.logger import get_logger

session = get_session()


# logger = get_logger(__name__)

def get_all_orders() -> List[Dict]:
    orders = session.query(Order).all()
    return [order.to_dict() for order in orders]


def get_order_by_id(_id: int) -> Optional[Dict]:
    order = session.query(Order).filter(Order.id == _id).first()
    if order is None:
        return
    return order.to_dict()


def find_orders_by_device_name(name: str) -> List[Dict]:
    orders = session.query(Order).filter(Order.device.like(f'%{name}%')).all()
    return [order.to_dict() for order in orders]


def add_new_order(device: str, defect: str, serial_number: str, shape: str, customer_id: int, kit: str = None,
                  price=None,
                  max_time_for_fixing: int = 14, diagnosis: str = None, comment: str = None,
                  status: str = 'is waiting') -> Dict:
    order = Order(
        device=device,
        defect=defect,
        serial_number=serial_number,
        shape=shape,
        customer_id=customer_id,
        kit=kit,
        price=price,
        max_time_for_fixing=max_time_for_fixing,
        diagnosis=diagnosis,
        comment=comment,
        status=status

    )
    session.add(order)
    session.commit()
    return order.to_dict()


def delete_order_by_id(_id):
    order = session.query(Order).filter(Order.id == _id).first()
    if order is None:
        return _id
    session.query(Order).filter(Order.id == _id).delete()
    session.commit()


def get_all_customers() -> List[Dict]:
    customers = session.query(Customer).all()
    return [customer.to_dict() for customer in customers]


def get_customer_by_id(_id: int) -> Optional[Dict]:
    order = session.query(Customer).filter(Customer.id == _id).first()
    if order is None:
        return
    return order.to_dict()


def find_customer_by_name(name: str) -> List[Dict]:
    customers = session.query(Customer).filter(
        or_(Customer.first_name.like(f'%{name}%'), Customer.last_name.like(f'%{name}%'))).all()
    return [customer.to_dict() for customer in customers]


def add_new_customer(first_name: str, last_name: str, phone: str, email: str = None, socials: str = None,
                     address: str = None) -> Dict:
    customer = Customer(
        first_name=first_name,
        last_name=last_name,
        phone=phone,
        email=email,
        socials=socials,
        address=address
    )
    session.add(customer)
    session.commit()
    return customer.to_dict()


def delete_customer_by_id(_id: int) -> Optional[int]:
    customer = session.query(Customer).filter(Customer.id == _id).first()
    if customer is None:
        return _id
    session.query(Customer).filter(Customer.id == _id).delete()
    session.commit()


def search_by_names(name: str) -> Tuple[List, List]:
    customers = find_customer_by_name(name)
    orders = find_orders_by_device_name(name)
    return customers, orders
