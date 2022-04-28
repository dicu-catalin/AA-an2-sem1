Transformarea creeaza un numar de k variabile pentru fiecare nod din graf
(n*k in total). Astfel, fiecare variabila pentru un nod din graf corespunde unei
valori intre 1 si k. Pentru a verifica daca exista o acoperire de k noduri 
pentru un graf, trebuie sa fie exact k variabile adevarate, care sa nu apartina
aceluiasi nod si restul la impartirea cu k sa fie diferit pentru toate variabilele.
Ultima conditie este ca pentru fiecare muchie din graf, cel putin una dintre 
variabilele corespunzatoare nodurilor din muchie sa fie adevarata. 

Timpul de executie al programului este O(n^3)
