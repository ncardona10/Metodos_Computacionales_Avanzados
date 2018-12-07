#!/bin/bash
#PBS -l nodes=1:ppn=4,mem=1gb,walltime=00:10:00
#PBS -M n.cardonac@uniandes.edu.co
#PBS -m abe
#PBS -j oe


module load anaconda/python3 
module load gcc/4.9.4 
module load openmpi/1.8.5
cd /hpcfs/home/fisi4028/n.cardonac/NathaliaCardona_Ejercicio30/clase

#compila y ejecuta adveccion en serial
g++ adveccionSerial.c -o adveccionSerial.x -std=c++11
./adveccionSerial.x > adveccionSerial.txt
#compila y ejecuta adveccion en paralelo
g++ -fopenmp adveccionParallel.c -o adveccionParallel.x -std=c++11
./adveccionParallel.x > adveccionParallel.txt
#grafica
python3 grafica.py 
#compila y ejecuta walk paralelo
gcc -fopenmp walkParallel.c -o walkParallel.x
./walkParallel.x > walkParallel.txt 
#compila y ejecuta walk serial
gcc walkSerial.c -o walkSerial.x
./walkSerial.x > walkSerial.txt 
#histograma
python3 hist.py 