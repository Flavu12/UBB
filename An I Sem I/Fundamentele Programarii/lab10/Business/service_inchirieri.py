from Domeniu.Inchiriere import Inchiriere
from erori.repo_error import RepoError


class ServiceInchirieri:

    def __init__(self, repo_inchirieri, repo_filme, repo_clienti):
        self.__repo_inchirieri = repo_inchirieri
        self.__repo_filme = repo_filme
        self.__repo_clienti = repo_clienti

    def get_all_inchirieri_service(self):
        '''
        returneaza lista de inchirieri
        :return: o lista de obiecte de tipul Inchiriere
        '''
        return self.__repo_inchirieri.get_all()

    def adauga_inchiriere_service(self, id_inchiriere, id_film, id_client):
        '''
        adauga inchirierile de filme a unui client intr-o lista
        '''
        client = self.__repo_clienti.cauta_client_dupa_id(id_client)
        film = self.__repo_filme.cauta_film_dupa_id(id_film)
        if film.get_stare_film():
            inchiriere = Inchiriere(id_inchiriere, id_film, id_client)
            film.set_stare_film()
            self.__repo_inchirieri.adauga_inchiriere(inchiriere)

    def sterge_film_si_inchirieri(self, id_film):
        '''
        sterge un film dupa id si inchirierile sale
        :param id_film: int
        :return:-
        '''
        lista_de_sters = []
        film = self.__repo_filme.cauta_film_dupa_id(id_film)
        inchirieri = self.__repo_inchirieri.get_all()
        for inchiriere in inchirieri:
            filmulet = self.__repo_filme.cauta_film_dupa_id(inchiriere.get_id_film())
            if filmulet.get_titlu_film() == film.get_titlu_film():
                lista_de_sters.append(inchiriere.get_id_inchiriere())

        for l in lista_de_sters:
            self.__repo_inchirieri.sterge_inchiriere_dupa_id(l)
        self.__repo_filme.sterge_film_dupa_id(id_film)

    def sterge_client_si_inchirieri(self, id_client):
        '''
        sterge un client dupa id si inchirierile sale
        :param id_client: int
        :return:-
        '''
        lista_de_sters = []
        client = self.__repo_clienti.cauta_client_dupa_id(id_client)
        inchirieri = self.__repo_inchirieri.get_all()
        for inchiriere in inchirieri:
            clientt = self.__repo_clienti.cauta_client_dupa_id(inchiriere.get_id_client())
            if clientt.get_nume_client() == client.get_nume_client():
                lista_de_sters.append(inchiriere.get_id_inchiriere())

        for l in lista_de_sters:
            self.__repo_inchirieri.sterge_inchiriere_dupa_id(l)
        self.__repo_clienti.sterge_client_dupa_id(id_client)

    def sterge_inchiriere_service(self, id_inchiriere):
        '''
        sterge o inchiriere din dictionarul de inchirieri
        :param id_inchiriere: int
        :return: -
        '''
        inchirieri = self.__repo_inchirieri.get_all()
        for inchiriere in inchirieri:
            if id_inchiriere == inchiriere.get_id_inchiriere():
                self.__repo_inchirieri.sterge_inchiriere_dupa_id(id_inchiriere)