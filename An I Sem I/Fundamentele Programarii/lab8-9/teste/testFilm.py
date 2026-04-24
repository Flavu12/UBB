# functiile testeaza domeniul aplicatiei pentru film
from domeniu.entitati import Film


def testFilm_get():
    film = Film("1", "Titlu", "Descriere", "Gen", 6)

    assert film.get_id() == "1"
    assert film.get_titlu() == "Titlu"
    assert film.get_descriere() == "Descriere"
    assert film.get_gen() == "Gen"
    assert film.get_nrf() == 6


def testFilm_set():
    film = Film("1", "Titlu", "Descriere", "Gen", 6)

    film.set_id("18")
    assert film.get_id() == "18"

    film.set_titlu("Titlu1")
    assert film.get_titlu() == "Titlu1"

    film.set_descriere("Descriere1")
    assert film.get_descriere() == "Descriere1"

    film.set_gen("Gen1")
    assert film.get_gen() == "Gen1"

    film.set_nrf(16)
    assert film.get_nrf() == 16
