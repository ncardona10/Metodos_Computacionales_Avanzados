#include <iostream>
#include <fstream>
#include <ctime>
#include <chrono>
using namespace std; 

int main(int argc, char const *argv[])
{
    auto t1 = chrono::high_resolution_clock::now();
    /* code */
    //lee el archivo
    ifstream file;
    file.open(argv[1], ios::in);
    //guarda en un contador el numero de veces que la cadena aparece
    int cadenas[5] = {0,0,0,0,0};
    int cont = 0;

    char a; file.get(a);
    while(!file.eof()){
        if(a-'0'==1){
            cont=1;
            cadenas[0]++;
        }
        else{
            if(a-'0'==cont+1){
                cadenas[cont]++;
                cont++;
                if(cont==5){
                    cont=0;
                }
            }          
            else{
                cont=0;
            }
        }
        file.get(a);
    }
    //escribe los resultados del contador que guardo para cada cadena, en el orden
    //1,12,123,1234,12345
    
    ofstream newFile;
    newFile.open(argv[2]);
    for(int i=0;i<5;i++){
        newFile << cadenas[i] << endl;
    }
    newFile.close();

    ofstream newT;
    newT.open(argv[3],ios_base::app);
    auto t2 = chrono::high_resolution_clock::now();
    chrono::duration<int64_t,nano> elapsed = t2 - t1; 
    newT << elapsed.count()  << endl;
    newT.close();

    return 0;
}
    

