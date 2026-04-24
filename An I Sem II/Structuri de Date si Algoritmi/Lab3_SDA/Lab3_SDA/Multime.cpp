#include "Multime.h"
#include "IteratorMultime.h"
#include <iostream>

using namespace std;

Nod::Nod(TElem v, Nod* u, Nod* a)
{//theta(1)
	val = v;
	urm = u;
	ant = a;
}

TElem Nod::get_val()
{//theta(1)
	return val;
}

Nod* Nod::get_urm()
{//theta(1)
	return urm;
}

Nod* Nod::get_ant()
{//theta(1)
	return ant;
}

//o posibila relatie
bool rel(TElem e1, TElem e2) {
	if (e1 <= e2) {
		return true;
	}
	else {
		return false;
	}
}

Multime::Multime() {
	prim = nullptr;
	ultim = nullptr;
	size = 0;
}


bool Multime::adauga(TElem elem) {
	//theta(1)
	if (cauta(elem)) //daca gasim elementul in lista nu il mai adaugam
		return false;

	Nod* nou = new Nod(elem, nullptr, nullptr);
	if (prim == nullptr) { //daca lista este goala
		prim = nou;
		ultim = nou; // actualizam si ultimul nod
	}
	else if (rel(elem, prim->val)) { //daca trebuie sa adaugam elementul pe prima pozitie
		nou->urm = prim;
		prim->ant = nou;
		prim = nou;
	}
	else {
		Nod* curent = prim;
		while (curent->urm != nullptr && rel(curent->urm->val, elem)) {
			curent = curent->urm;
		}
		if (curent->urm != nullptr) { // adaugam intre nodul curent si urmatorul nod
			nou->urm = curent->urm;
			nou->ant = curent;
			curent->urm->ant = nou;
			curent->urm = nou;
		}
		else { // inseram pe ultima pozitie
			nou->ant = curent;
			curent->urm = nou;
			ultim = nou; // actualizam si ultimul nod
		}
	}
	size++;
	return true;
}

bool Multime::sterge(TElem elem) {
	/*
* Complexitate: theta(1)
* BC: theta(1) //e primul elem
* WC: theta(n) // se sterge ultimul elem
*/
	if (!cauta(elem))  //in cazul in care nu exista elem 
		return false;
	Nod* curent = prim;
	while (rel(curent->val, elem) && curent != NULL)
	{

		if (curent->val == elem)  //daca am gasit val ce trebuie stearsa
		{
			if (curent == prim) //verif daca e primul nod
			{
				prim = curent->urm;
				if (prim != nullptr)
				{
					prim->ant = nullptr;
				}
			}
			else if (curent == ultim) //daca e ultimul
			{
				ultim = curent->ant;
				if (ultim != nullptr)
				{
					ultim->urm = nullptr;
				}
			}
			else
			{
				curent->ant->urm = curent->urm;
				curent->urm->ant = curent->ant;
			}
			delete curent; //sterg nodul
			size--;
			return true;
		}
		curent = curent->urm;
	}

}

bool Multime::cauta(TElem elem) const {
	/*Complexitate:
	*BC : theta(1) - gasim elem pe prima poz
	* WC : theta(n) - gasim elem pe ultima poz / nu il gasim deloc
	* AC : 1 / n + 2 / n + ...n / n + (n + 1) / n = (n + 1)(n + 2) / 2n apartine theta(n)
	*/
	Nod* curent = prim;
	while (curent != nullptr && rel(curent->val, elem))
	{
		if (curent->val == elem)
			return true;
		curent = curent->urm;
	}
	return false;
}


int Multime::dim() const {
	//theta(1)
	return size;
}



bool Multime::vida() const {
	//theta(1)
	if (size == 0)
		return true;
	return false;
}

IteratorMultime Multime::iterator() const {
	return IteratorMultime(*this);
}


Multime::~Multime() {
	while (prim != NULL)
	{
		Nod* aux = prim;
		prim = prim->urm;
		delete aux;
		size--;
	}
}






