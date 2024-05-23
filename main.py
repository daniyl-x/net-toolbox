import subprocess
from flask import Flask, request

import funs


app = Flask(__name__)


@app.get("/")
def index():
    data = {"msg": "Hello, World!"}
    data = funs.serialize_json(data)

    return data


@app.get("/ping")
def ping():
    ip = request.args.get("ip")
    result = subprocess.run(["ping", "-c", "5", ip], capture_output=True)
    data = {"stdout": result.stdout.decode()}
    data = funs.serialize_json(data)

    return data


@app.get("/dig")
def dig():
    domain = request.args.get("domain")
    result = subprocess.run(["dig", domain], capture_output=True)
    data = {"stdout": result.stdout.decode()}
    data = funs.serialize_json(data)

    return data
