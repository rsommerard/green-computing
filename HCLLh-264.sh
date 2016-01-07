#!/bin/bash

rm HCLLh-264.out
rm powerapi.out
rm HCLLh-264.png

vlc veryslowLosslessH264.mp4 &
VLCPID=$!
./bin/powerapi 84 100 $VLCPID &
POWERPID=$!
sleep 12;
kill $VLCPID
kill $POWERPID

./script.sh
mv data.out HCLLh-264.out

gnuplot HCLLh-264.conf
