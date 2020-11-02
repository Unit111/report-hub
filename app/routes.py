import os
import re

from flask import Flask, render_template, session, request, jsonify

from app.config import Config
from app.helpers import collect_files

app = Flask(__name__, static_url_path='/static')
app.config.from_object(Config())


@app.after_request
def add_header(response):
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    return response


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/content', methods=['GET'])
def get_content():
    name = request.args.get('name')
    return session["reports"][name]


@app.route('/all_reports', methods=['GET'])
def all_reports():
    session["reports"] = collect_files()
    return jsonify(session["reports"])


@app.route('/history', methods=['GET'])
def history():
    name = request.args.get('name')
    name = re.sub(r'_[0-9]{4}_[0-9]{2}_[0-9]{2}_[0-9]{2}_[0-9]{2}.json', "", name)
    filtered_reports = {k: v for (k, v) in session["reports"].items() if name in k}
    return jsonify(filtered_reports)
