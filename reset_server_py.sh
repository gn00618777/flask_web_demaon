#!/bin/bash

pid=`ps aux | grep "\bserver.py\b" | sed "s/ [0-99]\..*$//g" | sed "s/root//g"`

kill $pid

python /flask_web_demaon/SocketIO_Server/server.py &

sleep 3


