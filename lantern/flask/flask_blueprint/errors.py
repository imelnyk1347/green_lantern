from flask import jsonify


class NoSuchUserError(Exception):
    def __init__(self, user_id):
        self.message = f'No such user_id: {user_id}'


class NoSuchUserID(Exception):
    def __init__(self, store_id):
        self.message = f'No such user id: {store_id}'


class NoSuchStoreID(Exception):
    def __init__(self, store_id):
        self.message = f'No such store id: {store_id}'


def my_error_handler(e):
    return jsonify({'ERROR': e.message}), 404
