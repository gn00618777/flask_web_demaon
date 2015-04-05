#!/bin/bash

cd ovpn_files/
 
tar -t -f $1 1> /dev/null

if [ "$?" == "0" ]; then

    filename=`echo "$1" | sed "s/\..*$//g"`
    cd ..
    cd static/report/flexmonkey/html/
    exitoption=`cat connect_server_with_ovpn.html | grep "$filename-$filename"`
    if [ "$exitoption" == ""  ]; then
         addlinenumber=`cat connect_server_with_ovpn.html | grep -n "\bovpn_files\b" | sed "s/:.*$//g"`
         sed -i "$addlinenumber"a" <option value=\"$filename-$filename\">$filename</option>" connect_server_with_ovpn.html
         removelinenumber=`cat connect_server_with_ovpn.html | grep -n "\bovpn_files1\b" | sed "s/:.*$//g"`
         sed -i "$removelinenumber"a" <option value=\"$filename-$filename\">$filename</option>" connect_server_with_ovpn.html
         cd  ../../../../ovpn_files/
         tar -x -f $1
         rm $1
     fi
    echo 0
fi

if [ "$?" != "0" ]; then
     rm $1
     echo 1

 fi

