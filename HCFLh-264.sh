#!/bin/bash

rm HCFLh-264.out
rm powerapi.out
rm HCFLh-264.png

vlc veryslowFulllossH264.mp4 &
VLCPID=$!
./bin/powerapi 84 100 $VLCPID &
POWERPID=$!
sleep 12;
kill $VLCPID
kill $POWERPID

./script.sh
mv data.out HCFLh-264.out

gnuplot HCFLh-264.conf
