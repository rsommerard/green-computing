#!/bin/bash

exec 1> data.csv

i=0
for line in $(cat powerapi.out)
do
    #timestamp=`echo $line | cut -f 2 -d ";" | cut -f 2 -d "="`
    power=`echo $line | cut -f 5 -d ";" | cut -f 2 -d "="`
    #echo "$timestamp $power"
    echo "$i $power"
    let "i=i+1"
done
