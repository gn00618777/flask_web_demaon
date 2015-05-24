#!/bin/bash

pid=`ps aux | grep "\bclient.ovpn\b" | sed "s/ [0-99]\..*$//g" | sed "s/root//g"`

kill $pid
