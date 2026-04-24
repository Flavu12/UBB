from error.repo_error import RepoError


class RepoClienti:

    def __init__(self):
        self.__clienti = []

    def adauga_client(self, client):
        '''
        adauga un client la dictionarul de clienti
        :param client: client
        :return: -
        '''
        ok = 0
        for cauta_client in self.__clienti:
            if cauta_client.get_id_client() == client.get_id_client():
                ok = 1
        if ok == 1:
            raise RepoError("Client existent!")
        self.__clienti.append(client)

    def sterge_client_dupa_id(self, id_client):
        '''
        sterge un client din dictionarul de clienti pe baza id_client
        :param id_client: int - id client
        :return: -
        '''
        ok = 0
        for client in self.__clienti:
            if client.get_id_client() == id_client:
                ok = 1
        if ok == 0:
            raise RepoError("Client inexistent!")
        for client in self.__clienti:
            if client.get_id_client() == id_client:
                 self.__clienti.remove(client)

    def cauta_client_dupa_id(self, id_client):
        '''
        cauta un client in dictionarul de clienti dupa id client
        :param id_client: int - id client
        :return: clientul cu id-ul id_clien - int
        '''
        ok = 0
        for client in self.__clienti:
            if client.get_id_client() == id_client:
                ok = 1
        if ok == 0:
            raise RepoError("Client inexistent!")
        for client in self.__clienti:
            if client.get_id_client() == id_client:
                return client

    def modifica_client(self, client):
        '''
        modifica un client din dictionarul de clienti
        :param client: client
        :return: - (dictionarul de clienti sufera o modificare a unui client)
        '''
        ok = 0
        for client in self.__clienti:
            if client.get_id_client() == id_client:
                ok = 1
        if ok == 0:
            raise RepoError("Client inexistent!")
        id = client.get_id_client()
        for cauta_client in self.__clienti:
            if cauta_client.get_id_client() == id:
                self.__clienti.remove(cauta_client)
        self.__clienti.append(client)

    def get_all_clienti(self):
        '''
        returneaza toti clientii din dictionarul de clienti
        :return: dictionarul de clienti
        '''
        clienti = []
        for client in self.__clienti:
            clienti.append(client)
        return clienti

    def __len__(self):
        '''
        :return: lungimea dictionarului de clienti
        '''
        return len(self.__clienti)