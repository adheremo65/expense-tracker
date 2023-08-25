from models import User,Expense
from sqlalchemy import engine,create_engine,func
from colorama import init, Fore, Style
from sqlalchemy.orm import sessionmaker
engine = create_engine("sqlite:///expense.db")
session = sessionmaker(bind=engine)

init()


class display:
    def __init__(self):
        self.session = session()
        self.current_user = None
        
   

    def login(self):
        user_name = input("input your name")
        password = input("put your password")
        user = self.session.query(User).filter_by(user_name = user_name, password = password).first()
        if user:
            self.current_user = user
            print(f"Welcome, {user.user_name}!")
        else:
            print("Invalid credentials. Please try again.")

    def print_colored(self,text,color):
        print(text + color +Style.RESET_ALL )

    def totat_expense(self):
        if self.current_user:
            total_expense = self.session.query(func.sum(Expense.total)).filter_by(user_id= self.current_user.id).scalar()
            
            if total_expense is None:
                total_expense = 0
            print(f"your total expense is:  {total_expense}")
        else:
           print("Please log in first.")

if __name__ == "__main__":

    total_spent = display()
    while True:
        choise = input("1.Log\n2.Disply_Total_Expense\n3.Exit\nEnter your choice: ")
        if choise == "1": 
            total_spent.login()
        elif choise == "2": 
            total_spent.totat_expense()
        elif choise == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select again.")
            