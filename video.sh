#!/bin/bash

./mpeg-4_part14.sh
./h-264.sh
./vp8.sh
./vp9.sh
./LLvp8.sh
./LLvp9.sh
./yuv.sh

python compute_video.py

gnuplot video.conf
