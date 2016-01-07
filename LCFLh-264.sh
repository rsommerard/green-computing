#!/bin/bash

rm LCFLh-264.out
rm powerapi.out
rm LCFLh-264.png

vlc ultrafastFulllossH264.mp4 &
VLCPID=$!
./bin/powerapi 84 100 $VLCPID &
POWERPID=$!
sleep 12;
kill $VLCPID
kill $POWERPID

./script.sh
mv data.out LCFLh-264.out

gnuplot LCFLh-264.conf
