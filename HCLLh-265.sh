#!/bin/bash

rm HCLLh-265.out
rm powerapi.out
rm HCLLh-265.png

vlc veryslowLosslessH265.mp4 &
VLCPID=$!
./bin/powerapi 84 100 $VLCPID &
POWERPID=$!
sleep 12;
kill $VLCPID
kill $POWERPID

./script.sh
mv data.out HCLLh-265.out

gnuplot HCLLh-265.conf
