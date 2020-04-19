from flask import Flask
from flask import render_template, request, jsonify
import numpy as np
import traceback
import pickle
import pandas as pd

app = Flask(__name__, template_folder='templates')


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
