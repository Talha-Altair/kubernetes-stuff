from flask import Flask, jsonify
from dotenv import load_dotenv
import os

from utils import coll

load_dotenv()

app = Flask(__name__)


@app.route("/env")
def index():
    env_data = dict(os.environ)

    env_data["app"] = "backend"
    env_data["name"] = "Altair"

    return jsonify(env_data)


@app.route("/ping")
def ping():
    return jsonify({"ping": "pong"})



@app.route("/add/<data>")
def add(data):
    coll.insert_one({"data": data})

    return jsonify({"message": f"{data} added successfully"})


@app.route("/get")
def get():
    data = coll.find({})

    data = list(data)

    result = []

    for val in data:
        result.append(val['data'])

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, port=9000, host="0.0.0.0")
