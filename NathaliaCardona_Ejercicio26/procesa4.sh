#!/bin/bash
#PBS -l nodes=1:ppn=4,mem=1gb,walltime=00:10:00
#PBS -M n.cardonac@uniandes.edu.co
#PBS -m abe


module load anaconda/python3
module load gcc/4.9.4
cd /hpcfs/home/fisi4028/n.cardonac/NathaliaCardona_Ejercicio26
./correr.sh 4


