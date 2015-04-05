#!/bin/bash

if [ "$1" == "low" ]; then
   
     echo "0" > /sys/class/gpio/gpio196/value    

elif [ "$1" == "high" ]; then

     echo "1" > /sys/class/gpio/gpio196/value

else 
     echo ""

fi


