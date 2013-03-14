'''
Created on 14 Mar 2013

@author: moz
'''

from flask import Flask
from flask.templating import render_template
from flask.helpers import url_for, send_from_directory
app = Flask(__name__)

@app.route("/")
def index():
    print url_for('static', filename='index.html')
    return send_from_directory(app.static_folder, 'index.html')



if __name__ == "__main__":
    app.run()