from db.db_engine import get_session
from models import Customer, Order

session = get_session()
x = session.query(Order).all()
for el in x:
    el = el.to_dict()
    customer = el['customer']
    print(customer.first_name)
