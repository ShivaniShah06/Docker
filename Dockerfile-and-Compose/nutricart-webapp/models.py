from database import Base
from sqlalchemy import String, Boolean, Integer, Column, Text
import uuid


class Item(Base):
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True,autoincrement=True)
    name = Column(String(255),nullable=False,unique=True)
    description = Column(Text)
    discount = Column(Boolean, default=False)
    price = Column(Integer,nullable=False)


    def __repr__(self):
        return f"<Item name={self.name} price={self.price}>"
 