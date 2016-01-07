#!/bin/bash

rm HCFLh-265.out
rm powerapi.out
rm HCFLh-265.png

vlc veryslowFulllossH265.mp4 &
VLCPID=$!
./bin/powerapi 84 100 $VLCPID &
POWERPID=$!
sleep 12;
kill $VLCPID
kill $POWERPID

./script.sh
mv data.out HCFLh-265.out

gnuplot HCFLh-265.conf
