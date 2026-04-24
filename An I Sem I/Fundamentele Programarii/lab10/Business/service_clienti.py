from Domeniu.Client import Client
import random

class ServiceClienti:

    def __init__(self, validator_client, repo_clienti):
        self.__validator_client = validator_client
        self.__repo_clienti = repo_clienti

    def adauga_client_service(self, id_client, nume, cnp):
        '''
        adauga un client in dictionarul de clienti
        :param id_client: int
        :param nume: string
        :param cnp: int
        :return:
        '''
        client = Client(id_client, nume, cnp)
        self.__validator_client.valideaza(client)
        self.__repo_clienti.adauga_client(client)

    def get_all_clienti_service(self):
        '''
        :return: returneaza dictionarul de clienti
        '''
        return self.__repo_clienti.get_all()

    def cauta_clienti_service(self, id_client):
        return self.__repo_clienti.cauta_client_dupa_id(id_client)

    def sterge_client_service(self, id_client):
        '''
        sterge un client din dictionarul de clienti
        :param id_client: int
        :return: -
        '''
        clienti = self.__repo_clienti.get_all()
        for client in clienti:
            if id_client == client.get_id_client():
                self.__repo_clienti.sterge_client_dupa_id(id_client)

    def clienti_random(self, numere):
        nume = self.__repo_clienti.get_all()
        ln = 1
        lista_cnp = ["5234567891234", "6345678912345", "5456789123456", "5567891234567", "6031211234432", "6021212287765"]
        lista_nume = ["Ana", "Ion", "Alex", "Maria", "Sebi", "Flavia", "Alexandra", "Mihnea", "Teodora"]
        while numere > 0:
            client = Client(ln, random.choice(lista_nume), random.choice(lista_cnp))
            self.__repo_clienti.adauga_client(client)
            numere = numere - 1
            ln = ln + 1
