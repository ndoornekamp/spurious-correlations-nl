import json

from flask import render_template
from flask import request

from app import app

with open('data/correlated_series.json', 'r') as infile:
    correlated_series = json.load(infile)


@app.route('/')
def index():
    series1, series2, correlation = correlated_series[0]
    context = {
        "series1": series1,
        "series2": series2,
        "correlation": correlation,
    }
    return render_template('index.html', **context)


@app.route('/data', methods=['POST'])
def data():
    idx = json.loads(request.data)['index']
    series1, series2, correlation = correlated_series[idx]
    data = {
        "series1": series1,
        "series2": series2,
        "correlation": correlation,
    }
    return data
