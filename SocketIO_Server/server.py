import time
import serial
from flask import Flask, render_template
from flask.ext.socketio import SocketIO, emit
from threading import Thread 

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

def background_thread(rate):
    
    count=0

    ser = serial.Serial("/dev/ttyO2", baudrate=rate, timeout=1)
 
    while True:
        data = ser.read()
   
        if len(data) > 0:
           socketio.emit('my response',{'data':data},namespace='/test')
           count=0
        else:
           count=count+1
           if count == 60:
              socketio.emit('my response',{'data': '<br><h2>This page is time out</h2>'},namespace='/test')
              break

@app.route('/<string:baudrate>')
def into_receiver(baudrate):

    thread = Thread(target=background_thread, args=(baudrate,))
    thread.start()
    return render_template('socketio_receive.html')


@socketio.on('disconnect',namespace='/test')
def test_distconnect():
    print('Client disconnected')

if __name__ == '__main__':
    socketio.run(app, host='172.16.51.22', port=1400)
