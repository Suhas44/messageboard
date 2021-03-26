#!/usr/bin/env python3

# Imports
from flask import Flask,render_template,request,flash,redirect,url_for
from datetime import datetime
import os

# Setup
app = Flask(__name__)
sepr="#$%"
path="./messages"

if not os.path.isfile(path):
  f=open(path,'x')
  f.close()

def write(name,subject,message):
    f = open(path,'a')
    f.write(f'{name}{sepr}{subject}{sepr}{message}\n')
    f.close()

def read():
    f = open(path,'r')
    messages = []
    for l in f:
        l = l.split(sepr)
        messages.append(tuple(l))
    return messages

# Home page
@app.route('/',methods=['GET','POST']) 
def rules():
    if request.method == 'POST':
        name = request.form['name'].replace(sepr, "")
        message = request.form['msg'].replace(sepr, "")
        subject = request.form['subject'].replace(sepr, "")
        write(name,subject,message)

    return render_template('index.html', messages=read())
    


# Entry
if __name__ == '__main__':

    app.run(debug=True) # Run with debug