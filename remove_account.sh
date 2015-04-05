#!/bin/bash

line_removed_PPP_Account_html=`cat static/report/flexmonkey/html/PPP_Account.html | grep -n "$1" | sed "s/:<.*$//g"`

sed -i "$line_removed_PPP_Account_html d" static/report/flexmonkey/html/PPP_Account.html

account_name=`echo "$1" | sed "s/-.*$//g"`
server_name=`echo "$1" | sed "s/^.*-//g"`

line_removed_chap_secrets=`cat /etc/ppp/chap-secrets | grep -n "\b$account_name\b" | grep "\b$server_name\b" | sed "s/:.*$//g"`

sed -i "$line_removed_chap_secrets d" /etc/ppp/chap-secrets

