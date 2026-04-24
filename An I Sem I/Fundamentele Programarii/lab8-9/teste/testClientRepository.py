#functiile testeaza repository-ul aplicatiei pentru client
from domeniu.entitati import Client
from Infrastructura.clientRepository import ClientRepository


def test_getAll_ClientRepository():
    clientRepository = ClientRepository()
    client = Client("1", "Nume", "5030326260056", [1,2])
    clientRepository.adaugaClient(client)

    clienti = clientRepository.getAll()
    assert len(clienti) == 1
    assert clienti[0].get_id() == "1"

def test_getById_ClientRepository():
    clientRepository = ClientRepository()
    client = Client("1", "Nume", "5030326260056", [1,2])
    clientRepository.adaugaClient(client)

    client1 = clientRepository.getById(client.get_id())

    assert client1.get_id() == "1"
    assert client1.get_nume() == "Nume"

def test_adaugaClient_ClientRepository():
    clientRepository = ClientRepository()
    client = Client("1", "Nume", "5030326260056", [1,2])
    clientRepository.adaugaClient(client)

    clienti = clientRepository.getAll()
    assert len(clienti) == 1
    assert clienti[0].get_id() == "1"

    try:
        clientRepository.adaugaClient(client)
        assert False
    except KeyError:
        ...

def test_modifica_ClientRepository():
    clientRepository = ClientRepository()
    client1 = Client("13", "Nume1", "5030326260056", [1, 3])
    client2 = Client("13", "Nume2", "5030326260057", [1, 4])
    client3 = Client("166", "Nume3", "5030326260058", [1, 5])
    clientRepository.adaugaClient(client1)

    clientRepository.modifica(client2)

    clienti = clientRepository.getAll()
    assert clienti[0].get_nume() == "Nume2"

    try:
        clientRepository.modifica(client3)
        assert False
    except KeyError:
        ...

def test_sterge_ClientRepository():
    clientRepository = ClientRepository()
    client = Client("13", "Nume", "5030326260056", [1, 2])
    clientRepository.adaugaClient(client)

    clientRepository.sterge(client.get_id())

    clienti = clientRepository.getAll()
    assert len(clienti) == 0

    try:
        clientRepository.sterge("423432")
        assert False
    except KeyError:
        ...