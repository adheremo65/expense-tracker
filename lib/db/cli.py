#!/usr/bin/env python
from models import User,Expense
from sqlalchemy import engine,create_engine,func
from colorama import init, Fore, Style
from sqlalchemy.orm import sessionmaker
engine = create_engine("sqlite:///expense.db")
session = sessionmaker(bind=engine)
from tabulate import tabulate

init()


class display:
    def __init__(self):
        self.session = session()
        self.current_user = None
        
   

    def login(self):
        user_name = input("put your name:")
        password = input("put your password")
        user = self.session.query(User).filter_by(user_name = user_name, password = password).first()
        if user:
            self.current_user = user
            print(f"Welcome, {user.user_name}!")
        else:
            print("Invalid credentials. Please try again.")

    def print_colored(self,text,color):
        print(text + color +Style.RESET_ALL )

    def expense_per_item(self):
    # def user_expense_table(self):
        if self.current_user:
            user_expenses = (
            self.session.query(
                Expense.item,
                Expense.price,
                Expense.quantity,
                Expense.total,
                Expense.date,
            )
            .filter(Expense.user == self.current_user)
            .all()
        )

            headers = ["Item", "Price", "Quantity", "Total", "Date"]
            table_data = [(item, price, quantity, total, date) for item, price, quantity, total, date in user_expenses]

            print(tabulate(table_data, headers=headers, tablefmt="grid"))
        else:
            print("Please log in first.")
        

    def over_all_expense(self):
        if self.current_user:
            total_expense_for_user = self.session.query(func.sum(Expense.total)).join(User).filter(User.user_name == self.current_user.user_name,User.password == self.current_user.password).scalar()

            # Print the result
        print(Fore.BLUE + f"Total expense for user name  {self.current_user.user_name} is : {total_expense_for_user}")
        

if __name__ == "__main__":

    total_spent = display()
    while True:
        choise = input( Fore.YELLOW + "1.Log\n2.Disply_Expense_per_item and total_expense and \n3.Exit\nEnter your choice: ")
        if choise == "1": 
            total_spent.login()
        elif choise == "2": 
            total_spent.expense_per_item()
            total_spent.over_all_expense()
        elif choise == "3":
            print("Goodbye!")
            break
        else:
            print(Fore.RED + "Invalid choice. Please select again.")
            