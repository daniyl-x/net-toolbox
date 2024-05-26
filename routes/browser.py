from flask import Blueprint, render_template, request, url_for
import httpx


browser = Blueprint("browser", __name__)


@browser.get("/")
def index():
    template = "index.html"

    return render_template(template)


@browser.get("/dig")
def dig():
    template = "dig.html"

    host = request.args.get("host")
    if host:
        url = request.root_url + url_for("api.dig")
        response = httpx.get(f"{url}?host={host}")

        data = response.json()
        return render_template(template, data=data)
    else:
        return render_template(template)


@browser.get("/ping")
def ping():
    template = "ping.html"

    host = request.args.get("host")
    if host:
        url = request.root_url + url_for("api.ping")
        response = httpx.get(f"{url}?host={host}")

        data = response.json()
        return render_template(template, data=data)
    else:
        return render_template(template)


@browser.get("/whois")
def whois():
    template = "whois.html"

    host = request.args.get("host")
    if host:
        url = request.root_url + url_for("api.whois")
        response = httpx.get(f"{url}?host={host}")

        data = response.json()
        return render_template(template, data=data)
    else:
        return render_template(template)
