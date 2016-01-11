list_dir=`ls video`


for dir in $list_dir
do
echo $dir
file="video/$dir"
nom=`echo $dir | cut -d \. -f 1`

rm $nom.out
rm powerapi.out
rm $nom.png

vlc $file &
VLCPID=$!
./bin/powerapi 84 100 $VLCPID &
POWERPID=$!
sleep 12;
kill $VLCPID
kill $POWERPID

./script.sh
mv data.out $nom.out
echo "set autoscale fix
set key outside right center

set terminal png size 1024,768 enhanced font \"Helvetica,20\"
set output '$nom.png'

plot '$nom.out' title \"$nom\" with lines" > $nom.conf
gnuplot $nom.conf
done
