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

    # def totat_expense(self):
    #     if self.current_user:
    #         total = 

           
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


        # target_user_name = None 
        # user = input("put your name")# Replace with the username you're interested in

        # # Query to calculate the total expenses for the specified user
        # total_expense_for_user = (
        #     session.query(func.sum(Expense.total)).join(User).filter(User.user_name == target_user_name).scalar()
        # )

        # # Print the result
        # print(f"Total expense for user {target_user_name}: {total_expense_for_user}")

        
            

            # total_expense = (self.session.query(func.sum(Expense.total)).filter(Expense.user == self.current_user)).all()
            # incured = sum(expense[0] for expense in total_expense)
         
      
          
            # if total_expense is None:
            #     total_expense = 0
        #     print(f"your total expense is:  {incured}")
        # else:
        #     print("Please log in first.")

if __name__ == "__main__":

    total_spent = display()
    while True:
        choise = input( Fore.YELLOW + "1.Log\n2.Disply_Total_Expense\n3.Exit\nEnter your choice: ")
        if choise == "1": 
            total_spent.login()
        elif choise == "2": 
            total_spent.totat_expense()
        elif choise == "3":
            print("Goodbye!")
            break
        else:
            print(Fore.RED + "Invalid choice. Please select again.")
            