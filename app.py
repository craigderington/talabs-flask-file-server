#!usr/bin/python

import logging
import os
import config
from flask import Flask, request, send_from_directory

SECRET_KEY = config.SECRET_KEY
app = Flask(__name__,
            static_folder="static")

gunicorn_logger = logging.getLogger("gunicorn.error")
app.logger.handlers = gunicorn_logger.handlers
app.logger.setLevel(gunicorn_logger.level)


@app.route("/", methods=["GET"])
def index():
    """
    Default site index placeholder
    :param none
    :return str
    """
    app.logger.info("Serving {} request on site index".format(request.method))
    msg = "Download files from the static directory.  \
           Usage:  http://server-ip:8000/filename.ext"
    
    return msg


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


if __name__ == "__main__":   
    app.start()