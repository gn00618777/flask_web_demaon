#!/bin/bash



if [  "$1" == "rs232" ]; then

      echo "1" > /sys/class/gpio/gpio200/value
      echo "0" > /sys/class/gpio/gpio201/value
      echo "0" > /sys/class/gpio/gpio202/value
      echo "0" > /sys/class/gpio/gpio203/value 
     
      echo "1" > /sys/class/gpio/gpio204/value
      echo "0" > /sys/class/gpio/gpio205/value
      echo "0" > /sys/class/gpio/gpio206/value
      echo "0" > /sys/class/gpio/gpio207/value
      exit 0

fi

if [ "$1" == "rs422" ]; then

     echo "1" > /sys/class/gpio/gpio200/value
     echo "1" > /sys/class/gpio/gpio201/value
     echo "1" > /sys/class/gpio/gpio202/value
     echo "1" > /sys/class/gpio/gpio203/value

     echo "1" > /sys/class/gpio/gpio204/value
     echo "1" > /sys/class/gpio/gpio205/value
     echo "1" > /sys/class/gpio/gpio206/value
     echo "1" > /sys/class/gpio/gpio207/value
     exit 0

fi

if [ "$1" == "rs485" ]; then
  
     echo "0" > /sys/class/gpio/gpio200/value
     echo "1" > /sys/class/gpio/gpio201/value
     echo "0" > /sys/class/gpio/gpio202/value
     echo "1" > /sys/class/gpio/gpio203/value

     echo "0" > /sys/class/gpio/gpio204/value
     echo "1" > /sys/class/gpio/gpio205/value
     echo "0" > /sys/class/gpio/gpio206/value
     echo "1" > /sys/class/gpio/gpio207/value 
     exit 0

fi
