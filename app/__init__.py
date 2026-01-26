from flask import Flask
from mainEngine import MainEngine
from dotenv import load_dotenv
import os
import mysql.connector

# Initialize the app
app = Flask(__name__, instance_relative_config=True)


# Default to 'local' if APP_ENV is not set in the host environment
environment = os.getenv("APP_ENV", "local")

# Construct the filename, e.g., ".env.development"
env_file_path = f".env.{environment}"

# Load variables from the specific environment file
load_dotenv(dotenv_path=env_file_path)

db_user = os.getenv('SQL_USERNAME')
db_password = os.getenv('SQL_PASSWORD')
db_name = os.getenv('DBNAME')
db_connection_name = os.getenv('SQL_URL')
connection = mysql.connector.connect(user=db_user, password=db_password,
            host=db_connection_name, db=db_name)
            
mainEngine = MainEngine(connection)

# Load the views
from app import routes

# Load the config file
app.config.from_object('config')