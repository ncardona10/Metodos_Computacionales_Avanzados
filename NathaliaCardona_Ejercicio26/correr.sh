#!/bin/bash

#compila el codigo en c++
g++ cuenta.c -o cuenta.x -std=c++11

#genera las particiones 
python3 archivos.py 

#corre el codigo en c++ para todas las particiones
for part in {1,10,20,50,100};
do 
    #guarda el tiempo en que comienza a correr
    ti=$(($(date +%s%N)/1000000))
    

    cd "part"$part 
    for ((i=1;i<= part;i++));
    do 
        .././cuenta.x "pi"$i".txt" cuenta.txt tiempo.txt & 
    done 
    cd .. 
    sleep 3

    #guarda el tiempo en que finaliza y calcula el tiempo total
    tf=$(($(date +%s%N)/1000000))

    dt=$(($tf-$ti))
    echo $part $dt >> tiempos.txt 
    cat ./"part"$part/tiempo.txt >> ./"timePart"$part"p"$1".txt"
    rm -rf "part"$part
done 

#python3 grafica.py 




