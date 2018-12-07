#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "mpi.h"

double generarNum(){
    return ((double)rand()/(double)RAND_MAX);
}

int main(int argc, char *argv[])
{
    int true=1; /* to force the loop */
    int n, //cantidad de puntos
        rank, /* rank of the MPI process */
        size, //numero de procesadores
        len; /* name of the process */
    double PI_VALUE = 155.0/6.0;
    double mypi, /* value for each process */
        pi, /* value of pi calculated */
        h,
        sum, /*sum of the area */
        x;
    double start_time, /* starting time */
        end_time, /* ending time */
        /* time for computing value of pi */
        computation_time;
    char name[80]; /* char array for storing the name of
        the node where is located the
        process */
    /*Initialization */
    MPI_Init(&argc,&argv);
    MPI_Comm_size(MPI_COMM_WORLD,&size);
    MPI_Comm_rank(MPI_COMM_WORLD,&rank);
    /* We ask for the name of the node */
    MPI_Get_processor_name(name, &len);

    // printf("entra al main");

    /*while (true)
    {*/
    if (rank == 0) {
        // printf("Enter the number of intervals: (0 quits)");
        // fflush(stdout);
        // scanf("%d",&n);
        // start_time = MPI_Wtime();
        n = atoi(argv[1]);
    }
    MPI_Bcast(&n, 1, MPI_INT, 0, MPI_COMM_WORLD);
    int puntos_procesador = n/size;
    double suma = 0;
    int i;
    for(i= 0;i<puntos_procesador;i++){
        double x0 = generarNum();
        double x1 = generarNum();
        double x2 = generarNum();
        double x3 = generarNum();
        double x4 = generarNum();
        double x5 = generarNum();
        double x6 = generarNum();
        double x7 = generarNum();
        double x8 = generarNum();
        double x9 = generarNum();
        suma += (x0 + x1 + x2 + x3 + x4 + x5 + x6 + x7 + x8 + x9)*(x0 + x1 + x2 + x3 + x4 + x5 + x6 + x7 + x8 + x9);
    }

    mypi = suma;
    /* reference value of pi */

    // printf("This is my sum: %.16f from rank: %d in: %s\n", mypi,
    // rank, name);
    MPI_Reduce(&mypi, &pi, 1, MPI_DOUBLE, MPI_SUM, 0, MPI_COMM_WORLD);
    if (rank == 0){
        printf( "%d %.16f\n",n,pi/n);
        //end_time = MPI_Wtime();
        //computation_time = end_time - start_time;
        //printf("Time of calculating pi is: %f\n", computation_time);
    }
        
    MPI_Finalize();
    return 0;
}
