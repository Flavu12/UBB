#include "IteratorMultime.h"
#include "Multime.h"


IteratorMultime::IteratorMultime(const Multime& m) : mult(m) {
	actual = mult.prim;
}

TElem IteratorMultime::element() const {
	if (valid())

		return actual->get_val();
	else
		throw("Iterator invalid!");
}

bool IteratorMultime::valid() const {
	 if (actual != nullptr)
		return true;
	return false;
}

void IteratorMultime::urmator() {
	if (valid())
		actual = actual->get_urm();
	else
		throw("Iterator invalid!");
}

void IteratorMultime::prim() {
	actual = mult.prim;
}

