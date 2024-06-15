from binascii import Error
from flask import Flask
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)

def create_connection():
    try:
        connection = mysql.connector.connect(
            host="127.0.0.1",
            port="3306",
            user="root",
            password="Lisa2708..",
            database="primary"
        )
        print("Connection established")
        return connection
    except Error as e:
        print(e)
        return None

connection = create_connection()

from app import routes