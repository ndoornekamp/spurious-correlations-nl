import json

import numpy as np

from flask import render_template
from flask import request, session
from flask_babel import _, get_locale

from app import app
from app.correlation import find_max_correlation

YEARS = [2014, 2015, 2016, 2017, 2018, 2019, 2020]

with open('data/correlated_series.json', 'r') as infile:
    correlated_series = json.load(infile)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/data', methods=['POST'])
def data():
    language = str(get_locale())

    idx = json.loads(request.data)['index'] % len(correlated_series)  # Truly infinite scroll
    series1, series2, correlation = correlated_series[idx]

    series1['localized_title'] = _(series1['title'][language])
    series2['localized_title'] = _(series2['title'][language])
    series1['localized_axis_label'] = _(series1['axis_label'][language])
    series2['localized_axis_label'] = _(series2['axis_label'][language])

    data = {
        "series1": series1,
        "series2": series2,
        "correlation": correlation,
    }
    return data


@app.route('/find_new', methods=['GET', 'POST'])
def find_new():
    if request.method == 'GET':
        return render_template('find_new.html', years=YEARS)
    else:
        input_series = np.array([float(request.form[str(year)]) for year in YEARS])
        input_title = request.form['title']
        input_axis_label = request.form['axis_label']

        with open('data/all_data.json', 'r') as infile:
            all_data = json.load(infile)

        all_data_flat = [series for category_series in all_data.values() for series in category_series]
        all_series = np.array([np.array(data['values']) for data in all_data_flat])

        max_correlation, max_correlation_idx = find_max_correlation(input_series, all_series)
        max_correlated_series = all_data_flat[max_correlation_idx]

        language = str(get_locale())
        max_correlated_series['localized_title'] = _(max_correlated_series['title'][language])
        max_correlated_series['localized_axis_label'] = _(max_correlated_series['axis_label'][language])

        data = {
            "series1": {
                "localized_title": input_title,
                "localized_axis_label": input_axis_label,
                "values": list(input_series)
            },
            "series2": max_correlated_series,
            "correlation": max_correlation
        }

        return render_template('find_new.html', result=json.dumps(data))


@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html')


@app.route('/set_language', methods=['POST'])
def set_language():
    requested_language = json.loads(request.data)['language']
    if session.get('language') == requested_language:
        changed_language = False
    else:
        session['language'] = requested_language
        changed_language = True

    return json.dumps({'changed_language': changed_language})
