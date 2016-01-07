#!/bin/bash

rm HCh-265.out
rm powerapi.out
rm HCh-265.png

vlc placeboH265.mp4 &
VLCPID=$!
./bin/powerapi 84 100 $VLCPID &
POWERPID=$!
sleep 12;
kill $VLCPID
kill $POWERPID

./script.sh
mv data.out HCh-265.out

gnuplot HCh-265.conf
