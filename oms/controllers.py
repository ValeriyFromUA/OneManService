from operator import or_
from typing import Dict, List, Optional, Tuple

from db.db_engine import get_session
from models import Customer, Order, Comment
from oms.logger import get_logger

session = get_session()

logger = get_logger(__name__)


def get_all_orders() -> List[Dict]:
    orders = session.query(Order).all()
    logger.info(f"Successfully find all orders list")
    return [order.to_dict() for order in orders]


def get_order_by_id(_id: int) -> Optional[Dict]:
    order = session.query(Order).filter(Order.id == _id).first()
    if order is None:
        logger.info(f"Order with id #{_id} not exist")
        return
    logger.info(f"Successfully find order #{_id} list")
    return order.to_dict()


def find_orders_by_device_name(name: str) -> List[Dict]:
    orders = session.query(Order).filter(Order.device.like(f'%{name}%')).all()
    logger.info(f"Searching order with device name >{name}<")
    return [order.to_dict() for order in orders]


def add_new_order(device: str, defect: str, serial_number: str, shape: str, customer_id: int, kit: str = None,
                  max_time_for_fixing: int = 14, status: str = 'is waiting') -> Dict:
    order = Order(
        device=device,
        defect=defect,
        serial_number=serial_number,
        shape=shape,
        customer_id=customer_id,
        kit=kit,
        max_time_for_fixing=max_time_for_fixing,
        status=status

    )
    session.add(order)
    session.commit()
    logger.info(f"Successfully added new order for device {device}")
    return order.to_dict()


def update_status_by_id(_id: int, status: str) -> Dict:
    order = session.query(Order).filter(Order.id == _id).first()
    order.status = status
    session.commit()
    logger.info(f"Order #{_id} is updated")
    return order.to_dict()


def delete_order_by_id(_id) -> Optional[int]:
    order = session.query(Order).filter(Order.id == _id).first()
    if order is None:
        logger.info(f"Order #{_id} not exist")
        return _id
    session.query(Order).filter(Order.id == _id).delete()
    session.commit()
    logger.info(f"Successfully deleted order #{_id}")


def get_all_customers() -> List[Dict]:
    customers = session.query(Customer).all()
    logger.info(f"Successfully find all customers list")
    return [customer.to_dict() for customer in customers]


def get_customer_by_id(_id: int) -> Optional[Dict]:
    customer = session.query(Customer).filter(Customer.id == _id).first()
    if customer is None:
        logger.info(f"Customer with id #{_id} not exist")
        return
    logger.info(f"Successfully find customer #{_id}")
    return customer.to_dict()


def find_customer_by_name(name: str) -> List[Dict]:
    customers = session.query(Customer).filter(
        or_(Customer.first_name.like(f'%{name}%'), Customer.last_name.like(f'%{name}%'))).all()
    logger.info(f"Searching customer with name >{name}<")
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
    logger.info(f"Customer {first_name} {last_name} added to DB")
    return customer.to_dict()


def update_customer(_id: int, new_first_name: str = None, new_last_name: str = None, new_phone: str = None,
                    new_email: str = None,
                    new_socials: str = None, new_address: str = None) -> Dict:
    customer = session.query(Customer).filter(Customer.id == _id).first()
    customer.first_name = customer.first_name if new_first_name is None else new_first_name
    customer.last_name = customer.last_name if new_last_name is None else new_last_name
    customer.phone = customer.phone if new_phone is None else new_phone
    customer.email = customer.email if new_email is None else new_email
    customer.socials = customer.socials if new_socials is None else new_socials
    customer.address = customer.address if new_address is None else new_socials
    session.commit()
    logger.info(f"Customer #{_id} wad updated")
    return customer.to_dict()


def delete_customer_by_id(_id: int) -> Optional[int]:
    customer = session.query(Customer).filter(Customer.id == _id).first()
    if customer is None:
        logger.info(f"Customer with id #{_id} not exist")
        return _id
    logger.info(f"Customer with id #{_id} was deleted")
    session.query(Customer).filter(Customer.id == _id).delete()
    session.commit()


def search_by_names(name: str) -> Tuple[List, List]:
    customers = find_customer_by_name(name)
    orders = find_orders_by_device_name(name)
    return customers, orders


def add_comment(diagnosis: str, comment: str, price: int, order_id: int) -> Dict:
    comment = Comment(
        diagnosis=diagnosis,
        comment=comment,
        price=price,
        order_id=order_id
    )
    session.add(comment)
    session.commit()
    logger.info(f"Created new comment")
    return comment.to_dict()


def update_comment(_id: int, new_diagnosis: str = None, new_comment: str = None, new_price: int = None) -> Dict:
    comment = session.query(Comment).filter(Comment.id == _id).first()
    comment.comment = comment.comment if new_comment is None else new_comment
    comment.diagnosis = comment.diagnosis if new_diagnosis is None else new_diagnosis
    comment.price = comment.price if new_price is None else new_price
    session.commit()
    logger.info(f"Comment #{_id} was updated")
    return comment.to_dict()
