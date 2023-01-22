import datetime

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship

from models.base import Base


class OrderModel(Base):
    __tablename__ = 'order'

    id = Column(Integer, primary_key=True)
    device = Column(String)
    defect = Column(String)
    serial_number = Column(String)
    shape = Column(String, default="used")
    kit = Column(String)
    customer = relationship('CustomerModel', secondary='CustomerOrder', backref='order', cascade="all,delete")
    price = Column(String)
    start_date = Column(DateTime, default=datetime.datetime.utcnow())
    end_date = Column(DateTime)
    max_time_for_fixing = Column(Integer, default=14)
    diagnosis = Column(String)
    comment = Column(String)
    status = Column(String, default='is waiting')

    def __repr__(self):
        return (
            f'\n {self.id} {self.device} {self.defect} {self.serial_number},'
            f' {self.shape}, {self.kit}, {self.customer},'
            f' {self.price}, {self.start_date},'
            f' {self.end_date}, {self.max_time_for_fixing}, {self.diagnosis}, {self.comment}',
            {self.status})

    def to_dict(self):
        return {
            'id': self.id,
            'device': self.device,
            'defect': self.defect,
            'serial_number': self.serial_number,
            'shape': self.shape,
            'kit': self.kit,
            'customer': self.customer,
            'price': self.price,
            'start_date': self.start_date,
            'end_date': self.end_date,
            'max_time_for_fixing': self.max_time_for_fixing,
            'diagnosis': self.diagnosis,
            'comment': self.comment,
            'status': self.status
        }
