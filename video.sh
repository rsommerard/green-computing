#!/bin/bash

chmod +x *.sh
./mpeg-4_part14.sh
./h-264.sh
./vp8.sh
./vp9.sh
./LLvp8.sh
./LLvp9.sh
./LCh-265.sh
./HCh-265.sh
./LCFLh-264.sh
./LCFLh-265.sh
./HCFLh-264.sh
./HCFLh-265.sh
./LCLLh-264.sh
./LCLLh-265.sh
./HCLLh-264.sh
./HCLLh-265.sh
./yuv.sh

python compute_video.py

gnuplot video.conf
