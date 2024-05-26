from flask import Blueprint, request

from lib import functions as fn


api = Blueprint("api", __name__)


@api.get("/dig")
def dig():
    host = request.args.get("host")
    data = fn.run_cmd(["dig", host])

    return data


@api.get("/ping")
def ping():
    host = request.args.get("host")
    data = fn.run_cmd(["ping", "-c", "5", host])

    return data


@api.get("/traceroute")
def traceroute():
    host = request.args.get("host")
    data = fn.run_cmd(["traceroute", "--icmp", host])

    return data


@api.get("/whois")
def whois():
    host = request.args.get("host")
    data = fn.run_cmd(["whois", host])

    return data
