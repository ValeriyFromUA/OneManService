from sqlalchemy import PrimaryKeyConstraint, Column, Integer, ForeignKey

from models.base import Base


class CustomerOrder(Base):
    __tablename__ = 'customer_order'
    __table_args__ = (
        PrimaryKeyConstraint('customer_id', 'order_id'),
    )
    customer_id = Column(Integer, ForeignKey('customer.id', onupdate="CASCADE", ondelete="CASCADE"))
    order_id = Column(Integer, ForeignKey('order.id', onupdate="CASCADE", ondelete="CASCADE"))
