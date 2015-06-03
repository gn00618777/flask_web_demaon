#!/bin/bash

if [ "$1" == "com1" ]; then

     echo "1" > /sys/class/gpio/gpio102/value

else
   
     echo "1" > /sys/class/gpio/gpio13/value

fi
