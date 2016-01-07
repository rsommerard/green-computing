#!/bin/bash

rm LLvp9.out
rm powerapi.out
rm LLvp9.png

vlc losslessvp9.webm &
VLCPID=$!
./bin/powerapi 84 100 $VLCPID &
POWERPID=$!
sleep 15;
kill $VLCPID
kill $POWERPID

./script.sh
mv data.out LLvp9.out

gnuplot LLvp9.conf
