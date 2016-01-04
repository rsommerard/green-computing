#!/bin/bash

rm h-264.out
rm powerapi.out
rm h-264.png

vlc bsk.mp4 &
VLCPID=$!
./bin/powerapi 84 100 $VLCPID &
POWERPID=$!
sleep 12;
kill $VLCPID
kill $POWERPID

./script.sh
mv data.out h-264.out

gnuplot h-264.conf
