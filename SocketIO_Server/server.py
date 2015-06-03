import time
import serial
from flask import Flask, render_template, redirect
from flask.ext.socketio import SocketIO, emit
from threading import Thread 

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

def background_serial(port,rate):

    count=0

    if port == "com1":
       
       ser = serial.Serial("/dev/ttyO2", baudrate=rate, timeout=1)
    
    else:

       ser = serial.Serial("/dev/ttyO1",baudrate=rate, timeout=1)  

    while True:
        data = ser.read()

        if len(data) > 0:
           socketio.emit('my response', {'data':data}, namespace='/test')
           count=0
        else:
           count = count + 1
           if count == 60:
              socketio.emit('my response',{'data': '<br><h2>This page is time out</h2>'},namespace='/test')
              break

def background_openvpn_connect_state():

    time.sleep(3)

    fdout = open('bernieout','r')

    for line in open('bernieout'):
        time.sleep(0.5)
        line = fdout.readline()
        socketio.emit('my response', {'data':line+"<br>"}, namespace='/test')

    fdout.close()



@app.route('/<string:argument>')
def into_receiver(argument):
   
    if "com1" in argument and "9600" in argument:
       thread = Thread(target=background_serial, args=("com1","9600",))
       thread.start()
       return render_template('socketio_receive.html')

    if "com1" in argument and "115200" in argument:
       thread = Thread(target=background_serial, args=("com1","115200",)) 
       thread.start()
       return render_template('socketio_receive.html')
   
    if "com2" in argument and "9600" in argument: 
       thread = Thread(target=background_serial, args=("com2","9600",))
       thread.start()
       return render_template('socketio_receive.html')

    if "com2" in argument and "115200" in argument:
        thread = Thread(target=background_serial, args=("com2","115200",))
        thread.start()
        return render_template('socketio_receive.html')

    if argument == "openvpn_connect_state":
       thread = Thread(target=background_openvpn_connect_state)
       thread.start()
       return render_template('openVPN_client_state.html')

@app.route("/disconnect_ovpn_from_server",methods=['GET','POST'])
def disconnect_ovpn_from_server():
    import subprocess
    subprocess.call(['./disconnect_ovpn_from_server.sh'],stdout=subprocess.PIPE,stderr=subprocess.PIPE)

    return redirect('http://192.168.30.1:1300/PPTP_Server.html')


@socketio.on('disconnect',namespace='/test')
def test_distconnect():
    print('Client disconnected')

if __name__ == '__main__':
    socketio.run(app, host='192.168.30.1', port=1400)
