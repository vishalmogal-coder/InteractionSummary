from flask import Flask, request, jsonify
import json
from flask_cors import CORS
from interaction_script import get_interaction



app = Flask(__name__)
# print("Hello")


CORS(app)

@app.route('/summary', methods=['GET'])
def login():
    try:
        s=get_interaction()
        return s
    except:
        return jsonify(error="Error")