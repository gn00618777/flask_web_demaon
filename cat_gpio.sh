#!/bin/bash

str=`cat /sys/kernel/debug/gpio | grep "gpio-19"`

echo "$str"
