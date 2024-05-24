from flask import Blueprint

from lib import functions as fn


browser = Blueprint("browser", __name__)


@browser.get("/")
def index():
    data = {"msg": "Hello, World!"}
    data = fn.serialize_json(data)

    return data
