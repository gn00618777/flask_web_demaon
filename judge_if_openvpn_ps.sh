#!/bin/bash

str=`ps aux | grep "openvpn" | grep -c "openvpn --config"`


if [ "$str" == "1" ]; then
   echo "0"
else
   echo "1"
fi
