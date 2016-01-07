#!/bin/bash

rm LCh-265.out
rm powerapi.out
rm LCh-265.png

vlc ultrafastH265.mp4 &
VLCPID=$!
./bin/powerapi 84 100 $VLCPID &
POWERPID=$!
sleep 12;
kill $VLCPID
kill $POWERPID

./script.sh
mv data.out LCh-265.out

gnuplot LCh-265.conf
