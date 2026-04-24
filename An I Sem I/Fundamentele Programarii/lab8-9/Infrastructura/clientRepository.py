class ClientRepository:
    def __init__(self):
        # se va crea un dictionar pentru a stoca datele filmului
        self.__all_clients_dict = {}

    def getAll(self):
        # returneaza o lista cu toti clientii
        return list(self.__all_clients_dict.values())

    def getById(self, idClient):
        # in cazul in care exista un client dupa un id returneaza clientul altfel returneaza None
        if idClient in self.__all_clients_dict:
            return self.__all_clients_dict[idClient]
        return None

    def adaugaClient(self, client):
        # adauga un nou client in dictionar daca acesta nu se afla deja in dictionar, in caz contar returneaza un KeyError
        if self.getById(client.get_id()) is not None:
            raise KeyError("there is already a client with the given id!")
        self.__all_clients_dict[client.get_id()] = client

    def modifica(self, clientNou):
        # face update unui client daca se afla in dictionar, altfel returneaza un KeyError
        if self.getById(clientNou.get_id()) is None:
            raise KeyError("there is no client with the given id!")
        self.__all_clients_dict[clientNou.get_id()] = clientNou

    def sterge(self, idClient):
        # sterge un client dupa un id daca se afla in dictionar, altfel returneaza un KeyError
        if self.getById(idClient) is None:
            raise KeyError("there is no client with the given id!")
        self.__all_clients_dict.pop(idClient)