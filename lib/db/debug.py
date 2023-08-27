#!/usr/bin/env python
from faker import Faker
import random
from sqlalchemy import create_engine,func
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
    

    x = session.query(User.user_name, func.sum(Expense.total).label("total_expense")).join(Expense).group_by(User.user_name).all()

    total_expenses_per_user_per_item = (
    session.query(User.user_name, func.sum(Expense.total).label("total_expense"))
    .join(Expense)
    .group_by(User.user_name, User.password)
    .all()
)

    for user_name, total_expense in total_expenses_per_user_per_item:
        print(f"User: {user_name}, Total Expense: {total_expense}")

    target_user_name = None 
    target_user_name = input("put your name: ")# Replace with the username you're interested in
    target_user_password= input("put your password: ")

        # Query to calculate the total expenses for the specified user
    total_expense_for_user = (
            session.query(func.sum(Expense.total)).join(User).filter(User.user_name == target_user_name,User.password == target_user_password).scalar()
        )

        # Print the result
    print(f"Total expense for user {target_user_name}: {total_expense_for_user}")

    print(x)
    print(user.id)
    print(expense.item)

    


    import ipdb; ipdb.set_trace()
