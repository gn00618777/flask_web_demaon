#!/bin/bash

cd /etc/openvpn

domain_replaced=`cat server.conf | grep "\bserver\b" | sed "s/255.255.255.0//g" | sed "s/server//g" | sed "s/^.//g"`

if [ "$1" == "10_8" ]; then
    sed -i "s/$domain_replaced/10.8.0.0 /g" server.conf
fi

if [ "$1" == "192_168" ]; then
    sed -i "s/$domain_replaced/192.168.30.0 /g" server.conf
fi

maxclient_replaced=`cat server.conf | grep "max-clients"`

if [ "$2" == "5" ]; then
    sed -i "s/$maxclient_replaced/max-clients 5/g" server.conf
fi

if [ "$2" == "10" ]; then
    sed -i "s/$maxclient_replaced/max-clients 10/g" server.conf
fi

if [ "$2" == "15" ]; then
    sed -i "s/$maxclient_replaced/max-clients 15/g" server.conf
fi



