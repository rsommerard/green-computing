#!/bin/bash

rm mkv.csv
rm powerapi.out
rm mkv.png

vlc SampleVideo_1080x720_1mb.mkv &
VLCPID=$!
./bin/powerapi 84 100 $VLCPID &
POWERPID=$!
sleep 10;
kill $VLCPID
kill $POWERPID

./script.sh
mv data.csv mkv.csv

gnuplot mkv.conf
