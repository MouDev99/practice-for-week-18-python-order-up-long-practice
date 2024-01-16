from flask import Blueprint, redirect, render_template, url_for
from ..utils.get_data import get_menu_items, get_open_orders, \
   get_open_tables, get_servers
from flask_login import login_required
from app.models import db, Employee, Order, Table
from ..forms import TableAssignmentForm


orders = Blueprint("orders", __name__, url_prefix="")

@orders.route("/")
@login_required
def index():
    table_assignment_form = TableAssignmentForm()
    table_assignment_form.tables.choices = get_open_tables()
    table_assignment_form.servers.choices = get_servers()

    open_orders = get_open_orders()
    menu_items = get_menu_items()

    return render_template("orders.html", \
                           table_assignment_form=table_assignment_form, \
                           open_orders=open_orders, \
                           menu_items=menu_items)

@orders.route("/assign", methods=["POST"])
@login_required
def assign_table():
    table_assignment_form = TableAssignmentForm()
    table_id = table_assignment_form.tables.data
    server_id = table_assignment_form.servers.data

    if table_id is None or server_id is None:
        return redirect(url_for("index"))
    table = Table.query.get(table_id)
    employee = Employee.query.get(server_id)

    order = Order(table=table, employee=employee, finished=False)

    db.session.add(order)
    db.session.commit()
    return redirect(url_for("orders.index"))


@orders.route("/close/<int:order_id>", methods=["POST"])
@login_required
def close_table(order_id):
    order = Order.query.get(order_id)
    order.finished = True
    db.session.add(order)
    db.session.commit()
    return redirect(url_for(".index"))
