#include <iostream>
#include <random>
#include <fstream>
#include <math.h>
// #include <stdlib.h>
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



main(int argc, char const *argv[])
{

    
    //Parametros de entrada
    int n = atoi(argv[1]);
    double mu = atof(argv[2]);
    double sigma = atof(argv[3]);
    
    //Array 
    double *num = new double[n]; 

    //Inicializa num con la media
    num[0] = mu;
    cout << num[0] << endl;
    //Itera sobre los n-1 samples, utilizando metropolis hastings para filtrar los candidatos
    for(int i = 1; i<n; i++){
        double dn = (generarNum() - 0.5)*sigma;
        // cout<<dn<<endl;
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
        cout << num[i] << endl;
    }
    return 0;
}


