from flask import Flask, jsonify
from flask_restful import Resource, Api
from flask_mysqldb import MySQL

app = Flask(__name__)
api = Api(app)
class HelloWorld(Resource):
    def get(self):
        # Data you want to send to Flutter
        data = {
            'message': 'Hello from Python Backend!',
            'timestamp': '2025-12-22T16:21:00Z', # Example dynamic data
            'status': 'success'
        }
        return jsonify(data) # Return data as JSON

api.add_resource(HelloWorld, '/')
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)