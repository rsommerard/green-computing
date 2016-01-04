#!/bin/bash

./mpeg-4_part14.sh
./h-264.sh
./vp8.sh
./yuv.sh

python compute_video.py

gnuplot video.conf
