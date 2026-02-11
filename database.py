import mysql.connector.pooling
import os
from dotenv import load_dotenv

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

db_config = {
    "host": db_connection_name,
    "user": db_user,
    "password": db_password,
    "database": db_name
}

# Shared pool for all tables
connection_pool = mysql.connector.pooling.MySQLConnectionPool(
    pool_name="rebar_pool",
    pool_size=15,
    **db_config
)

def get_db():
    return connection_pool.get_connection()