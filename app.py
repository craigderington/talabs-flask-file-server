#!usr/bin/python

import os
from flask import Flask, request, send_from_directory
import logging

SECRET_KEY = os.urandom(64)
DEBUG = True

app = Flask(__name__,
            static_folder="static")


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
    :param filename
    :return file
    """
    app.logger.info("Serving {} request for file: {}".format(request.method, filename))

    return send_from_directory(
        app.static_folder + "/docs/",
        filename
    )


if __name__ == "__main__":   
    app.run(
        host="0.0.0.0",
        port=8000,
        debug=DEBUG
    )
