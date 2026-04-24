# functiile testeaza service-ul aplicatiei pentru client
from domeniu.entitati import Film
from Infrastructura.clientRepository import ClientRepository
from Infrastructura.filmRepository import FilmRepository
from business.clientService import ClientService


def test_getAll_ClientService():
    clientRepository = ClientRepository()
    filmRepository = FilmRepository()
    clientService = ClientService(clientRepository, filmRepository)
    clientService.adaugaClient("1", "Nume", "5030326260056", [1, 2])

    clienti = clientService.getAll()
    assert len(clienti) == 1
    assert clienti[0].get_id() == "1"


def test_adaugaClient_ClientService():
    clientRepository = ClientRepository()
    filmRepository = FilmRepository()
    clientService = ClientService(clientRepository, filmRepository)
    clientService.adaugaClient("1", "Nume", "5030326260056", [1, 2])

    clienti = clientService.getAll()
    assert len(clienti) == 1
    assert clienti[0].get_id() == "1"

    try:
        clientService.adaugaClient("1", "Nume", "5030326260056", [1, 2])
        assert False
    except KeyError:
        ...


def test_modifica_ClientService():
    clientRepository = ClientRepository()
    filmRepository = FilmRepository()
    clientService = ClientService(clientRepository, filmRepository)
    clientService.adaugaClient("1", "Nume", "5030326260056", [1, 2])

    clientService.modifica("1", "Nume1",  "5030326260056", [1, 2])
    clienti = clientService.getAll()

    assert len(clienti) == 1
    assert clienti[0].get_nume() == "Nume1"

    try:
        clientService.modifica("2", "Nume2", "6030818279911", [1, 2])
        assert False
    except KeyError:
        ...


def test_sterge_ClientService():
    clientRepository = ClientRepository()
    filmRepository = FilmRepository()
    clientService = ClientService(clientRepository, filmRepository)
    clientService.adaugaClient("1", "Nume", "5030326260056", [1, 2])

    clientService.sterge("1")

    clienti = clientService.getAll()
    assert len(clienti) == 0

    try:
        clientService.sterge("1234")
        assert False
    except KeyError:
        ...


def test_findById_ClientService():
    clientRepository = ClientRepository()
    filmRepository = FilmRepository()
    clientService = ClientService(clientRepository, filmRepository)
    clientService.adaugaClient("1", "Nume", "5030326260056", [1, 2])

    client = clientService.findById("1")
    assert client.get_id() == "1"

    client1 = clientService.findById("1224")
    assert client1 == None


def test_inchiriere_film_ClientService():
    clientRepository = ClientRepository()
    filmRepository = FilmRepository()
    clientService = ClientService(clientRepository, filmRepository)
    clientService.adaugaClient("1", "Nume", "5030326260056", [1, 2])
    film = Film("15", "Titlu", "Descriere", "Gen", 6)
    filmRepository.adaugaFilm(film)

    clientService.inchiriere_film("15", "1")

    clienti = clientService.getAll()
    assert clienti[0].get_lista_inchirieri() == [1, 2, '15']


def test_sortare_dupa_nume_si_numar_ClientService():
    clientRepository = ClientRepository()
    filmRepository = FilmRepository()
    clientService = ClientService(clientRepository, filmRepository)
    clientService.adaugaClient("1", "Bogdan", "5030326260051", [1, 2, 3])
    clientService.adaugaClient("2", "Alin", "5030326260052", [5, 6, 7, 8, 9, 10])
    clientService.adaugaClient("3", "Teodora", "5030326260053", [2, 5, 99, 100])
    clientService.adaugaClient("4", "Nume4", "5030326260054", [])

    sorted_list = clientService.sortare_dupa_nume_si_numar()

    assert len(sorted_list) == 3
    assert sorted_list[0].get_id() == "1"
    assert sorted_list[0].get_nume() == "Bogdan"

    assert sorted_list[1].get_lista_inchirieri() == [2, 5, 99, 100]
    assert sorted_list[1].get_nume() == "Teodora"

    assert sorted_list[2].get_cnp() == "5030326260052"
    # assert sorted_list[2].get_id() == "2"


def thirty_percent_ClientService():
    clientRepository = ClientRepository()
    filmRepository = FilmRepository()
    clientService = ClientService(clientRepository, filmRepository)
    clientService.adaugaClient("1", "Bogdan", "5030326260051", [1, 2, 3])
    clientService.adaugaClient("2", "Alin", "5030326260052", [5, 6, 7, 8, 9, 10])
    clientService.adaugaClient("3", "Teodora", "5030326260053", [2, 5, 99, 100])
    clientService.adaugaClient("4", "Nume4", "5030326260054", [])

    sorted_list = clientService.thirty_percent()

    assert len(sorted_list) == 1
    # assert sorted_list[0].get_id() == "2"
    assert sorted_list[0].get_nume() == "Alin"
    assert sorted_list[0].get_lista_inchirieri() == [5, 6, 7, 8, 9, 10]
