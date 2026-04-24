#include "IteratorMD.h"
#include "MD.h"

using namespace std;

IteratorMD::IteratorMD(const MD& _md) : md(_md) {
	curent = 0;

	deplasare();
}

TElem IteratorMD::element() const {
	if (valid() == 0)
		throw std::invalid_argument("iteratorul nu este valid");
	return md.e[curent];
	
}

bool IteratorMD::valid() const {
	return (curent < md.m);
}

void IteratorMD::urmator() {
	if (valid() == 0)
		throw std::invalid_argument("iteratorul nu este valid");
	curent++;
	deplasare();
}

void IteratorMD::prim() {
	curent = 0;
	deplasare();
}


void IteratorMD::revinoKPasi(int k) {
	/*
	Funcție revinoKPasi(MD,It, k)
	preconditii:
		md este multidictionar
		it iterator
		k numar natural nenul
	postconditii:
		md este multidictionar
		it' iterator cu k pasi in urma
		daca k este <= 0 arunca exceptie


    Dacă iteratorul nu este valid sau k este mai mic sau egal cu zero
        Aruncă excepție cu mesajul "iteratorul nu este valid sau k este zero sau negativ"
    Sfârșit dacă

    pasi <- 0
    Cat timp pasi < k și iteratorul este valid
        curent <- curent - 1
        deplasare()
        pasi <- pasi + 1
    Sfârșit cat timp
Sfârșit funcție

	*/
	if (valid() == 0 || k <= 0)
		throw std::invalid_argument("iteratorul nu este valid sau k este zero sau negativ");

	int pasi = 0;
	while (pasi < k && valid()) {
		curent--;
		deplasare();
		pasi++;
	}
}

