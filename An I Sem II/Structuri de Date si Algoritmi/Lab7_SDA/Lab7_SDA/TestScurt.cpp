#include <assert.h>

#include "MDO.h"
#include "IteratorMDO.h"

#include <exception>
#include <vector>

using namespace std;

bool relatie1(TCheie cheie1, TCheie cheie2) {
	if (cheie1 <= cheie2) {
		return true;
	}
	else {
		return false;
	}
}

void testAll(){
	MDO dictOrd = MDO(relatie1);
	assert(dictOrd.dim() == 0);
	assert(dictOrd.vid());
    dictOrd.adauga(1,2);
    dictOrd.adauga(1,3);
    assert(dictOrd.dim() == 2);
    assert(!dictOrd.vid());
    vector<TValoare> v= dictOrd.cauta(1);
    assert(v.size()==2);
    v= dictOrd.cauta(3);
    assert(v.size()==0);
    IteratorMDO it = dictOrd.iterator();
    it.prim();
    while (it.valid()){
    	TElem e = it.element();
    	it.urmator();
    }
    assert(dictOrd.sterge(1, 2) == true);
    assert(dictOrd.sterge(1, 3) == true);
    assert(dictOrd.sterge(2, 1) == false);
    assert(dictOrd.vid());
}

bool valoarePar(TValoare v) {
    return v % 2 == 0;
}


void testFiltreaza() {
    MDO d = MDO(relatie1);
    d.adauga(1, 1);
    d.adauga(2, 2);
    d.adauga(3, 3);
    d.adauga(4, 4);
    d.adauga(5, 5);

    // Filtrează valori pare
    d.filtreaza(valoarePar);
    assert(d.dim() == 2);
    assert(d.cauta(1).empty());
    assert(d.cauta(2).size() == 1);
    assert(d.cauta(2)[0] == 2);
    assert(d.cauta(3).empty());
    assert(d.cauta(4).size() == 1);
    assert(d.cauta(4)[0] == 4);
    assert(d.cauta(5).empty());
}
