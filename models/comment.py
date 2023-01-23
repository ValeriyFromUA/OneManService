from sqlalchemy import Column, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship

from models import Base


class Comment(Base):
    __tablename__ = 'comment'

    id = Column(Integer, primary_key=True)
    diagnosis = Column(Text)
    comment = Column(Text)
    price = Column(Integer)

    order_id = Column(Integer, ForeignKey('order.id'))
    order = relationship('Order', back_populates='comment')

    def __repr__(self):
        return f'\n{self.diagnosis} {self.comment} {self.price}'

    def to_dict(self):
        return {
            'id': self.id,
            'diagnosis': self.diagnosis,
            'comment': self.comment,
            'price': self.price
        }
