#pragma once

#include <vector>
using namespace std;
typedef int TCheie;
typedef int TValoare;
typedef  bool (*Conditie)(TValoare);

#include <utility>
typedef std::pair<TCheie, TValoare> TElem;

class Nod;

typedef Nod* PNod;

class Nod {
public:
	friend class MDO;
	Nod(TElem e, PNod st, PNod dr, PNod urm)
	{
		this->e = e;
		this->st = st;
		this->dr = dr;
		this->urm = urm;
	}
	TElem e;
	PNod st;
	PNod dr;
	PNod urm;
private:
};
class IteratorMDO;

typedef bool(*Relatie)(TCheie, TCheie);

class MDO {
	friend class IteratorMDO;
    private:
		void dealoca(PNod p)
		{
			if (p != NULL)
			{
				if (p->st != NULL)
					dealoca(p->st);
				if (p->dr != NULL)
					dealoca(p->dr);
				delete p;
			}
		}

		PNod rad;
		int dimensiune;
		Relatie rel;


	/* aici e reprezentarea */
    public:

	// constructorul implicit al MultiDictionarului Ordonat
	MDO(Relatie r);

	// adauga o pereche (cheie, valoare) in MDO
	void adauga(TCheie c, TValoare v);

	//cauta o cheie si returneaza vectorul de valori asociate
	vector<TValoare> cauta(TCheie c) const;

	//sterge o cheie si o valoare 
	//returneaza adevarat daca s-a gasit cheia si valoarea de sters
	bool sterge(TCheie c, TValoare v);

	//returneaza numarul de perechi (cheie, valoare) din MDO 
	int dim() const;

	//verifica daca MultiDictionarul Ordonat e vid 
	bool vid() const;

	// se returneaza iterator pe MDO
	// iteratorul va returna perechile in ordine in raport cu relatia de ordine
	IteratorMDO iterator() const;

	// destructorul 	
	~MDO();

	void filtreaza(Conditie cond);

	void filtreazaRec(PNod& p, Conditie cond);

};
