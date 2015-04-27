import time
import serial
from flask import Flask, render_template, request
from flask.ext.socketio import SocketIO, emit
from threading import Thread 

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

def background_thread():
    
    fread = open('baud_rate','r')

    ser = serial.Serial("/dev/ttyO2", baudrate=fread.read(), timeout=3.0)
    while True:
        data = ser.read()
        if data == "^":
           socketio.emit('my response',{'data':'<br><br><h1>Stop Receive!</h1>'},namespace='/test') 
           break
        if len(data) > 0:
           socketio.emit('my response',{'data':data},namespace='/test')

@app.route('/')
def into_receiver():
    thread = Thread(target=background_thread)
    thread.start()
    return render_template('socketio_receive.html')

@socketio.on('connect', namespace='/test')
def test_connect():
    emit('my response', {'data':'<h1>SocketIO Connected!</h1><br><br>'})

@socketio.on('disconnect',namespace='/test')
def test_distconnect():
    print('Client disconnected')

if __name__ == '__main__':
    socketio.run(app, host='172.16.51.22', port=1400)
