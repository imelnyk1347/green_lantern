from flask import Flask

import inject

from errors import NoSuchUserError, NoSuchStoreID, NoSuchUserID, my_error_handler
from fake_storage import FakeStorage
from views import users_blp, store_blp, goods_blp


def configure(binder):
    db = FakeStorage()
    binder.bind('DB', db)


def make_app():
    inject.clear_and_configure(configure)

    app = Flask(__name__)

    app.register_blueprint(users_blp)
    app.register_blueprint(store_blp)
    app.register_blueprint(goods_blp)

    app.register_error_handler(NoSuchUserError, my_error_handler)
    app.register_error_handler(NoSuchStoreID, my_error_handler)
    app.register_error_handler(NoSuchUserID, my_error_handler)

    return app
