#!/bin/bash

rm mp4.out
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
mv data.out mp4.out

gnuplot mp4.conf
