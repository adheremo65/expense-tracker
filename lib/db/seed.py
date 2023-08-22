#!/usr/bin/env python


from sqlalchemy.orm import sessionmaker
from sqlalchemy import engine,create_engine
from models import User,Expense

class info():
    def __init__(self) -> None:
        self.engine = create_engine('sqlite:///expense.db')
        Session = sessionmaker(bind=self.engine)
        self.session = Session()
        self.current_Identifier = None

    def register_user(self):
        user_name = input("Enter your user name: ")
        password = input("Enter your password: ")
        user_identifier = User(user_name= user_name, password = password)
        self.session.add(user_identifier)
        self.session.commit()
        self.current_Identifier = user_identifier
        
        

    def add_expense(self):
        #user_name = input("Enter your user name: ")
        if self.current_Identifier:
            item = input("Enter item name: ")
            size = input("Enter item size: ")
            quantity = int(input("Enter quantity: "))
            price = float(input("Enter price: "))
            total = price * quantity
            expense_incured = Expense(item= item, size =size,quantity = quantity,price = price,total = total,user=self.current_Identifier)
            self.session.add(expense_incured)
            self.session.commit()
        else:
             print("No user registered. Please register a user first.")



if __name__ == '__main__':
    info_instance = info()
    info_instance.register_user()
    info_instance.add_expense()
    
    
    