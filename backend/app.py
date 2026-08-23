from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
from routes.orders import orders_bp
from routes.inventory import inventory_bp
from routes.resources import resources_bp
import os

app = Flask(__name__)
CORS(app)

# Register API blueprints
app.register_blueprint(orders_bp)
app.register_blueprint(inventory_bp)
app.register_blueprint(resources_bp)


# Frontend folder path
FRONTEND_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "frontend")
)


# Home page
@app.route("/")
def home():
    return send_from_directory(FRONTEND_DIR, "index.html")


# Serve frontend files such as HTML, CSS and JavaScript
@app.route("/<path:filename>")
def frontend_files(filename):
    return send_from_directory(FRONTEND_DIR, filename)


# Health check API
@app.route("/api/health")
def health():
    return jsonify({
        "status": "healthy",
        "service": "Production Planning Platform"
    })


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )