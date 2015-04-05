#!/bin/bash

str=`ps aux | grep "openvpn" | grep "openvpn \n-\n-config"`


if [ "$str" == "" ]; then
   echo "0"
else
   echo "1"
fi
