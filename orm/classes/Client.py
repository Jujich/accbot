from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from orm.classes.Base import Base


class Client(Base):
    __tablename__ = 'clients'

    id = Column(Integer, primary_key=True)
    tgClientId = Column(Integer, unique=True, nullable=False)
    username = Column(String(50))

    tgAccId = Column(Integer, ForeignKey('accountants.tgAccId'))

    accountant = relationship("Accountant", back_populates="clients")
