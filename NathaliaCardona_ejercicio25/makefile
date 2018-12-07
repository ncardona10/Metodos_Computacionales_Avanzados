sample.pdf: sample.dat
	python3 grafica.py

sample.dat: sample 
	./sample 1000 0 1 > sample.dat 
sample:
	g++ sample.c -o sample -std=gnu++11
clean:
	rm sample
	rm *.dat
	rm *.pdf
