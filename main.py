# -*- coding: utf-8 -*-

# [START app]
import logging

from flask import Flask
from views import v_entry, v_regist, v_result

app = Flask(__name__)


@app.route('/')
def top():
    return v_entry()

@app.route('/regist', methods=['POST'])
def posted():
    return v_regist()

@app.route('/r')
def view_result():
    return v_result()


@app.errorhandler(500)
def server_error(e):
    # Log the error and stacktrace.
    logging.exception('An error occurred during a request.')
    return 'An internal error occurred.', 500
# [END app]

