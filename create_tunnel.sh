#!/bin/bash

cd /etc/ppp/peers/

echo "pty \"pptp $2 --nolaunchpppd\"" > $1
echo "name $3" 1>> $1
echo "remotename $5" 1>> $1
echo "require-mppe-40" 1>> $1
echo "require-mppe-128" 1>> $1
echo "file /etc/ppp/options.pptp" 1>> $1
echo "ipparam $1" 1>> $1

cd /flask_web_demaon
tunnel_name=`cat tunnel_list | grep "^$1$"`
if [ "$tunnel_name" == "" ]; then
   echo "$1" 1>> tunnel_list
fi

cd /etc/ppp/
account=`cat chap-secrets | grep "\b$3\b" | grep "\b$5\b" | grep "\b$4\b"`
if [ "$account" == "" ]; then
   echo "$3 $5 $4 *" 1>> chap-secrets
fi
