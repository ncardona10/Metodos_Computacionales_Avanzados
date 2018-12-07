GelmanRubin.png: markovChain.c graficas.py
	g++ -fopenmp markovChain.c -o markovChain.x -std=c++11
	./markovChain.x
	python3 graficas.py

clean:
	rm *.dat
	rm *.png 
	rm *.x