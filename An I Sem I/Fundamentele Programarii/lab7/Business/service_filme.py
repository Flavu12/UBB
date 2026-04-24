from Domeniu.Film import Film

class ServiceFilme:

    def __init__(self, validator_film, repo_filme, repo_clienti):
        self.__validator_film = validator_film
        self.__repo_filme = repo_filme
        self.__repo_clienti = repo_clienti

    def sterge_client_si_filmele_lui(self, id_client):
        '''
        sterge un client client din dictionarul de clienti si filmele film corespunzatoare lui din dictionarul de filme
        :param id_client: int - id client
        :return: -
        '''
        filme = self.__repo_filme.get_all_filme()
        filme_client = [x for x in filme if x.get_id_client_film() == id_client]
        for film_client in filme_client:
            self.__repo_filme.sterge_film_dupa_id(film_client.get_id_film())
        self.__repo_clienti.sterge_client_dupa_id(id_client)

    def adauga_film_service(self, id_client, id_film, titlu_film, descriere_film, gen_film):
        '''
        adauga filmul film in dictionarul de filme
        :param id_client: int
        :param id_film: int
        :param titlu_film: string
        :param descriere_film: string
        :param gen_film: string
        :return: - (la dictionarul de filme se adauga filmul film
        '''
        film = Film(id_client, id_film, titlu_film, descriere_film, gen_film)
        self.__validator_film.valideaza_film(film)
        self.__repo_filme.adauga_film(film)

    def get_all_filme_service(self):
        '''
        :return: returneaza dictionarul de filme
        '''
        return self.__repo_filme.get_all_filme()

    def sterge_film(self, id_client, id_film):
        '''
        sterge un film din dictionarul de filme si clientului client corespunzator
        :param id_client: int
        :param id_film: int
        :return: -
        '''
        filme = self.__repo_filme.get_all_filme()
        filme_client = [x for x in filme if x.get_id_client_film() == id_client]
        for film_client in filme_client:
            if id_film == film_client.get_id_film():
                self.__repo_filme.sterge_film_dupa_id(id_film)