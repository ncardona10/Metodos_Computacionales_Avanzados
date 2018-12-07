#!/bin/bash
#PBS -l nodes=1:ppn=4,mem=1gb,walltime=00:10:00
#PBS -M n.cardonac@uniandes.edu.co
#PBS -m abe
#PBS -j oe


module load anaconda/python3 
module load gcc/4.9.4 
module load openmpi/1.8.5
cd /hpcfs/home/fisi4028/n.cardonac/NathaliaCardona_Ejercicio29/clase

#compila y ejecuta el codigo de c que usa mp
gcc -fopenmp HelloWorld.c -o helloWorld.x
./helloworld.x >> helloworld.dat
#compila y ejecuta adveccion
g++ adveccion.c -o adveccion.x -std=c++11
./adveccion.x >> adveccion.dat
#grafica
python3 grafica.py 