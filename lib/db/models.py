from sqlalchemy import create_engine
from faker import Faker
faker = Faker()
from sqlalchemy.ext.declarative import declarative_base
engine = create_engine("sqlite:///expenses.db")
Base = declarative_base()
from datetime import datetime
from sqlalchemy import Column,DateTime,String,Integer,DECIMAL,ForeignKey



class User(Base):
    __tablename__ = "users"
    id = Column(Integer(),primary_key=True)
    user_name = Column(String(),index=True)
    password = Column(String())
    def __repr__(self):
        return f"user {User.id}: "\
              + f"name {User.user_name}, "\
              + f"password{User.password}"
class Expense(Base):
    __tablename__ = "expenses"
    id = Column(Integer(), primary_key=True)
    item = Column(String())
    size = Column(String())
    quantity = Column(Integer())
    price = Column(DECIMAL())
    total = Column(DECIMAL())
    date = Column(DateTime, default = datetime.now())
    user_id = Column(Integer(), ForeignKey('users.id'))

    def __repr__(self):
        return f"item {Expense.id}: "\
        + f"Size {Expense.size}, "\
        + f"Quantity {Expense.quantity}, "\
        + f"Total {Expense.total}, "\
        + f"date {Expense.date}, "\
        + f"user_id {User.id}"

