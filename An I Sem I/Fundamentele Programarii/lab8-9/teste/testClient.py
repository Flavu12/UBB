#functiile testeaza domeniul aplicatiei pentru client
from domeniu.entitati import Client


def testClient_get():
    client = Client("1", "Nume", "5030326260056", [1,2])

    assert client.get_id() == "1"
    assert client.get_nume() == "Nume"
    assert client.get_cnp() == "5030326260056"
    assert client.get_lista_inchirieri() == [1,2]

def testClient_set():
    client = Client("1", "Nume", "5030326260056", [1, 2])

    client.set_id("4")
    assert client.get_id() == "4"

    client.set_nume("M")
    assert client.get_nume() == "M"

    client.set_cnp("5030326260055")
    assert client.get_cnp() == "5030326260055"

    client.set_lista_inchirieri([1,2,3,4])
    assert client.get_lista_inchirieri() == [1,2,3,4]
