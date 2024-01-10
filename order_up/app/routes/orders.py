from flask import Blueprint, render_template
from flask_login import login_required


orders = Blueprint("orders", __name__, url_prefix="")

@orders.route("/")
@login_required
def index():
    return render_template("orders.html")
