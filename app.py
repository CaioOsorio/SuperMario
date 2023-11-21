from flask import Flask, render_template

app = Flask("__name__")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/luigi')
def luigi():
    return render_template('luigi.html')

