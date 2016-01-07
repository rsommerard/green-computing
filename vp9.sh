#!/bin/bash

rm vp9.out
rm powerapi.out
rm vp9.png

vlc ConstantQualityvp9.webm &
VLCPID=$!
./bin/powerapi 84 100 $VLCPID &
POWERPID=$!
sleep 15;
kill $VLCPID
kill $POWERPID

./script.sh
mv data.out vp9.out

gnuplot vp9.conf
