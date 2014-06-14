#!/usr/bin/env bash 

map=data/caporaso-gut.txt
data=data/caporaso-gut.biom
tdir=time-results
{ time supervised_learning.py -i $data -m $map -c SEX -o qiime-dir/ -f ; } 2> $tdir/qiime.time

for selects in `seq 100 100 1000`; do 
  echo "Running $selects"
  { time fizzy -i $data -m $map -l SEX -o mim/mim-$selects.txt -n $selects -f MIM ; } 2> $tdir/mim-$selects.time
  { time fizzy -i $data -m $map -l SEX -o jmi/jmi-$selects.txt -n $selects -f JMI ; } 2> $tdir/jmi-$selects.time
done
