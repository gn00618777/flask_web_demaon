#!/bin/bash

str=`ps aux | grep "openvpn" | grep -c "client.ovpn"`


if [ "$str" == "0" ]; then
   echo "0"
else
   echo "1"
fi
