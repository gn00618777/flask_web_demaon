#!/bin/bash

cd ovpn_files/

ovpndirectory=`echo $1 | sed "s/^.*-//g"`
rm -r $ovpndirectory/

sed -i "s/<option value=\"$1\">$ovpndirectory<\/option>//g" ../static/report/flexmonkey/html/connect_server_with_ovpn.html

sed -i "/^$/d" ../static/report/flexmonkey/html/connect_server_with_ovpn.html
