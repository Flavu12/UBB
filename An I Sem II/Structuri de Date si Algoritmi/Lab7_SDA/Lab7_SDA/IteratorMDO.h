#pragma once

#include "MDO.h"
#include <stdexcept>
#include <vector>

class IteratorMDO{
	friend class MDO;
	friend class Nod;
private:

	//constructorul primeste o referinta catre Container
	//iteratorul va referi primul element din container
	IteratorMDO(const MDO& dictionar);

	//contine o referinta catre containerul pe care il itereaza
	const MDO& dict;
	
	PNod curent;
	PNod primul;
	void inordine(PNod v)
	{
		if (v->st != NULL)
			inordine(v->st);
		if (primul == NULL)
		{
			primul = v;
			curent = primul;
		}
		else
		{
			curent->urm = v;
			curent = curent->urm;
		}
		if (v->dr != NULL)
			inordine(v->dr);
	}


public:

		//reseteaza pozitia iteratorului la inceputul containerului
		void prim();

		//muta iteratorul in container
		// arunca exceptie daca iteratorul nu e valid
		void urmator();

		//verifica daca iteratorul e valid (indica un element al containerului)
		bool valid() const;

		//returneaza valoarea elementului din container referit de iterator
		//arunca exceptie daca iteratorul nu e valid
		TElem element() const;
};

