from flask import Flask, jsonify, render_template
from dotenv import load_dotenv
import os
import requests

from settings import BACKEND_URL

load_dotenv()

app = Flask(__name__)


@app.route("/env")
def index():
    env_data = dict(os.environ)

    env_data["app"] = "frontend"
    env_data["name"] = "Altair"

    return jsonify(env_data)


@app.route("/data")
def data():
    res = requests.get(BACKEND_URL + "/get")

    data = res.json()

    return jsonify(data)


@app.route("/")
def home():
    res = requests.get(BACKEND_URL + "/get")

    data = res.json()

    return render_template("index.html", data=data)


if __name__ == "__main__":
    app.run(debug=True, port=3000, host="0.0.0.0")
