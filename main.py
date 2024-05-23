import subprocess
from flask import Flask, request


app = Flask(__name__)


@app.get("/")
def index():
    return {"msg": "Hello, World!"}


@app.get("/ping")
def ping():
    ip = request.args.get("ip")
    result = subprocess.run(
            ["ping", "-c", "5", ip],
            capture_output=True
            )
    return {"stdout": result.stdout.decode()}
