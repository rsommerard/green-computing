#!/bin/bash

./mp4.sh
./mkv.sh
./flv.sh

gnuplot all.conf
