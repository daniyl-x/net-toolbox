from flask import Blueprint, render_template


browser = Blueprint("browser", __name__)


@browser.get("/")
def index():
    template = "index.html"

    return render_template(template)


@browser.get("/dig")
def dig():
    template = "dig.html"

    return render_template(template)


@browser.get("/ping")
def ping():
    template = "ping.html"

    return render_template(template)
