#!/bin/bash

# add new account in PPP_Account.html
server_name=`cat /etc/ppp/pptpd-options | grep "^name" | sed 's/^.* //g'`
judge_string=`cat /etc/ppp/chap-secrets | grep "\b$1\b" | grep "\b$server_name\b"`

if [ "$judge_string" == "" ]; then

sed -i "10a <tr><td class=\"hdrl\"><input type=\"checkbox\" value=\"$1-$server_name\" name=\"account\">$1</input></td><td class=\"hdrl\"><center>$server_name</center></td><td class=\"hdrl\"><center>$2</center></td><td class=\"hdrl\">Anyone</td></tr>" static/report/flexmonkey/html/PPP_Account.html

# add new account in chap-secrets file
  echo "$1 $server_name $2 \"*\"" >> /etc/ppp/chap-secrets

fi

