#!/bin/bash

cd static/report/flexmonkey/html/

declare -i number

number=`echo $1 | sed "s/^.*t//g"`

declare -i base

base=35

declare -i line

line=$number+$base

judgestr=`cat client_config_dir.html | grep -n "remove_config_client$number"`
judgestrnum=`echo $judgestr | sed "s/:.*$//g"`

sed -i "$judgestrnum d" client_config_dir.html
sed -i "$line a <form action=\"remove_config_client$number\" method=\"post\">client$number has subnet: $2</form>" client_config_dir.html

cd /etc/openvpn/servers/server/ccd/
if [ "$2" != "" ]; then
   echo "iroute $2 255.255.255.0" > client$number
else
    rm client$number
fi

cd /etc/openvpn/
    sameclient=`cat server.conf | grep ";client$number"`
    if [ "$sameclient" == "" ]; then
        if [ "$2" != "" ]; then
            echo "route $2 255.255.255.0 ;client$number" >> server.conf
            echo "push \"route $2 255.255.255.0\" ;Client$number" >> server.conf
        fi
    else
        if [ "$2" != "" ]; then
           replaced_client=`cat server.conf | grep ";client$number"`
           sed -i "s/$replaced_client/route $2 255.255.255.0 ;client$number/g" server.conf
           Replaced_client=`cat server.conf | grep ";Client$number"`
           sed -i "s/$Replaced_client/push \"route $2 255.255.255.0\" ;Client$number/" server.conf
        else
            replaced_client=`cat server.conf | grep ";client$number"`
            sed -i "s/$replaced_client//g" server.conf
            sed -i "/^$/d" server.conf
            Replaced_client=`cat server.conf | grep ";Client$number"`
            sed -i "s/$Replaced_client//g" server.conf
            sed -i "/^$/d" server.conf

        fi
    fi

