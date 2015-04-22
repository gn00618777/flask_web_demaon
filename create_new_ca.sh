#!/bin/bash

rm /flask_web_demaon/static/report/flexmonkey/html/client_configs.tar
cd /etc/openvpn/easy-rsa
source vars
./clean-all

# create ca
(echo ""; echo ""; echo ""; echo ""; echo ""; echo ""; echo ""; echo "";) | ./build-ca

# create server key
common_name=`cat vars | grep "export KEY_CN"`
sed -i "s/$common_name/export KEY_CN=myserver/g" vars
source vars
./pkitool --server myserver

#create clients key
for (( i=1 ; i<=$1 ; i=i+1 ))
do
    common_name=`cat vars | grep "export KEY_CN"`
    echo "$common_name" >> recordCN
    sed -i "s/$common_name/export KEY_CN=client$i/g" vars
    source vars
    ./pkitool client$i
done

# package the requirements of client
cd /etc/openvpn/easy-rsa/keys
for (( i=1 ; i<=$1 ; i=i+1))
do
    mkdir user$i
    cp client$i.crt user$i/
    cp client$i.key user$i/
    cp ca.crt user$i/
    cp /etc/openvpn/dh1024.pem /etc/openvpn/easy-rsa/keys/user$i/
    # revise client.ovpn for each client
    cp /etc/openvpn/client.conf /etc/openvpn/client.ovpn
    sed -i "s/client1/client$i/g" /etc/openvpn/client.ovpn

    cp /etc/openvpn/client.ovpn /etc/openvpn/easy-rsa/keys/user$i/
    rm /etc/openvpn/client.ovpn
    cp -r user$i /flask_web_demaon/static/download/client_configs/
    rm -r user$i
done

cd /flask_web_demaon/static/download
tar -cv -f client_configs.tar client_configs/*
cp client_configs.tar /flask_web_demaon/static/report/flexmonkey/html/
rm -r /flask_web_demaon/static/download/client_configs/user*
rm client_configs.tar


