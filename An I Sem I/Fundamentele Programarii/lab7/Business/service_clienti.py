from Domeniu.Client import Client

class ServiceClienti:

    def __init__(self, validator_client, repo_clienti):
        self.__validator_client = validator_client
        self.__repo_clienti = repo_clienti

    def adauga_client(self, id_client, nume, cnp):
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
        return self.__repo_clienti.get_all_clienti()
