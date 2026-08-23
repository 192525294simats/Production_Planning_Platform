from flask import Blueprint, jsonify
from models import get_inventory

inventory_bp = Blueprint("inventory", __name__)


@inventory_bp.route("/api/inventory", methods=["GET"])
def inventory():
    data = get_inventory()

    result = []

    for row in data:
        result.append({
            "id": row[0],
            "item_name": row[1],
            "stock_quantity": row[2],
            "reorder_level": row[3],
            "status": "REORDER" if row[2] < row[3] else "AVAILABLE"
        })

    return jsonify(result)