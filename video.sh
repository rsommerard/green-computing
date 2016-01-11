#!/bin/bash

chmod +x *.sh

./lecteur.sh

python compute_video.py

echo "set terminal png size 1024,768 enhanced font \"Helvetica,20\"
set output 'average.png'

set ylabel \"Power (mW)\"

set style fill solid border
set style data histogram
set style histogram clustered
plot for [COL=2:7] \"average.out\" using COL:xticlabels(1)  title columnheader" > video.conf

gnuplot video.conf
