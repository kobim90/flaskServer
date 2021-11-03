from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
from Models.users import *
from Routes.users import users
import os
load_dotenv()

DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_NAME = os.getenv('DB_NAME')
PORT = os.getenv('PORT')


app = Flask(__name__)

CORS(app, resources={
            r"/api/*": {"origins": "http://localhost:3000"}})
app.config['CORS_HEADERS'] = 'Content-Type'

HOST = f"mongodb+srv://{DB_USER}:{DB_PASSWORD}@kobiscluster.rvdyv.mongodb.net/{DB_NAME}" \
       f"?retryWrites=true&w=majority"

try:
    connect(host=HOST)
    print("----Connected to DB!----")
except Exception as e:
    print("Error connecting to DB", e)


@app.errorhandler(404)
def page_not_found(e):
    return {'message': "the page you are looking for is not found"}, 404


# Routes
@app.route('/')
def hello_world():
    return 'Hello World'


app.register_blueprint(users)

if __name__ == '__main__':
    app.run(debug=True, port=PORT)
