from flask import Blueprint, request, jsonify
import inject


store = Blueprint("store", __name__)


@store.route('/store', methods=['POST'])
def create_store():
    db = inject.instance('DB')
    store_id = db.stores.create_new_store(request.json)
    return jsonify({'stored_id': store_id}), 201


@store.route('/store/<int:store_id>')
def get_stores(store_id):
    db = inject.instance('DB')
    full_stores_info = db.stores.get_full_info(store_id)
    return jsonify(full_stores_info), 200


@store.route('/store/<int:store_id>', methods=['PUT'])
def update_store(store_id):
    db = inject.instance('DB')
    result = db.stores.update_store(request.json, store_id)
    return jsonify(result), 200

# import pdb;pdb.set_trace()
