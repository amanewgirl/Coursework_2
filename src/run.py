import os
from flask import Flask, redirect, url_for, abort,render_template, send_from_directory, request
from os.path import basename



@app.route ("/")
def sending():
    return render_template ("test.html")

@app.route ("/talk",methods = ['POST', 'GET'])
def recieving(input=None):
    if request.method == 'POST':
	user = request.form
	return render_template('testtalk.html', user = user) 


@app.route ("/hello/")
def hello():
    name = request.args.get ('name','')
    if name =='':
       return "no param supplied "
    else :
       return " Hello %s" % name


def hello():
    name = request.args.get ('name','')
    if name =='':
       return "no param supplied "
    else :
       return " Hello %s" % input

if __name__ =="__main__":
      app.run(host='0.0.0.0', debug = True)

