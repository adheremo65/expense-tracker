from models import User,Expense
from sqlalchemy import engine,create_engine
from colorama import init, Fore, Style
from sqlalchemy.orm import sessionmaker
engine = create_engine("sqlite:///expense.db")
session = sessionmaker(bind=engine)
current_user = None
init()


class display:


    def login(self):
        user_name = input("input your name")
        password = input("put your password")
        user = session.query(User).filter_by(user_name = user_name, password = password).first()
        if user:
            current_user = user
            print(f"Welcome, {user.user_name}!")
        else:
            print("Invalid credentials. Please try again.")

    def print_colored(self,text,color):
        print(text + color +Style.RESET_ALL )

    def totat_expense(self):
        pass