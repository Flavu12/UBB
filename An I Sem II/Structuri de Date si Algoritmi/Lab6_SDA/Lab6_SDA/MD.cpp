#include "MD.h"
#include "IteratorMD.h"
#include <exception>
#include <iostream>

using namespace std;


int hashCode(TElem e) {
	//ptr moment numarul e intreg
	return abs(e.first);
}

int MD::d(TElem e) const {
	//dispersia prin diviziune
	return hashCode(e) % m;
}

MD::MD() { // theta (n)
	m = 200000;
	e = new TElem[200000];
	urm = new int[200000];
	for (int i = 0; i < m; i++)
	{
		e[i].second = zero;
		urm[i] = -1;
		e[i].first = zero;
	}
	dime = 0;

	primLiber = 0;
}


void MD::adauga(TCheie c, TValoare v) { // best case = theta (1) worst case = theta ( n)
	TElem elem = make_pair(c, v);
	int i = d(elem);
	if (e[i].second == zero)
	{
		e[i].first = c;
		e[i].second = v;
		if (i == primLiber)
			actPrimLiber();
		dime++;
		return;
	}

	int j = -1;

	while (i != -1)
	{
		j = i;
		i = urm[i];
	}

	e[primLiber] = elem;
	urm[j] = primLiber;
	actPrimLiber();
	dime++;
}


bool MD::sterge(TCheie c, TValoare v) { // best case = theta (1) worst case = theta ( n)
	TElem elem = make_pair(c, v);
	int i = d(elem);
	while (i != -1 && e[i] != elem)
		i = urm[i];
	if (i != -1)
	{
		e[i].first = zero;
		e[i].second = zero;
		dime--;
		return true;
	}

	return false;
}


vector <TValoare> MD::cauta(TCheie c) const { // best case = theta (1) worst case = theta ( n)
	vector <TValoare> v;
	TElem elem = make_pair(c, 0);
	int i = d(elem);
	while (i != -1)
	{
		if (e[i].first == c)
		{
			v.push_back(e[i].second);
		}
		i = urm[i];
	}
	return v;
}


int MD::dim() const {
	return dime;
}


bool MD::vid() const {
	return (dime == 0);
}

IteratorMD MD::iterator() const {
	return IteratorMD(*this);
}


MD::~MD() {
}
