import sys
import numpy as np
from time import time

# clasa reprezinta nodurile din care este format arborele
class node:
	def __init__(self, value):
		self.left = None
		self.fnc = value
		self.right = None

# creeaza o noua matrice pentru fiecare fiu(stanga si dreapta) al nodului curent	
def bdd(root, niv):
	# daca matricea nu mai are nicio linie, inseamna ca expresia este valida
	if len(root.fnc) == 0:
		print("1")
		sys.exit()
	# verifica daca s-a ajuns la ultimul nod din arbore
	if niv == len(root.fnc[0]):
		return

	left = []
	right = []
	# construieste matricile pentru fiii nodului curent
	for line in root.fnc:
		if line[niv] == 1:
			left.append(line)
		elif line[niv] == -1:
			right.append(line)
		else:
			left.append(line)
			right.append(line)

	root.left = node(left)
	root.right = node(right)
	# apeleaza functia pentru ambele noduri nou create
	bdd(root.left, niv+1)
	bdd(root.right, niv+1)


def read():
	fnc = "(~1V~6)^(~1V~7)^(~2V~6)^(~2V~7)^(~3V~6)^(~3V~7)^(~4V~6)^(~4V~7)^(~5V~6)^(~5V~7)^(5V4V2V6)^(5V4V2V7)^(4V3V1V6)^(4V3V1V7)^(3V4V6)^(3V4V7)^(1V4V6)^(1V4V7)^(2V5V7)^(2V5V6)"
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
	root = node(fnc_matrix)
	bdd(root, 0)
	print("0")

if __name__ == "__main__":
    main()