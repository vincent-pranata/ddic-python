import os
from dotenv import load_dotenv

# Default to 'development' if APP_ENV is not set in the host environment
environment = os.getenv("APP_ENV", "uat")

# Construct the filename, e.g., ".env.development"
env_file_path = f".env.{environment}"

# Load variables from the specific environment file
load_dotenv(dotenv_path=env_file_path)

# You can now access all variables using os.getenv()
DATABASE_URL = os.getenv("URL")
DEBUG_MODE = os.getenv("DEBUG") == "True" # Convert string "True" to boolean True

print(f"Loading configuration for: {environment}")
print(f"Debug mode is: {DEBUG_MODE}")
print(f"Database URL: {DATABASE_URL}")

# set the app env by running the line below on cmd line
# $env:APP_ENV = "local"/ "uat"/ "prod"