# functiile testeaza repository-ul aplicatiei pentru film
from domeniu.entitati import Film
from Infrastructura.filmRepository import FilmRepository


def test_getAll_FilmRepository():
    filmRepository = FilmRepository()
    film1 = Film("1", "Titlu", "Descriere", "Gen", 6)
    film2 = Film("2", "Titlu2", "Descriere2", "Gen2", 8)
    filmRepository.adaugaFilm(film1)
    filmRepository.adaugaFilm(film2)

    filme = filmRepository.getAll()
    assert len(filme) == 2
    assert filme[0].get_id() == "1"
    assert filme[1].get_id() == "2"

def test_getById_FilmRepository():
    filmRepository = FilmRepository()
    film1 = Film("1", "Titlu", "Descriere", "Gen", 6)
    filmRepository.adaugaFilm(film1)

    film = filmRepository.getById("1")

    assert film.get_titlu() == "Titlu"

def test_adaugaFilm_FilmRepository():
    filmRepository = FilmRepository()
    film1 = Film("1", "Titlu", "Descriere", "Gen", 6)
    filmRepository.adaugaFilm(film1)

    filme = filmRepository.getAll()
    assert len(filme) == 1
    assert filme[0].get_id() == "1"

    try:
        filmRepository.adaugaFilm(film1)
        assert False
    except KeyError:
        ...

def test_modifica_FilmRepository():
    filmRepository = FilmRepository()
    film1 = Film("1", "Titlu1", "Descriere1", "Gen1", 6)
    film2 = Film("1", "Titlu2", "Descriere2", "gen2", 5)
    film3 = Film("2", "Titlu3", "Descriere3", "gen3", 7)
    filmRepository.adaugaFilm(film1)
    filmRepository.modifica(film2)

    filme = filmRepository.getAll()
    assert filme[0].get_titlu() == "Titlu2"

    try:
        filmRepository.modifica(film3)
        assert False
    except KeyError:
        ...

def test_sterge_FilmRepostiory():
    filmRepository = FilmRepository()
    film1 = Film("1", "Titlu1", "Descriere1", "Gen1", 6)
    filmRepository.adaugaFilm(film1)

    filmRepository.sterge(film1.get_id())

    assert len(filmRepository.getAll()) == 0

    try:
        filmRepository.sterge("12345")
        assert False
    except KeyError:
        ...

