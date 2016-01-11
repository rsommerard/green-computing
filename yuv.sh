#!/bin/bash

rm yuv.out
rm powerapi.out
rm yuv.png

vlc video/bsk.yuv &
VLCPID=$!
./bin/powerapi 84 100 $VLCPID &
POWERPID=$!
sleep 12;
kill $VLCPID
kill $POWERPID

./script.sh
mv data.out yuv.out

gnuplot yuv.conf
