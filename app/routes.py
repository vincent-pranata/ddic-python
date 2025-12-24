from flask import jsonify, request, redirect, session, url_for
import requests,os,json
from app import app, mainEngine

@app.route('/')
def index():
    data = {
        'message': 'Hello from Python Backend!',
        'timestamp': '2025-12-22T16:21:00Z', # Example dynamic data
        'status': 'success'
    }
    return jsonify(data)