from flask import Blueprint, render_template
from grocery_store.database import db
from flask_login import current_user, login_required

from grocery_store.models import Good


main = Blueprint('main', __name__)


@main.route('/')
def index():
    goods = Good.query.all()
    return render_template('index.html', goods=goods)


@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', user=current_user.name, email=current_user.email)


@main.route('/order')
@login_required
def order():
    user = current_user.name
    email = current_user.email
    orders = current_user.orders

    #  sum of all user goods price
    for ordering in orders:
        order_orderline = sum([order_lin.good.price for order_lin in ordering.order_lines])
    total = order_orderline

    return render_template("order.html", user=user, email=email, orders=orders, total=total)
