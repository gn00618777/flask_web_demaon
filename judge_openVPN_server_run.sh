#!/bin/bash

s=`/etc/init.d/openvpn status | grep server | grep not`
if [ "$s" != "" ]; then
    echo "0"
else
    echo "1"
fi
