#!/bin/bash

rm LCFLh-265.out
rm powerapi.out
rm LCFLh-265.png

vlc ultrafastfulllossH265.mp4 &
VLCPID=$!
./bin/powerapi 84 100 $VLCPID &
POWERPID=$!
sleep 12;
kill $VLCPID
kill $POWERPID

./script.sh
mv data.out LCFLh-265.out

gnuplot LCFLh-265.conf
