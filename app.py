from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo



app = Flask(__name__)

mongo = PyMongo(app, uri='mongodb://localhost:27017/police_db')

@app.route('/')

def index():

 # Find one record of data from the mongo database
    stop_data = mongo.db.collection()

    # Return template and data
    return render_template('index.html', police_stops=stop_data)

if __name__ == "__main__":
    app.run(debug=True)
