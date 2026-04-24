from Business.service_filme import ServiceFilme
from Domeniu.Film import Film
from Infrastructura.repo_filme import RepoFilme
from Validare.validator_film import ValidatorFilm
from erori.repo_error import RepoError


def teste_domeniu():
    film = Film("1", "Scream", "a aparut in anul 1996", "horror")

    assert film.get_id_film() == "1"
    assert film.get_titlu_film() == "Scream"
    assert film.get_descriere_film() == "a aparut in anul 1996"
    assert film.get_gen_film() == "horror"

    film.set_titlu_film("Ice Age")
    assert film.get_titlu_film() == "Ice Age"

    film.set_descriere_film("a aparut in anul 2000")
    assert film.get_descriere_film() == "a aparut in anul 2000"

    film.set_gen_film("animatie")
    assert film.get_gen_film() == "animatie"

# Teste Repository


def test_adauga_film_repo():
    filme_repo = RepoFilme()
    film1 = Film("1", "Scream", "a aparut in anul 1996", "horror")

    filme_repo.adauga_film(film1)

    filme = filme_repo.get_all()
    assert len(filme) == 1
    assert filme[0].get_id_film() == "1"
    film2 = Film("1", "Ice Age", "a aparut in anul 2000", "animatie")
    try:
        filme_repo.adauga_film(film2)
        assert False
    except RepoError:
        ...


def test_get_all_repo():

    filme_repo = RepoFilme()
    film1 = Film("1", "Scream", "a aparut in anul 1996", "horror")
    film2 = Film("2", "Ice Age", "a aparut in anul 2000", "animatie")
    filme_repo.adauga_film(film1)
    filme_repo.adauga_film(film2)

    filme = filme_repo.get_all()
    assert len(filme) == 2
    assert filme[0].get_id_film() == "1"
    assert filme[1].get_id_film() == "2"


def test_cauta_dupa_id_repo():
    filme_repo = RepoFilme()
    film1 = Film("1", "Scream", "a aparut in anul 1996", "horror")
    filme_repo.adauga_film(film1)

    film = filme_repo.cauta_film_dupa_id("1")

    assert film.get_titlu_film() == "Scream"


def test_modifica_repo():
    filme_repo = RepoFilme()
    film1 = Film("1", "Scream", "a aparut in anul 1996", "horror")
    film2 = Film("1", "Ice Age", "a aparut in anul 2000", "animatie")
    film3 = Film("2", "Scary Movie", "a aparut in anul 2010", "comedie")

    filme_repo.adauga_film(film1)
    filme_repo.modifica_film(film2)


    try:
        filme_repo.modifica_film(film3)
        assert False
    except RepoError:
        ...


def test_sterge_repo():
    filme_repo = RepoFilme()
    film1 = Film("1", "Scream", "a aparut in anul 1996", "horror")
    filme_repo.adauga_film(film1)

    filme_repo.sterge_film_dupa_id(film1.get_id_film())

    assert len(filme_repo.get_all()) == 0

    try:
        filme_repo.sterge_film_dupa_id("23423")
        assert False
    except RepoError:
        ...

# Teste Service


def test_adauga_film_service():
    filme_repo = RepoFilme()
    filme_validare = ValidatorFilm()
    filme_service = ServiceFilme(filme_validare, filme_repo)
    filme_service.adauga_film_service("1", "Scream", "a aparut in anul 1996", "horror")

    filme = filme_service.get_all_filme_service()
    assert len(filme) == 1
    assert filme[0].get_id_film() == "1"

    try:
        filme_service.adauga_film_service("1", "Ice Age", "a aparut in anul 2000", "animatie")
        assert False
    except RepoError:
        ...


def test_cauta_film_dupa_id_service():
    filme_repo = RepoFilme()
    film_validator = ValidatorFilm()
    filme_service = ServiceFilme(film_validator, filme_repo)
    filme_service.adauga_film_service("1", "Scream", "a aparut in anul 1996", "horror")

    film = filme_service.cauta_film_service("1")
    assert film.get_id_film() == "1"
    assert film.get_titlu_film() == "Scream"

    film2 = filme_service.cauta_film_service("44")
    assert film2 == None


def test_sterge_film_service():
    filme_repo = RepoFilme()
    validator_film = ValidatorFilm
    filme_service = ServiceFilme(validator_film, filme_repo)
    filme_service.adauga_film_service("1", "Scream", "a aparut in anul 1996", "horror")

    filme_service.sterge_film_service("1")

    filme = filme_service.get_all_filme_service()
    assert len(filme) == 0

    try:
        filme_service.sterge_film_service("12")
        assert False
    except RepoError:
        ...


def test_get_all_service():
    filme_repo = RepoFilme()
    validator_film = ValidatorFilm
    filme_service = ServiceFilme(validator_film, filme_repo)
    filme_service.adauga_film_service("1", "Scream", "a aparut in anul 1996", "horror")
    filme_service.adauga_film_service("2", "Scary Movie", "a aparut in anul 2010", "comedie")

    filme = filme_service.get_all_filme_service()
    assert len(filme) == 2
    assert filme[0].get_id_film() == "1"
    assert filme[1].get_id_film() == "2"


def ruleaza_toate_testele_filme():
    teste_domeniu()
    test_adauga_film_repo()
    test_get_all_repo()
    test_cauta_dupa_id_repo()
    test_modifica_repo()
    test_sterge_repo()
    test_adauga_film_service()
    test_cauta_film_dupa_id_service()
    test_sterge_film_service()
    test_get_all_service()
