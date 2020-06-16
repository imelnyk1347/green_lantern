from store_app import app
from fake_storage import FakeStorage
import inject
from .views import users, goods, store  # .users


def configure(binder):
    db = FakeStorage()
    binder.bind('DB', db)


inject.clear_and_configure(configure)


if __name__ == '__main__':
    app.register_blueprint(users, goods, store)
    app.run(debug=True)
