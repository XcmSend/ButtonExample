
# A very simple Flask Hello World app for you to get started with...

import pickledb
from flask import Flask, request, jsonify
from flask_cors import CORS

import logging
logger = logging.getLogger('werkzeug')
handler = logging.FileHandler('access.log')
logger.addHandler(handler)

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

cacher = {}

@app.route('/')
def hello_world():
    return 'Hello!!'

@app.route('/mempool/<blueblue>', methods=["POST", "GET"])
def save_me(blueblue):
    print("got mempool!!")
    global cacher
    app.logger.info("Here's some info")
    print(f"Request method: {request.method}")
    print(f"Request path: {request.path}")
    print(f"Request headers: {request.headers}")
    print(f"Request form data: {request.form}")
    print(f"Request JSON data: {request.json}")  # Assumes JSON content type
    print(f"Request args: {request.args}")
    outme = request.get_json().get('requestContent')
    print(f"outme = {outme}")
    if not outme:
        return 'nope'
    cacher[blueblue] = outme
    print("EOL!!")
    return jsonify({'result': 'ok'})

@app.route('/loot/<blueblue>')
def get_loot(blueblue):
    if not cacher.get(blueblue):
        return jsonify({'message': 'no data found'})
    return jsonify({'result':cacher.get(blueblue)})

