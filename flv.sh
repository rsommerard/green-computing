#!/bin/bash

rm flv.csv
rm powerapi.out
rm flv.png

vlc SampleVideo_1080x720_1mb.flv &
VLCPID=$!
./bin/powerapi 84 100 $VLCPID &
POWERPID=$!
sleep 10;
kill $VLCPID
kill $POWERPID

./script.sh
mv data.csv flv.csv

gnuplot flv.conf
