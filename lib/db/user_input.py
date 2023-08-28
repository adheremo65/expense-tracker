#!/usr/bin/env python
from models import User,Expense
from sqlalchemy import engine,create_engine,func
from colorama import init, Fore, Style
from sqlalchemy.orm import sessionmaker
engine = create_engine("sqlite:///expense.db")
session = sessionmaker(bind=engine)
from tabulate import tabulate

init()

class info():
    def __init__(self) -> None:
        self.engine = create_engine('sqlite:///expense.db')
        session = sessionmaker(bind=self.engine)
        self.session = session()
        self.current_Identifier = None
    
    def register_user(self):
        user_name = input("Enter your user name: ")
        password = input("Enter your password: ")

        user_identifier = User(user_name= user_name, password = password)
        self.session.add(user_identifier)
        self.session.commit()
        self.current_Identifier = user_identifier
        
    def add_expense(self):
        user_name = input("Enter your user name: ")
        password = input("Enter your password: ")
        user = self.session.query(User).filter_by(user_name=user_name, password=password).first()
        if user:
            if self.current_Identifier is None:
                self.current_Identifier = user
                
            new_items = int(input("How many items are you adding? "))
            bath_enries = []

            for _ in range(new_items):
                item = input("Enter item name: ")
                size = input("Enter item size: ")
                quantity = float(input("Enter quantity: "))
                price = float(input("Enter price: "))
                total = price * quantity
                bath_enries.append((item, size, quantity, price, total))

            for entry in bath_enries:
                item, size, quantity, price, total = entry
                expense_incured = Expense(item=item, size=size, quantity=quantity, price=price, total=total, user=self.current_Identifier)
                self.session.add(expense_incured)
                self.session.commit()

            daily_expenses = self.session.query(Expense.total).filter_by(user=self.current_Identifier).all()

            def aggregate(expenses):
                total_daily_expense = 0
                for expense in expenses:
                    total_daily_expense += expense[0]
                return total_daily_expense

            total_expense = aggregate(daily_expenses)
            print(f"Your total expense is {total_expense}")

        else:
            print("User does not exist. Please register first.")
            self.register_user()
            self.add_expense()

if __name__ == '__main__':
    info_instance = info()
    info_instance.add_expense()
