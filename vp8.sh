#!/bin/bash

rm vp8.out
rm powerapi.out
rm vp8.png

vlc bsk.webm &
VLCPID=$!
./bin/powerapi 84 100 $VLCPID &
POWERPID=$!
sleep 15;
kill $VLCPID
kill $POWERPID

./script.sh
mv data.out vp8.out

gnuplot vp8.conf
