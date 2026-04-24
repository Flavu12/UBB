#functiile testeaza service-ul aplicatiei pentru film
from Infrastructura.filmRepository import FilmRepository
from business.filmService import FilmService


def test_getALL_FilmService():
    filmRepository = FilmRepository()
    filmService = FilmService(filmRepository)
    filmService.adaugaFilm("1", "Titlu", "Descriere", "Gen", 6)
    filmService.adaugaFilm("2", "Titlu2", "Descriere2", "Gen2", 6)

    filme = filmService.getAll()
    assert len(filme) == 2
    assert filme[0].get_id() == "1"
    assert filme[1].get_id() == "2"

def test_adaugaFilm_FilmService():
    filmRepository = FilmRepository()
    filmService = FilmService(filmRepository)
    filmService.adaugaFilm("1", "Titlu", "Descriere", "Gen", 6)

    filme = filmService.getAll()
    assert len(filme) == 1
    assert filme[0].get_id() == "1"

    try:
        filmService.adaugaFilm("1", "Titlu", "Descriere", "Gen", 6)
        assert False
    except KeyError:
        ...

def test_modifica_FilmService():
    filmRepository = FilmRepository()
    filmService = FilmService(filmRepository)
    filmService.adaugaFilm("1", "Titlu", "Descriere", "Gen", 6)

    filmService.modifica("1", "Titlu1", "Descriere1", "Gen1",6)

    filme = filmService.getAll()
    assert len(filme) == 1
    assert filme[0].get_titlu() == "Titlu1"

    try:
        filmService.modifica("2", "Titlu1", "Descriere1", "Gen1", 6)
        assert False
    except KeyError:
        ...

def test_sterge_FilmService():
    filmRepository = FilmRepository()
    filmService = FilmService(filmRepository)
    filmService.adaugaFilm("1", "Titlu", "Descriere", "Gen", 6)

    filmService.sterge("1")

    filme = filmService.getAll()
    assert len(filme) == 0

def test_findById_FilmService():
    filmRepository = FilmRepository()
    filmService = FilmService(filmRepository)
    filmService.adaugaFilm("1", "Titlu", "Descriere", "Gen", 6)

    film = filmService.findById("1")
    assert film.get_id() == "1"
    assert film.get_titlu() == "Titlu"

    film2 = filmService.findById("1234")
    assert film2 == None

def test_inchiriere_dupa_id_FilmService():
    filmRepository = FilmRepository()
    filmService = FilmService(filmRepository)
    filmService.adaugaFilm("1", "Titlu", "Descriere", "Gen", 6)

    filmService.inchiriere_film_dupa_id("1")
    filme = filmService.getAll()
    assert filme[0].get_nrf() == 7

    try:
        filmService.inchiriere_film_dupa_id("507")
        assert False
    except KeyError:
        ...

def test_inchiriere_film_sortare_FilmService():
    filmRepository = FilmRepository()
    filmService = FilmService(filmRepository)
    filmService.adaugaFilm("1", "Titlu1", "Descriere1", "Gen1", 1)
    filmService.adaugaFilm("2", "Titlu2", "Descriere2", "Gen2", 10)
    filmService.adaugaFilm("3", "Titlu3", "Descriere3", "Gen3", 7)

    filmService.inchiriere_film_sortare()
    filme = filmService.getAll()

    assert len(filme) == 3
    assert filme[0].get_id() == "2"
    assert filme[1].get_id() == "3"
    assert filme[2].get_id() == "1"

    assert filme[0].get_nrf() == 10
    assert filme[1].get_nrf() == 7
    assert filme[2].get_nrf() == 1