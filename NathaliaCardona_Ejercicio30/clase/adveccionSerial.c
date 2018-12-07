#include <stdio.h>
#include <array>
#include <algorithm>
#include <iterator>
#include <omp.h>
#include <fstream>
#include <iostream>
using namespace std;

//constantes
double dx = 0.05;
double l = 4.0;
int n = (int)(l/dx + 1);

//metodos
double flux(double u){
  double f = 0.5*u*u;
  return f; 
}

void lax(double t_max, double dt, double *u ){
  int nt = (int)(t_max/dt);
  double u_new[n];
  copy(u, u + n, u_new);
  
  for(int i = 0; i < nt; i++){
      double f[n];    
      for(int k = 0; k < n; k++){
        f[k] = flux(u[k]);      
      }
      
      for(int j = 1; j < n-1; j++){
        u_new[j] = 0.5*(u[j+1] + u[j-1]);
        u_new[j] -= (0.5*dt/dx)*(f[j+1] - f[j-1]);
      }
      copy(u_new, u_new + n, u);
    }
}


int main(int argc, char const *argv[])
{
  /* code */
  double t_max = 1.0;
  
  //for(int i = 0; i < 4; i++){
    double x[n];
    double u[n];
    
    for(int k = 0; k < n; k++){
      x[k]=4.0*k/(n-1.0);
      // cout<<x[k] <<endl;
      if(x[k]<2.0){
        u[k]=1.0;
      }
      else{
        u[k]=0.0;
      }
      // cout<<u[k]<<endl;
    }

    double dt = 0.5*dx;
    lax(t_max, dt, u);
    for(int m = 0; m < n; m++){
      cout << u[m] << " ";      
    }
    cout << endl;
  //}  
  
  return 0;
}

