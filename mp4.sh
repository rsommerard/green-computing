#!/bin/bash

rm mp4.csv
rm powerapi.out
rm mp4.png

vlc SampleVideo_1080x720_1mb.mp4 &
VLCPID=$!
./bin/powerapi 84 100 $VLCPID &
POWERPID=$!
sleep 10;
kill $VLCPID
kill $POWERPID

./script.sh
mv data.csv mp4.csv

gnuplot mp4.conf
