import sys
import numpy as np

def verify(fnc_matrix, sol):
	i = 0
	j = 0
	# verifica pe rand elementele de pe linii(clauzele) pana cand gaseste un 
	# element care sa faca clauza adevarata. Daca se dovedeste ca o clauza
	# nu este adevarata cu configuratia acutala, intoarce 0 si trece la 
	# urmatoarea configuratie
	while i < len(fnc_matrix):
		if fnc_matrix[i][j] * sol[j] == 1:
			i += 1
			j = -1
		j += 1
		if j == len(sol):
			return 0
	return 1


def btk(fnc_matrix, sol, poz):
	# atunci cand toate variabilele au o valoare, testeaza solutia si in cazul
	# in care aceasta este buna, afiseaza 1 si rularea se opreste
	if poz == len(sol):
		if verify(fnc_matrix, sol) == 1:
			print("1")
			sys.exit()
	else:
		for i in range(0, 2):  # da valori tuturor variabilelor(fals/adevarat)
			if i == 0:
				sol[poz] = -1
			else:
				sol[poz] = 1
			#se apeleaza iar functia pentru a da valoare urmatoarei variabile
			btk(fnc_matrix, sol, poz+1)

def read():
	file = open(sys.argv[1])
	fnc = file.readline()  # citeste expresia in forma conjunctiva normala
	file.close()
	clauses = fnc.split("^")  # separa clauzele
	variables = set()
	# parcurge fiecare clauza pentru a aflat variabilele din expresie
	for clause in clauses:
		clause = clause.strip("()")
		variables_curr = clause.split("V")
		for variable in variables_curr:
			variables.add(variable.strip("~"))
	# creeaza matricea in care se va retine expresia
	fnc_matrix = np.zeros((len(clauses), len(variables)))

	# parcurge fiecare clauza si completeaza matricea in functie de variabilele
	# de pe fiecare clauza
	nr_clauses = len(clauses)
	for i in range(0, nr_clauses):
		clause = clauses[i].strip("()")
		variables_curr = clause.split("V")
		for variable in variables_curr:
			if variable[0] == "~":
				fnc_matrix[i][int(variable.strip("~"))-1] = -1
			else:
				fnc_matrix[i][int(variable)-1] = 1
	
	return fnc_matrix


def main():
	fnc_matrix = read()
	sol = np.zeros((len(fnc_matrix[0])))
	btk(fnc_matrix, sol, 0)
	print("0")

if __name__ == "__main__":
    main()