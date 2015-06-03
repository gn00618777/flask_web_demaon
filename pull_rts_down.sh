#!/bin/bash

if [ "$1" == "com1" ]; then 

   echo "0" > /sys/class/gpio/gpio102/value

else

   echo "0" > /sys/class/gpio/gpio13/value

fi
