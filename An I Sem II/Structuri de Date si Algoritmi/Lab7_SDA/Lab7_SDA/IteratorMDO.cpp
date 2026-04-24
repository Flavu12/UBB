#include "IteratorMDO.h"
#include "MDO.h"

IteratorMDO::IteratorMDO(const MDO& d) : dict(d){
	
	PNod p = dict.rad;
	if (p!=NULL)
		inordine(p);
	
}

void IteratorMDO::prim(){
	curent = primul;
}

void IteratorMDO::urmator(){
	if (valid()==0)
		throw std::invalid_argument("iteratorul nu este valid");
	curent = curent->urm;

}

bool IteratorMDO::valid() const{
	if (curent==NULL)
		return false;
	return true;
}

TElem IteratorMDO::element() const{
	if (valid() == 0)
		throw std::invalid_argument("iteratorul nu este valid");
	return curent->e;
}


