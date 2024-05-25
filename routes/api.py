from flask import Blueprint, request

from lib import functions as fn


api = Blueprint("api", __name__)


@api.get("/dig")
def dig():
    domain = request.args.get("domain")
    data = fn.run_cmd(["dig", domain])

    return data


@api.get("/ping")
def ping():
    ip = request.args.get("ip")
    data = fn.run_cmd(["ping", "-c", "5", ip])

    return data
