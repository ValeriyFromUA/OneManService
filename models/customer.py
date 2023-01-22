from sqlalchemy import Column, Integer, String
from sqlalchemy_utils import EmailType, PhoneNumberType
from sqlalchemy.orm import relationship

from models.base import Base


class CustomerModel(Base):
    __tablename__ = 'customer'

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    phone = Column(PhoneNumberType())
    email = Column(EmailType)
    socials = Column(String)
    orders = relationship('OrderModel', secondary='CustomerOrder', backref='customer', cascade="all,delete")

    def __repr__(self):
        return f'\n {self.first_name} {self.last_name} : {self.phone}, {self.email}, {self.socials}; {self.orders}'

    def to_dict(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'phone': self.phone,
            'email': self.email,
            'socials': self.socials,
            'orders': self.orders
        }
