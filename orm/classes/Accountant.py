from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from orm.classes.Base import Base


class Accountant(Base):
    __tablename__ = 'accountants'

    id = Column(Integer, primary_key=True)
    tgAccId = Column(Integer, unique=True, nullable=False)
    username = Column(String(50))
    tgGroupId = Column(Integer, unique=True)

    clients = relationship("Client", back_populates="accountant")
