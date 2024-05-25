from flask import Flask

from routes.api import api
from routes.browser import browser


app = Flask(
        __name__,
        static_url_path="/static",
)

app.register_blueprint(api, url_prefix='/api')
app.register_blueprint(browser)
