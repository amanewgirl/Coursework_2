from flask import Flask, redirect, url_for, abort,render_template, send_from_directory, request
from flask_socketio import SocketIO, send

app=Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'
socketio = SocketIO(app)

@socketio.on('message')
def handleMessage(msg):
    print('Message:' +msg)
    send(msg, broadcast=True)

@app.route('/in')
def index():
    return render_template('index.html')


if __name__ =="__main__":
   socketio.run(app, host='0.0.0.0')
   