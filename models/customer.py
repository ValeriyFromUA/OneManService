from sqlalchemy import Column, Integer, String
from sqlalchemy_utils import EmailType
from sqlalchemy.orm import relationship

from models.base import Base


class Customer(Base):
    __tablename__ = 'customer'

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    phone = Column(String)
    email = Column(EmailType)
    socials = Column(String)
    address = Column(String)
    order = relationship('Order', back_populates='customer')

    def __repr__(self):
        return (
            f"{self.first_name} {self.last_name} {self.phone} {self.email} {self.socials} {self.address} "
        )

    def to_dict(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'phone': self.phone,
            'email': self.email,
            'socials': self.socials,
            'address': self.address
        }
