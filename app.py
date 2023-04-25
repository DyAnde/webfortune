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
    #output = os.system('fortune')
    #return '<pre>' + str(output) + '</pre>' 
    return 'THIS IS WHERE FORTUNE WOULD BE IF IT WORKED'

@app.route('/cowsay/<message>/')
def cowsay(message):
    os.system(f'cowsay({message}) > temp.txt')
    with open('temp.txt', 'r') as f:
        ahhh = f.read()
    os.remove('temp.txt')
    return '<pre>' + ahhh + '</pre>'

@app.route('/cowfortune/')
def cowfortune():
    #output = os.system('fortune')
    #return os.system(f'cowsay({output})')
    return 
