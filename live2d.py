import json
import logging
from flask import Flask, send_from_directory

with open('data/db/config.db', 'r', encoding='utf-8') as file:
    lines = file.readlines()
live2d_port = int(lines[25].strip())
app = Flask(__name__, static_folder='dist')
logging.getLogger('werkzeug').setLevel(logging.ERROR)


@app.route('/')
def index():
    return app.send_static_file('live2d.html')


@app.route('/assets/<path:path>')
def serve_static(path):
    return send_from_directory('./dist/assets', path)


@app.route('/api/get_mouth_y')
def read_txt():
    with open("data/cache/cache.txt", "r") as f:
        return json.dumps({"y": f.read()})


def run_live2d():
    app.run(port=live2d_port, host="0.0.0.0")
