#!/bin/bash

ovpndirectory=`echo $1 | sed "s/^.*-//g"`

cd ovpn_files/$ovpndirectory/

ovpn_file=`ls | grep ".ovpn"`

openvpn --config $ovpn_file &






