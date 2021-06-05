import json

from flask import render_template
from flask import request, session
from flask_babel import _, get_locale

from app import app

with open('data/correlated_series.json', 'r') as infile:
    correlated_series = json.load(infile)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/data', methods=['POST'])
def data():
    locale = str(get_locale())
    locale_to_language = {
        'uk': 'en',
        'nl': 'nl'
    }
    language = locale_to_language[locale]

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
    return render_template('find_new.html')


@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html')


@app.route('/set_locale', methods=['POST'])
def set_locale():
    requested_locale = json.loads(request.data)['locale']
    if session.get('locale') == requested_locale:
        changed_locale = False
    else:
        session['locale'] = requested_locale
        changed_locale = True

    return json.dumps({'changed_locale': changed_locale})
