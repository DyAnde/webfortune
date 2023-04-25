from flask import (
    abort, Flask, jsonify, redirect, render_template, request,
    session, url_for
)
import os 

app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('fortune'))

@app.route('/fortune/')
def fortune():
    return '<pre>' + output + '</pre>' 

@app.route('/cowsay/<message>/')
def cowsay(message):
    return cowsay(message) 

@app.route('/cowfortune/')
def cowfortune():
    return redirect(url_for('fortune'))
