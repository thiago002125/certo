from app import app
from flask import jsonify

@app.route("/hello")

def name():
        return jsonify({"msg": "hello"})
