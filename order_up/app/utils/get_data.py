from sqlalchemy.orm import joinedload
from app.models import Employee, Order, \
    Table, MenuItemType


def get_menu_items():
     menu_item_types_with_items = MenuItemType.query.options(joinedload(MenuItemType.menu_items)).all()
     menu_items_data = [(item.name, [(itm.id, itm.name) for itm in item.menu_items]) for item in menu_item_types_with_items]
     return menu_items_data

def get_open_orders():
     open_orders = Order.query.filter(Order.finished == False)
     return [(order.id, order.table_id, order.table.number, order.total_price) for order in open_orders]

def get_open_tables():
      # Get the tables and open orders
      tables = Table.query.order_by(Table.number).all()
      open_orders = Order.query.filter(Order.finished == False)

      # Get the table ids for the open orders
      busy_table_ids = [order.table_id for order in open_orders]

      # Filter the list of tables for only the open tables
      open_tables = [table for table in tables if table.id not in busy_table_ids]

      # Finally, convert those tables to tuples for the select field and
      # return the result
      return [(t.id, f"Table {t.number}") for t in open_tables]

def get_servers():
      employees = Employee.query.all()
      return [(emp.id, emp.name) for emp in employees]
