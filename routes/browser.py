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

    domain = request.args.get("domain")
    if domain:
        url = request.root_url + url_for("api.dig")
        response = httpx.get(f"{url}?domain={domain}")

        data = response.json()
        return render_template(template, data=data)
    else:
        return render_template(template)


@browser.get("/ping")
def ping():
    template = "ping.html"

    ip = request.args.get("ip")
    if ip:
        url = request.root_url + url_for("api.ping")
        response = httpx.get(f"{url}?ip={ip}")

        data = response.json()
        return render_template(template, data=data)
    else:
        return render_template(template)
