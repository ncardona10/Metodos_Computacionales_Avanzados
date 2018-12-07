#!/bin/bash
#PBS -l nodes=1:ppn=2,mem=1gb,walltime=00:10:00
#PBS -M n.cardonac@uniandes.edu.co
#PBS -m abe


module load anaconda/python3
module load gcc/4.9.4
cd /hpcfs/home/fisi4028/n.cardonac/NathaliaCardona_Ejercicio28
mpicc integra.c -o integra.x
mpiexec -np 4 ./integra.x 1000 >> data.dat
mpiexec -np 4 ./integra.x 10000 >> data.dat 
mpiexec -np 4 ./integra.x 100000 >> data.dat 
mpiexec -np 4 ./integra.x 1000000 >> data.dat 
mpiexec -np 4 ./integra.x 10000000 >> data.dat 
mpiexec -np 4 ./integra.x 100000000 >> data.dat 
python3 grafica.py
