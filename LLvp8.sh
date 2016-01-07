#!/bin/bash

rm LLvp8.out
rm powerapi.out
rm LLvp8.png

vlc losslessvp8.webm &
VLCPID=$!
./bin/powerapi 84 100 $VLCPID &
POWERPID=$!
sleep 15;
kill $VLCPID
kill $POWERPID

./script.sh
mv data.out LLvp8.out

gnuplot LLvp8.conf
