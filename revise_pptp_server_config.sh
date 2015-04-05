#!/bin/bash

cd /etc/ppp

server_name=`cat pptpd-options | grep "^name"`
sed -i "s/$server_name/name $1/g" pptpd-options

cd /etc

server_ip=`cat pptpd.conf | grep "^localip"`
sed -i "s/$server_ip/localip $2/g" pptpd.conf

clients_ip=`cat pptpd.conf | grep "^remoteip"`
sed -i "s/$clients_ip/remoteip $3/g" pptpd.conf



