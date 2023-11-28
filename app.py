from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask("__name__")

#adicionar database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.db'
#inicializando database
db = SQLAlchemy(app)
#criando modelo
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    email = cb.Column(db.String(200), nullable=False, unique=True)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)

    #criar uma string
    def_repr_(self):
        

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/luigi')
def luigi():
    return render_template('luigi.html')

@app.route('/bowser')
def bowser():
    return render_template('bowser.html')

