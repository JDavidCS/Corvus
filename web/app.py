#!/usr/bin/python3

from flask import Flask, jsonify, render_template
from flask_cors import CORS


app = Flask(__name__)

cors = CORS(app, resources={r'/api/*':  {'origins': '*'}})


@app.route('/')
def landing():
    return render_template('index.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')


@app.route('/app')
def application():
    return render_template('app.html')


@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not Found'}), 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5001', threaded=True, debug=True)
