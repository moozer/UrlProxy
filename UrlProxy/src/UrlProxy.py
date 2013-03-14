'''
Created on 14 Mar 2013

@author: moz
'''

from flask import Flask
from flask.templating import render_template
from flask.helpers import url_for, send_from_directory
from flask.globals import request
from werkzeug.utils import redirect
app = Flask(__name__)

@app.route("/")
def index():
    print url_for('static', filename='index.html')
    return send_from_directory(app.static_folder, 'index.html')

@app.route("/ProcessRedirect")
def ProcessRedirect(methods=['GET']): #     is implied
    URL = request.args['urltoget']
    return redirect(URL)

if __name__ == "__main__":
    app.run()