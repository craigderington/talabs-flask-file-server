#!usr/bin/python

import logging
import os
import config
from flask import Flask, request, send_from_directory, render_template
from datetime import datetime, timedelta

# define app
app = Flask(__name__,
            static_folder="static",
            template_folder="templates")

# setup gunicorn logging
gunicorn_logger = logging.getLogger("gunicorn.error")
app.logger.handlers = gunicorn_logger.handlers
app.logger.setLevel(gunicorn_logger.level)
app.SECRET_KEY = config.SECRET_KEY


@app.route("/", methods=["GET"])
@app.route("/index", methods=["GET"])
def index():
    """
    Default site index placeholder
    :param none
    :return str
    """
    app.logger.info("Serving {} request on site index".format(request.method))
    return render_template(
        "index.html",
        today=get_date()
    )


@app.route("/<path:filename>", methods=["GET"])
def send_file(filename):
    """
    Expose an endpoint and serve static files
    :param path + filename
    :return file
    """
    app.logger.info("Serving {} request for file: {}".format(request.method, filename))

    return send_from_directory(
        app.static_folder + "/docs/",
        filename
    )


@app.route("/login", methods=["GET"])
def login():
    """
    Render the login page
    :param none
    :return template
    """
    return render_template(
        "login.html",
        today=get_date()
    )


@app.errorhandler(404)
def page_not_found(err):
    """
    404 error handler
    """
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(err):
    """
    500 error handler
    """
    return render_template('500.html'), 500


def get_date():
    """
    Generate the current date time
    :param: none
    :return date as str
    """
    return datetime.now().strftime("%c")


if __name__ == "__main__":   
    app.start()
