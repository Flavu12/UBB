#include "CP.h"
#include "TestScurt.h"
#include <assert.h>

bool rel(TPrioritate p1, TPrioritate p2) {
	if (p1 <= p2) {
		return true;
	}
	else {
		return false;
	}
}




void testAll() { //apelam fiecare functie sa vedem daca exista
	CP c(rel);
	
	assert(c.vida() == true);
	
	//adaugam 5, 3, 10, 2, 12 -> rezultat: 2, 3, 5, 10, 12
	c.adauga(5, 5);
	assert(c.element().first == 5);
	assert(c.element().second == 5);
	c.adauga(3, 3);
	assert(c.element().first == 3);
	assert(c.element().second == 3);
	c.adauga(10, 10);
	assert(c.element().first == 3);
	assert(c.element().second == 3);
	c.adauga(2, 2);
	assert(c.element().first == 2);
	assert(c.element().second == 2);
	c.adauga(12, 12);
	assert(c.element().first == 2);
	assert(c.element().second == 2);
	assert(c.vida() == false);
	assert(c.sterge().second == 2);
	assert(c.element().second == 3);
	assert(c.sterge().second == 3);
	assert(c.element().second == 5);
	assert(c.sterge().second == 5);
	assert(c.element().second == 10);
	assert(c.sterge().second == 10);
	assert(c.element().second == 12);
	assert(c.sterge().second == 12);
	assert(c.vida() == true);
}

void test_nou()
{
		CP c(rel);
		c.adauga(1, 1);
		c.adauga(2, 2);
		c.adauga(3, 3);

		
		assert(c.modificaPrioritate(2, 5) == 2); // Prioritatea veche a elementului cu cheia 2 era 2
		assert(c.element().second == 1); // Prioritatea elementului curent trebuie să fie 5

		
		assert(c.modificaPrioritate(4, 10) == -1); // Elementul cu cheia 4 nu există, deci se întoarce -1

		
		assert(c.modificaPrioritate(3, 0) == 3); // Prioritatea veche a elementului cu cheia 1 era 1
		assert(c.element().second == 0); // Prioritatea elementului curent trebuie să fie 0


	}
	