from flask import Blueprint
from flask_login import login_required


orders = Blueprint("orders", __name__, url_prefix="")

@orders.route("/")
@login_required
def index():
    return "Order Up"
