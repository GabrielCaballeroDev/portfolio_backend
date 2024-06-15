from app import app, connection
from flask import jsonify
import mysql.connector
from mysql.connector import connect, DatabaseError

@app.route('/')

def myinfo():
    try:
        if connection is not None and connection.is_connected():
            cursor = connection.cursor(dictionary=True)
            cursor.execute('SELECT * FROM my_info')
            results = cursor.fetchall()
            return jsonify(results)
        else:
            return "Failed to connect to the database.", 500
    except DatabaseError as e:
        print(e)
        return "An error occurred while accessing the database.", 500

