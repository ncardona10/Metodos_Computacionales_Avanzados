#include <stdio.h>
#include "mpi.h"
using namespace std;
int main(int argc, char *argv[])
{
    int rank, number;
    number = 0;
    /* starts MPI */
    MPI_Init(&argc, &argv);
    /* get current process rank */
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    if (rank == 0)
    {
        number = 123;
        MPI_Send(&number, 1, MPI_INT, 1, 0, MPI_COMM_WORLD);
    }
    else if (rank == 1)
    // if (rank == 1)
    {
        printf("Number = %d\n", number);
        MPI_Recv(&number, 1, MPI_INT, 0, 0, MPI_COMM_WORLD,
                 MPI_STATUS_IGNORE);
        cout << "Process 1 received data from process 0, number = " << number << endl);
    }
    MPI_Finalize(); /* ends MPI */
    return 0;
}