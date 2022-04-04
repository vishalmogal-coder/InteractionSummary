from flask import Flask, request, jsonify
import json
from flask_cors import CORS
app = Flask(__name__)
from interaction_script import *

# print("Hello")


CORS(app)

@app.route('/summary', methods=['GET'])
def login():
    try:
        s=get_interaction()
        return s
    except:
        return jsonify(error="Error")