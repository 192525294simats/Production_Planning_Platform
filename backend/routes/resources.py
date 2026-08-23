from flask import Blueprint, jsonify
from models import get_resources

resources_bp = Blueprint("resources", __name__)


@resources_bp.route("/api/resources", methods=["GET"])
def resources():
    data = get_resources()

    result = []

    for row in data:
        result.append({
            "id": row[0],
            "resource_name": row[1],
            "utilization": row[2],
            "availability": row[3]
        })

    return jsonify(result)
    