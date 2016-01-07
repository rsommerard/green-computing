#!/bin/bash

rm LCLLh-264.out
rm powerapi.out
rm LCLLh-264.png

vlc utlrafastLosslessH264.mp4 &
VLCPID=$!
./bin/powerapi 84 100 $VLCPID &
POWERPID=$!
sleep 12;
kill $VLCPID
kill $POWERPID

./script.sh
mv data.out LCLLh-264.out

gnuplot LCLLh-264.conf
