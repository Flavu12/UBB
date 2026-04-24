from Business.service_clienti import ServiceClienti
from Domeniu.Client import Client
from Infrastructura.repo_clienti import RepoClienti
from Validare.validator_client import ValidatorClient
from erori.repo_error import RepoError


def teste_domeniu():
    client = Client("1", "Ana", 6030101200025)

    assert client.get_id_client() == "1"
    assert client.get_nume_client() == "Ana"

    client.set_nume_client("Maria")
    assert client.get_nume_client() == "Maria"

# Teste Repository


def test_adauga_client_repo():
    clienti_repo = RepoClienti()
    client1 = Client("1", "Ana", 6030101200025)

    clienti_repo.adauga_client(client1)

    clienti = clienti_repo.get_all()
    assert len(clienti) == 1
    assert clienti[0].get_id_client() == "1"
    client2 = Client("1", "Alex", 5030201200025)
    try:
        clienti_repo.adauga_client(client2)
        assert False
    except RepoError:
        ...


def test_get_all_repo():
    clienti_repo = RepoClienti()
    client1 = Client("1", "Ana", 6030101200025)
    client2 = Client("2", "Alex", 5030201200025)
    clienti_repo.adauga_client(client1)
    clienti_repo.adauga_client(client2)

    clienti = clienti_repo.get_all()
    assert len(clienti) == 2
    assert clienti[0].get_id_client() == "1"
    assert clienti[1].get_id_client() == "2"


def test_cauta_dupa_id_repo():
    clienti_repo = RepoClienti()
    client1 = Client("1", "Ana", 6030101200025)
    clienti_repo.adauga_client(client1)

    client = clienti_repo.cauta_client_dupa_id("1")
    assert client.get_nume_client() == "Ana"


def test_modifica_repo():
    clienti_repo = RepoClienti()
    client1 = Client("1", "Ana", 6030101200025)
    client2 = Client("1", "Maria", 6030506234432)
    client3 = Client("2", "Alex", 5021010445566)

    clienti_repo.adauga_client(client1)
    clienti_repo.modifica_client(client2)

    clienti = clienti_repo.get_all()
    assert clienti[0].get_nume_client() == "Maria"

    try:
        clienti_repo.modifica_client(client3)
        assert False
    except RepoError:
        ...


def test_sterge_repo():
    clienti_repo = RepoClienti()
    client1 = Client("1", "Ana", 6030101200025)
    clienti_repo.adauga_client(client1)

    clienti_repo.sterge_client_dupa_id(client1.get_id_client())

    assert len(clienti_repo.get_all()) == 0

    try:
        clienti_repo.sterge_client_dupa_id("23423")
        assert False
    except RepoError:
        ...

# Teste Service


def test_adauga_client_service():
    clienti_repo = RepoClienti()
    clienti_validare = ValidatorClient()
    clienti_service = ServiceClienti(clienti_validare, clienti_repo)
    clienti_service.adauga_client_service("1", "Ana", 6030101200025)

    clienti = clienti_service.get_all_clienti_service()
    assert len(clienti) == 1
    assert clienti[0].get_id_client() == "1"

    try:
        clienti_service.adauga_client_service("1", "Maria", 60331111202721)
        assert False
    except RepoError:
        ...


def test_cauta_client_dupa_id_service():
    clienti_repo = RepoClienti()
    clienti_validare = ValidatorClient()
    clienti_service = ServiceClienti(clienti_validare, clienti_repo)
    clienti_service.adauga_client_service("1", "Ana", 6030101200025)

    client = clienti_service.cauta_clienti_service("1")
    assert client.get_id_client() == "1"
    assert client.get_nume_client() == "Ana"

    client2 = clienti_service.cauta_clienti_service("44")
    assert client2 == None


def test_sterge_client_service():
    clienti_repo = RepoClienti()
    clienti_validare = ValidatorClient()
    clienti_service = ServiceClienti(clienti_validare, clienti_repo)
    clienti_service.adauga_client_service("1", "Ana", 6030101200025)

    clienti_service.sterge_client_service("1")

    clienti = clienti_service.get_all_clienti_service()
    assert len(clienti) == 0

    try:
        clienti_service.sterge_client_service("12")
        assert False
    except RepoError:
        ...


def test_get_all_service():
    clienti_repo = RepoClienti()
    clienti_validare = ValidatorClient()
    clienti_service = ServiceClienti(clienti_validare, clienti_repo)
    clienti_service.adauga_client_service("1", "Ana", 6030101200025)
    clienti_service.adauga_client_service("2", "Alex", 5021102200026)

    clienti = clienti_service.get_all_clienti_service()
    assert len(clienti) == 2
    assert clienti[0].get_id_client() == "1"
    assert clienti[1].get_id_client() == "2"


def ruleaza_toate_testele_clienti():
    teste_domeniu()
    test_adauga_client_repo()
    test_get_all_repo()
    test_cauta_dupa_id_repo()
    test_modifica_repo()
    test_sterge_repo()
    test_adauga_client_service()
    test_cauta_client_dupa_id_service()
    test_sterge_client_service()
    test_get_all_service()
