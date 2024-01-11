from dotenv import load_dotenv
load_dotenv()


from app import flask_app as app
from app.models import db, Employee, Menu, \
    MenuItem, MenuItemType, Table
from random import randrange


with app.app_context():
    db.drop_all()
    db.create_all()

    employee = Employee(name="Margot", employee_number=1234, password="password")

    dinner = Menu(name="Dinner")

    beverages = MenuItemType(name="Beverages")
    entrees = MenuItemType(name="Entrees")
    sides = MenuItemType(name="Sides")

    fries = MenuItem(name="French fries", price=3.50, type=sides, menu=dinner)
    drp = MenuItem(name="Dr. Pepper", price=1.0, type=beverages, menu=dinner)
    jambalaya = MenuItem(name="Jambalaya", price=21.98, type=entrees, menu=dinner)

    for i in range(10):
        table = Table(number=i+1, capacity=randrange(2, 7))
        db.session.add(table)

    db.session.add(employee)
    db.session.add(dinner)
    db.session.commit()
