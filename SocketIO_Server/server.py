import time
from flask import Flask, render_template
from flask.ext.socketio import SocketIO, emit
from threading import Thread 

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)
thread = None

def background_thread():
    count = 0
    for i in range(5):
        time.sleep(10)
        count += 1
        socketio.emit('my response',{'data':'Server generated event','count':count},namespace='/test')

@app.route('/')
def into_receiver():
    global thread
    if thread is None:
       thread = Thread(target=background_thread)
       thread.start()
    return render_template('socketio_receive.html')

@socketio.on('connect', namespace='/test')
def test_connect():
    emit('my response', {'data':'Connected'})

@socketio.on('disconnect',namespace='/test')
def test_distconnect():
    print('Client disconnected')

if __name__ == '__main__':
    socketio.run(app, host='172.16.51.22', port=1400)
