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
    # import pdb;pdb.set_trace()
    return render_template('profile.html', user=current_user.name, email=current_user.email)
