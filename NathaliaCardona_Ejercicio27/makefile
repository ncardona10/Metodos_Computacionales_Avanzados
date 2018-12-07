mpiList2 mpiList1: list2.c list1.c
	mpic++ list2.c -o mpiList2
	mpirun -np 4 ./mpiList2 
	mpic++ list1.c -o mpiList1 
	mpirun -np 2 ./mpiList1
clean:
	rm mpiList*
