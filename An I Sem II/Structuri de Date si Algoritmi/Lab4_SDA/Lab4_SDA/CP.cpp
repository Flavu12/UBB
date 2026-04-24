
#include "CP.h"
#include <exception>
#include <stdio.h>

using namespace std;


CP::CP(Relatie r) {
	this->capacitate = 1;
	this->prim = -1;
	this->ultim = -1;
	this->r = r;
	this->elemente = new Element[capacitate];
	this->urm = new int[capacitate];
	init_spatiu_liber();

}
void CP::redim()
{
	//crearea unui nou spatiu in memorie
	int new_cp = 2 * capacitate;
	Element* new_elem = new Element[new_cp];
	int* new_urm = new int[new_cp];
	//copierea vechilor elemente
	for (int i = 0; i < capacitate; i++)
	{
		new_urm[i] = urm[i];
		new_elem[i] = elemente[i];
	}
	for (int i = capacitate; i < new_cp; i++)
		new_urm[i] = i + 1;

	//distrugerea spatiului vechi de memorie
	delete[] elemente;
	delete[] urm;


	primLiber = capacitate;
	urm = new_urm;
	elemente = new_elem;
	capacitate = new_cp;
	urm[capacitate - 1] = -1;

}

void CP::init_spatiu_liber()
{
	//marchez toate pozitiile din  vector ca find libere
	for (int i = 0; i < capacitate - 1; i++)
		urm[i] = i + 1;
	//marcam	
	urm[capacitate - 1] = -1;
	primLiber = 0;
}

// caz favorabil theta(1)
//caz defavorabil theta(cp)
//caz mediu theta(cp)
//complexitate generala O(n)
int CP::aloca()
{
	//daca nu mai avem nici un spatiu liber facem redimensionare	
	if (primLiber == -1)
		redim();

	int pozitie_libera = primLiber;

	primLiber = urm[primLiber];

	return pozitie_libera;


}

//complexitate theta(1)
void CP::dealoca(int i)
{
	//adaugam la inceptul listei noua pozitie libera
	urm[i] = primLiber;
	primLiber = i;
}

void CP::adauga(TElem e, TPrioritate p) {
	int poz = aloca();
	elemente[poz] = make_pair(e, p);

	// Cazul în care coada este vidă sau elementul trebuie adăugat la început
	if (prim == -1 || r(p, elemente[prim].second)) {
		urm[poz] = prim;
		prim = poz;
	}
	else {
		int t = prim;
		int prev = -1;
		// Căutăm poziția în coadă a noului element
		while (t != -1 && r(elemente[t].second, p)) {
			prev = t;
			t = urm[t];
		}
		// Elementul trebuie inserat între două elemente existente sau la sfârșitul cozii
		urm[poz] = t;
		if (t == prim) {
			prim = poz;
		}
		else {
			urm[prev] = poz;
		}
	}
}

bool CP::vida() const {
	return prim == -1;
}


//arunca exceptie daca coada e vida
Element CP::element() const {
	if (vida())
	throw exception("Coada cu prioritati este vida!");
	return elemente[prim];
	
}

Element CP::sterge() {
	if (vida()) throw exception("coada este vida");
	Element e = elemente[prim];
	int urmatorul = urm[prim];
	dealoca(prim);//dealoca spatiul care era ocupat de primul element
	prim = urmatorul;
	return e;
}

TPrioritate CP::modificaPrioritate(TElem elem, TPrioritate nouaPrioritate) {//O(n)
	/*modificaPrioritate(cp, elem, nouaPrioritate)
	* preconditii: cp este de tip Coada cu Prioritati, elem este de tip TElem, nouaPrioritate este de tip TPrioritate
	* postconditii: cp' coada in care s-a modificat prioritatea unui element 
	* pozitie<-prim
	* prev<- -1
	* prioritateVeche<- -1
	* cat timp pozitie != -1 executa
		daca elemente[pozitie].valoare = elem atunci
			prioriateVeche = elemente[poz].prioritate
			elemente[pozitie].prioritate = nouaPrioritate
			daca prev != -1 si relatie(elemente[pozitie].prioritate, elemente[prev].valoare) atunci
				urmator[prev]<-urmator[pozitie];
				urmator[pozitie]<-prim
				prim<-pozitie
			SFDaca
		SFDaca
	poz = urmator[poz];
	SFCatTimp
	returneaza prioritateVeche
	*/
	int pozitie = prim;
	int prev = -1;
	int PrioritateVeche = -1;
	// Căutăm poziția elementului în coadă
	while (pozitie != -1) {
		if (elemente[pozitie].first == elem) {
			PrioritateVeche = elemente[pozitie].second;
			// Actualizăm prioritatea elementului
			elemente[pozitie].second = nouaPrioritate;
			if (prev != -1 && r(elemente[pozitie].second, elemente[prev].second)) {//verificam daca elementele trebuie sa fie reordonate
				urm[prev] = urm[pozitie];
				urm[pozitie] = prim;
				prim = pozitie;
				}
			break;
			}
		prev = pozitie;
		pozitie = urm[pozitie];
		}
	return PrioritateVeche;
	}



CP::~CP() {
	delete[] urm;
	delete[] elemente;
};




