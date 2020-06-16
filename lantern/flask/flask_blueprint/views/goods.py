from flask import Blueprint, request, jsonify
import inject


goods = Blueprint("goods", __name__)


@goods.route('/goods', methods=['POST'])
def create_goods():
    db = inject.instance('DB')
    goods = db.goods.add_goods(request.json)
    return jsonify({'numbers of items created': len(request.json)}), 201


@goods.route('/goods')
def get_goods():
    db = inject.instance('DB')
    goods = db.goods.get_full_info_of_goods()
    return jsonify(goods), 200


@goods.route('/goods', methods=['PUT'])
def update_goods():
    db = inject.instance('DB')
    succes_count, error_ids = db.goods.put_info_on_goods(request.json)
    return jsonify(
        {
            'successfully_updated': succes_count,
            'errors': {'no such id in goods': error_ids}
        }
    ), 200
