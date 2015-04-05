#!/bin/bash

pid=`ps | grep "openvpn" | sed "s/t.*$//g" | sed "s/^.//g"`

kill $pid
