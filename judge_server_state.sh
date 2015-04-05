#!/bin/bash

str=`/etc/init.d/openvpn status | grep "server" | grep "not"`

if [ "$str" == "" ]; then
   echo "1"
else
   echo "0"
fi

