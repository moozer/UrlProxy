'''
Created on 14 Mar 2013

@author: moz

Using 
- flask httpd: http://flask.pocoo.org/
- requests: http://docs.python-requests.org/en/latest/
-- Stock debian unstable version is not new enough. 
-- Get version 1.10 from experimental: http://packages.debian.org/experimental/all/python-requests/download

'''

from flask import Flask, Response
from flask.templating import render_template
from flask.helpers import url_for, send_from_directory
from flask.globals import request
import requests
from werkzeug.utils import redirect
import werkzeug
import time
app = Flask(__name__)

@app.route("/")
def index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route("/ProcessRedirect")
def ProcessRedirect():
    URL = request.args['urltoget']
    return redirect(URL)

@app.route("/Stream")
def Stream():
    ''' reads and streams the data from the URL in chunks (as opposed to everything at once '''
    
    def ReadChunks( req, chunk_size = 1000 ):
        ''' generator the returns the chunks '''
        for data in req.iter_content(chunk_size=chunk_size, decode_unicode=False):
            time.sleep(0.5) # insert a sleep to make effect obvious
            yield data
    
    URL = request.args['urltoget']
    chunk_size = 1000 # a random size, could be a parameter.
    
    try:
        r = requests.get(URL, stream=True)
        return Response(ReadChunks(r, chunk_size), mimetype=r.headers['content-type'])
    
    except Exception, e:
        return "Bad stuff happened while fetching %s (%s)"%(URL, e)

    

if __name__ == "__main__":
    app.run()