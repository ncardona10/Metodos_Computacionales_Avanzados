#include <iostream>
#include <random>
#include <fstream>
#include <sstream>
#include <math.h>
#include <string>
#include <stdlib.h>
#include <omp.h>
using namespace std;

//Funciones
//Numeros aleatorios entre 0 y 1
double generarNum(){
    return ((double)rand()/RAND_MAX);
}

//Funcion gaussiana
double gauss(double x, double mu, double sigma){
    double g = 1/pow(2.0*M_PI*sigma*sigma,0.5)*exp(-pow(x-mu,2.0)/(2.0*sigma*sigma));
    return (g);
}

void printNum(int n, double mu, double sigma){      
    #pragma omp parallel num_threads(8)
    {
        int rank = omp_get_thread_num();
        //abre el archivo
        ofstream myFile;
        myFile.open("sample_"+ to_string(rank+1)+".dat");
        //Array 
        double *num = new double[n]; 
        //Inicializa num con la media
        num[0] = mu;
        myFile << to_string(num[0]) << endl;
        //Itera sobre los n-1 samples, utilizando metropolis hastings para filtrar los candidatos
        for(int i = 1; i<n; i++){
            double dn = (generarNum() - 0.5)*sigma;
            //cout<<dn<<endl;
            double temp = num[i-1] + dn;
            //Aplicar MH 
            double alpha = gauss(temp, mu, sigma) / gauss(num[i-1], mu, sigma);
            double temp2 = generarNum();
            if(temp2<=alpha){
                num[i] = temp;
            }
            else{
                num[i] = num[i-1];
            }
            myFile << to_string(num[i]) << endl;
        }
        myFile.close();
    }
}

main(int argc, char *argv[])
{

    
    //Parametros de la gaussiana
    int n = 1000;
    double mu = 0;
    double sigma = 1;
    
    //Llama a la funcion que imprime los numeros aleatorios y los escribe en los archivos
    printNum(n,mu,sigma);
    

    
    return 0;
}