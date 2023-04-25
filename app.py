from flask import (
		abort, Flask, jsonify, redirect, render_template, request,
		session, url_for
		)
import os 

app = Flask(__name__)

TEMP_FILE = 'temp.txt'

@app.route('/')
def index():
	return redirect(url_for('fortune'))

@app.route('/fortune/')
def fortune():
	os.system('fortune > temp.txt')
	with open(TEMP_FILE, 'r') as f:
		reee = f.read()
	os.remove(TEMP_FILE)
	return reee 

@app.route('/cowsay/<message>/')
def cowsay(message):
	os.system('cowsay '+message+' > temp.txt')
	with open(TEMP_FILE, 'r') as f:
		ahhh = f.read()
	os.remove(TEMP_FILE)
	return '<pre>' + ahhh + '</pre>'

@app.route('/cowfortune/')
def cowfortune():
	os.system('fortune | cowsay > temp.txt')
	with open(TEMP_FILE, 'r') as f:
		reah = f.read()
	os.remove(TEMP_FILE)
	return '<pre>' + reah + '</pre>'
