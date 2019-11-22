from flask import Flask
from prometheus_client import make_wsgi_app
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.serving import run_simple
from flask_prometheus_metrics import register_metrics

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello metrics! Go to /metrics"


register_metrics(app, app_version="v0.1.2", app_config="production")

dispatcher = DispatcherMiddleware(app.wsgi_app, {"/metrics": make_wsgi_app()})

run_simple(hostname="localhost", port=5000, application=dispatcher)