#!/bin/bash

rm mpeg-4_part14.out
rm powerapi.out
rm mpeg-4_part14.png

vlc bsk.m4v &
VLCPID=$!
./bin/powerapi 84 100 $VLCPID &
POWERPID=$!
sleep 12;
kill $VLCPID
kill $POWERPID

./script.sh
mv data.out mpeg-4_part14.out

gnuplot mpeg-4_part14.conf
