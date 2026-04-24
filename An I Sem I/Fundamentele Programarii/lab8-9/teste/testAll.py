from teste.testClient import testClient_get, testClient_set
from teste.testClientRepository import *
from teste.testClientService import *
from teste.testFilm import testFilm_set, testFilm_get
from teste.testFilmRepository import *
from teste.testFilmService import *


def testAll():
    #functia apeleaza toate testele aplicatiei
    testClient_get()
    testClient_set()

    test_getAll_ClientRepository()
    test_getById_ClientRepository()
    test_adaugaClient_ClientRepository()
    test_modifica_ClientRepository()
    test_sterge_ClientRepository()

    test_getAll_ClientService()
    test_adaugaClient_ClientService()
    test_modifica_ClientService()
    test_sterge_ClientService()
    test_findById_ClientService()
    test_inchiriere_film_ClientService()
    test_sortare_dupa_nume_si_numar_ClientService()
    thirty_percent_ClientService()

    testFilm_get()
    testFilm_set()

    test_getAll_FilmRepository()
    test_getById_FilmRepository()
    test_adaugaFilm_FilmRepository()
    test_modifica_FilmRepository()
    test_sterge_FilmRepostiory()

    test_getALL_FilmService()
    test_adaugaFilm_FilmService()
    test_modifica_FilmService()
    test_sterge_FilmService()
    test_findById_FilmService()
    test_inchiriere_dupa_id_FilmService()
    test_inchiriere_film_sortare_FilmService()
