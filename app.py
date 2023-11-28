from flask import Flask, render_template
from flask_sqlalchemy import SQLALchemy
from datetime import datetime

app = Flask("__name__")

#adicionar database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.db'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/luigi')
def luigi():
    return render_template('luigi.html')

@app.route('/bowser')
def bowser():
    return render_template('bowser.html')

