#include "IteratorMDO.h"
#include "MDO.h"
#include <iostream>
#include <vector>

#include <exception>
using namespace std;

MDO::MDO(Relatie r) {
	this->rad = NULL;
	dimensiune = 0;
	rel = r;
}

// Complexitate BC= theta (1) WC=theta(n) OC=O(n)
void MDO::adauga(TCheie c, TValoare v) {
	TElem e;
	e.first = c;
	e.second = v;
	int gasit = 0;
	if (rad == NULL)
	{
		rad = new Nod(e, NULL, NULL, NULL);
		dimensiune++;
		gasit = 1;
	}
	Nod* p = rad;
	while (gasit == 0)
	{
		if (e.first == p->e.first)// Dacă cheia există deja în arbore
		{
			gasit = 1;
			while (p->urm != NULL)// Parcurge lista de valori asociate cheii și se oprește la ultimul nod
				p = p->urm;
			PNod n = new Nod(e, NULL, NULL, NULL);
			p->urm = n;
			dimensiune++;
		}
		else
		{
			if (e.first < p->e.first)// Dacă cheia este mai mică decât cheia nodului curent
			{
				if (p->st == NULL)  // Dacă nu există subarbore stâng, creează un nou nod și actualizează subarborele stâng al nodului curent
				{
					gasit = 1;
					PNod n = new Nod(e, NULL, NULL, NULL);
					p->st = n;
					dimensiune++;
				}
				else
					p = p->st;
			}
			else// Dacă cheia este mai mare decât cheia nodului curent
			{
				if (p->dr == NULL)
				{
					gasit = 1;
					PNod n = new Nod(e, NULL, NULL, NULL);
					p->dr = n;
					dimensiune++;
				}
				else
					p = p->dr;
			}
		}
	}

}

// Complexitate BC= theta (1) WC=theta(n) OC=O(n)
vector<TValoare> MDO::cauta(TCheie c) const {
	vector <TValoare> v;
	int gasit = 0;
	PNod p = rad;
	if (p == NULL)
		return v;
	while (gasit == 0)
	{
		if (c == p->e.first)
		{
			gasit = 1;
		}
		else
		{
			if (c < p->e.first)
			{
				p = p->st;
				if (p == NULL)
					gasit = 1;
			}
			else
			{
				p = p->dr;
				if (p == NULL)
					gasit = 1;
			}
		}
	}
	while (p != NULL)
	{
		v.push_back(p->e.second);
		p = p->urm;
	}

	return v;
}

// Complexitate BC= theta (1) WC=theta(n) OC=O(n)
bool MDO::sterge(TCheie c, TValoare v) {
	int gasit = 0;
	Nod* p = rad;
	while (gasit == 0)
	{
		if (c == p->e.first)
		{
			gasit = 1;
		}
		else
		{
			if (c < p->e.first)
			{
				p = p->st;
				if (p == NULL)
					gasit = 1;
			}
			else
			{
				p = p->dr;
				if (p == NULL)
					gasit = 1;
			}
		}
	}
	if (p != NULL)
	{
		while (p != NULL and p->e.second != v)
		{
			p = p->urm;
		}
		if (p != NULL)
		{
			
			p->e.second = -100000;
			dimensiune--;
			return true;
		}
	}
	return false;
}

int MDO::dim() const {
	return dimensiune;
}

bool MDO::vid() const {
	if (dimensiune==0)
		return true;
	return false;
}

IteratorMDO MDO::iterator() const {
	return IteratorMDO(*this);
}

MDO::~MDO() {
	dealoca(rad);
}

void MDO::filtreaza(Conditie cond) {
	filtreazaRec(rad, cond);
}

void MDO::filtreazaRec(PNod& p, Conditie cond) {
	/*
	functie MDO::filtreazaRec(PNod: p, conditie: Conditie)
	preconditii: MDO este un multidictionar ordonat
				 Conditie este o functie
	postconditii: MDO' cu elementele care nu respecta conditia sterse
    pentru fiecare nod n in inordine(rad)
        daca conditie(n.e.valoare) este fals
            sterge(n.e.cheie, n.e.valoare)
        sfarsit daca
    sfarsit pentru
sfarsit functie*/
	if (p == nullptr)
		return;

	filtreazaRec(p->st, cond);

	if (!cond(p->e.second)) {
		PNod temp = p;
		p = p->urm;
		delete temp;
		dimensiune--;
	}
	else {
		filtreazaRec(p->urm, cond);
	}
}

