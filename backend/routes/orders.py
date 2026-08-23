from flask import Blueprint, jsonify
from models import get_production_orders

orders_bp = Blueprint("orders", __name__)


@orders_bp.route("/api/orders", methods=["GET"])
def orders():
    data = get_production_orders()

    result = []

    for row in data:
        result.append({
            "id": row[0],
            "product_name": row[1],
            "quantity": row[2],
            "production_line": row[3],
            "status": row[4],
            "due_date": str(row[5])
        })

    return jsonify(result)