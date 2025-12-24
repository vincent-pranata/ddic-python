from flask import Flask, request, url_for, jsonify
from mainEngine import MainEngine


# Initialize the app
app = Flask(__name__, instance_relative_config=True)

mainEngine = MainEngine()


# Load the views
from app import routes

# Load the config file
app.config.from_object('config')