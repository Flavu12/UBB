from Domeniu.Client import Client
from Domeniu.Film import Film
from Infrastructura.repo_clienti import RepoClienti
from Infrastructura.repo_filme import RepoFilme
from Validare.validator_film import ValidatorFilm
from Validare.validator_client import ValidatorClient
from error.validation_error import ValidError

# id_client_film, id_film, titlu_film, descriere_film, gen_film
class TesteFilm:

    def __init__(self, film):
        self.__film = film

    def Testare_Filme(self):
        self.__film = Film(1, 5, "Midsommer", "Excelent", "Groaza")
        assert self.__film.get_id_client_film() == 1
        assert self.__film.get_id_film() == 5
        assert self.__film.get_titlu_film() == "Midsommer"
        assert self.__film.get_descriere_film() == "Excelent"
        assert self.__film.get_gen_film() == "Groaza"
        self.__film.set_titlu_film("Teambuilding")
        assert self.__film.get_titlu_film() == "Teambuilding"
        self.__film.set_gen_film("Comedie")
        assert self.__film.get_gen_film() == "Comedie"
        self.__film.set_descriere_film("11")
        assert self.__film.get_descriere_film() == "11"
        film_gresit = Film(0, 0, "", "", "")
        try:
            ValidatorFilm.valideaza_film(self, film_gresit)
            assert False
        except ValidError as ve:
            assert (str(ve) == "Id client invalid!\nId film invalid!\nTitlu film invalid!\nDescriere film invalida!\nGen film invalid!\n")

class TesteClient:
    def __init__(self, client):
        self.__client = client

    def Testare_Client(self):
        self.__client = Client(1, "Cena", "5030917314018")
        assert self.__client.get_id_client() == 1
        assert self.__client.get_nume_client() == "Cena"
        assert self.__client.get_cnp() == "5030917314018"
        self.__client.set_nume_client("Gergel")
        assert self.__client.get_nume_client() == "Gergel"
        client_prost = Client(0, "", 1)
        try:
            ValidatorClient.valideaza(self, client_prost)
            assert False
        except ValidError as ve:
            assert (str(ve) == "Id invalid!\nNume invalid!\nCnp invalid!\n")

class TesteRepo:
    def __init__(self):
        self.__filme = {}
        self.__clienti = {}

    def Testare_Repository_Filme(self):
        film = Film(1, 5, "Midsommer", "E smecher rau", "Groaza")
        ValidatorFilm.valideaza_film(self, film)
        lista_filme = RepoFilme()
        lista_filme.adauga_film(film)
        # assert len(lista_filme) == 1
        lista_filme.sterge_film_dupa_id(5)
        assert len(lista_filme.get_all_filme()) == 0

    def Testare_Repository_Clienti(self):
        client = Client(1, "Gergel", 5030917314018)
        ValidatorClient.valideaza(self, client)
        lista_clienti = RepoClienti()
        lista_clienti.adauga_client(client)
        assert len(lista_clienti) == 1
        lista_clienti.sterge_client_dupa_id(1)
        assert len(lista_clienti) == 0


def ruleaza_toate_testele():
    film = Film(1, 1, "", "", "")
    TesteFilm.Testare_Filme(film)
    client = Client(1, "", "")
    TesteClient.Testare_Client(client)
    lista_filme = {}
    lista_clienti = {}
    TesteRepo.Testare_Repository_Filme(lista_filme)
    TesteRepo.Testare_Repository_Clienti(lista_clienti)

ruleaza_toate_testele()
