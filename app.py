from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask("__name__")

        

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/luigi')
def luigi():
    return render_template('luigi.html')

@app.route('/bowser')
def bowser():
    return render_template('bowser.html')

