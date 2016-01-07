#!/bin/bash

rm LCLLh-265.out
rm powerapi.out
rm LCLLh-265.png

vlc utlrafastLosslessH265.mp4 &
VLCPID=$!
./bin/powerapi 84 100 $VLCPID &
POWERPID=$!
sleep 12;
kill $VLCPID
kill $POWERPID

./script.sh
mv data.out LCLLh-265.out

gnuplot LCLLh-265.conf
