from flask import Flask, request

import funs


app = Flask(__name__)


@app.get("/")
def index():
    data = {"msg": "Hello, World!"}
    data = funs.serialize_json(data)

    return data


@app.get("/dig")
def dig():
    domain = request.args.get("domain")
    data = funs.run_cmd(["dig", domain])
    data = funs.serialize_json(data)

    return data


@app.get("/ping")
def ping():
    ip = request.args.get("ip")
    data = funs.run_cmd(["ping", "-c", "5", ip])
    data = funs.serialize_json(data)

    return data
