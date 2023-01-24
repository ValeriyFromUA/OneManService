import datetime

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from models.base import Base


def days_in_work(start):
    difference = datetime.datetime.now()-start
    return difference.days


class Order(Base):
    __tablename__ = 'order'

    id = Column(Integer, primary_key=True)
    device = Column(String)
    defect = Column(String)
    serial_number = Column(String)
    shape = Column(String, default="used")
    kit = Column(String)

    start_date = Column(DateTime, default=datetime.datetime.utcnow())
    end_date = Column(DateTime)
    max_time_for_fixing = Column(Integer, default=14)
    status = Column(String, default='is waiting')

    comment = relationship('Comment', back_populates='order')

    customer_id = Column(Integer, ForeignKey('customer.id'))
    customer = relationship('Customer', back_populates='order')

    def __repr__(self):
        return (
            f'\n {self.device} {self.defect} {self.serial_number},'
            f' {self.shape}, {self.kit}, {self.customer}, {self.start_date},'
            f' {self.end_date}, {self.max_time_for_fixing},{self.status}')

    def to_dict(self):
        return {
            'id': self.id,
            'device': self.device,
            'defect': self.defect,
            'serial_number': self.serial_number,
            'shape': self.shape,
            'kit': self.kit,
            'customer': self.customer,
            'start_date': self.start_date,
            'end_date': self.end_date,
            'max_time_for_fixing': self.max_time_for_fixing,
            'days_in_work': days_in_work(self.start_date),
            'status': self.status,
        }
