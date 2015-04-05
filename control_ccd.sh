#!/bin/bash


cd static/report/flexmonkey/html

declare -i base
declare -i base1
declare -i line
declare -i line1
declare -i count
declare -i line_removed
declare -i first_remove_config_client_line
base=13
base1=35

judge=`cat client_config_dir.html | grep "add_config_client"`

if [ "$judge" == "" ]; then

   if [ "$1" == "5" ]; then

       for  (( i=1; i<=5; i=i+1 ))
       do
           line=$base+$i
           sed -i "$line a <h1><form action=\"add_config_client$i\" method=\"post\">client$i's subnet:<input type=\"text\" name=\"subnet_text\"><input type=\"submit\" value=\"add\"></form></h1>" client_config_dir.html
       done

       for  (( j=1; j<=5; j=j+1 ))
       do
           line1=$base1+$j
           sed -i "$line1 a <form action=\"remove_config_client$j\" method=\"post\">client$j has subnet:</form>" client_config_dir.html
       done

   elif [ "$1" == "10" ]; then

        for  (( i=1; i<=10 ; i=i+1 ))
        do
           line=$base+$i
           sed -i "$line a <h1><form action=\"add_config_client$i\" method=\"post\">client$i's subnet:<input type=\"text\" name=\"subnet_text\"><input type=\"submit\" value=\"add\"></form></h1>" client_config_dir.html
        done

        for  (( j=1; j<=10; j=j+1 ))
        do
           line1=$base1+$j
           sed -i "$line1 a <form action=\"remove_config_client$j\" method=\"post\">client$j has subnet:</form>" client_config_dir.html
        done

   else
        for  (( i=1; i<=15; i=i+1 ))
        do
           line=$base+$i
           sed -i "$line a <h1><form action=\"add_config_client$i\" method=\"post\">client$i's subnet:<input type=\"text\" name=\"subnet_text\"><input type=\"submit\" value=\"add\"></form></h1>" client_config_dir.html
        done

        for  (( j=1; j<=15; j=j+1  ))
        do
           line1=$base1+$j
           sed -i "$line1 a <form action=\"remove_config_client$j\" method=\"post\">client$j has subnet:</form>" client_config_dir.html
        done
    fi
else
    count=`cat client_config_dir.html | grep -c "add_config_client"`
    line_removed=15+$count-1
    sed -i "15,$line_removed d" client_config_dir.html
    first_remove_config_client=`cat client_config_dir.html | grep -n "remove_config_client1\b"`
    first_remove_config_client_line=`echo $first_remove_config_client | sed "s/:.*$//g"`
    line_removed=$first_remove_config_client_line+$count-1
    sed -i "$first_remove_config_client_line,$line_removed d" client_config_dir.html

    cd /etc/openvpn/
    sed -i "s/^route.*$//g" server.conf
    sed -i "s/^push.*$//g" server.conf
    sed -i "/^$/d" server.conf
    echo "push \"route 192.168.30.0 255.255.255.0\" " >> server.conf

    cd /etc/openvpn/servers/server/ccd/
    rm client*

fi

