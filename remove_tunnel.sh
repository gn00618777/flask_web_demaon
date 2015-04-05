#!/bin/bash

sed -i "s/^$1$//g" tunnel_list
sed -i '/^$/d' tunnel_list

cd /etc/ppp/peers
rm $1


