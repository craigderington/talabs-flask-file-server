#!.env/bin/python

import os
from flask import Flask, request, send_from_directory

app = Flask(__name__,
            static_folder="static")

SECRET_KEY = os.urandom(64)
DEBUG = True

@app.route("/", methods=["GET"])
def index():
    """
    Homepage
    :pass
    :return
    """
    return "Hello, World!"


@app.route("/<path:filename>", methods=["GET"])
def send_file(filename):
    """
    Expose an endpoint and serve files
    :param
    :return 
    """
    return send_from_directory(
        app.static_folder,
        filename
    )


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=8000,
        debug=DEBUG
    )
