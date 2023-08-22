#!/usr/bin/env python3

from faker import Faker
import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import User,Expense 

fake = Faker()

if __name__ == '__main__':
    
    engine = create_engine('sqlite:///expense.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    user = User(user_name="JohnDoe", password= 123456)
    session.add(user)
    session.commit()

    expense = Expense(item="Item 1", size="Medium", quantity=2, price=10.0, total=20,user_id = 1)
    session.add(expense)
    session.commit()

    print(user.id)
    print(Expense.item)

    


    import ipdb; ipdb.set_trace()
