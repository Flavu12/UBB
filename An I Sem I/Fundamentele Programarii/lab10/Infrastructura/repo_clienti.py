from erori.repo_error import RepoError


class RepoClienti:

    def __init__(self):
        self.__clienti = {}

    def adauga_client(self, client):
        if client.get_id_client() in self.__clienti:
            raise RepoError("client deja existent!")
        self.__clienti[client.get_id_client()] = client

    def sterge_client_dupa_id(self, id_client):
        if id_client not in self.__clienti:
            raise RepoError("Client inexistent!")
        del self.__clienti[id_client]

    def cauta_client_dupa_id(self, id_client):
        if id_client not in self.__clienti:
            raise RepoError("client inexistent!")
        return self.__clienti[id_client]

    def modifica_client(self, client):
        if client.get_id_client() not in self.__clienti:
            raise RepoError("client inexistent!")
        self.__clienti[client.get_id_client()] = client

    def get_all(self):
        clienti = []
        for id_client in self.__clienti:
            clienti.append(self.__clienti[id_client])
        return clienti

    def __len__(self):
        return len(self.__clienti)
