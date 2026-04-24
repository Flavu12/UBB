import random

from Domeniu.Film import Film


class ServiceFilme:

    def __init__(self, validator_film, repo_filme):
        self.__validator_film = validator_film
        self.__repo_filme = repo_filme

    def adauga_film_service(self, id_film, titlu_film, descriere_film, gen_film):
        '''
        adauga filmul film in dictionarul de filme
        :param id_film: int
        :param titlu_film: string
        :param descriere_film: string
        :param gen_film: string
        :param stare_film: string
        :return: - (la dictionarul de filme se adauga filmul film
        '''
        film = Film(id_film, titlu_film, descriere_film, gen_film)
        self.__validator_film.valideaza_film(film)
        self.__repo_filme.adauga_film(film)

    def get_all_filme_service(self):
        '''
        :return: returneaza dictionarul de filme
        '''
        return self.__repo_filme.get_all()

    def sterge_film_service(self, id_film):
        '''
        sterge un film din dictionarul de filme si clientului client corespunzator
        :param id_film: int
        :return: -
        '''
        filme = self.__repo_filme.get_all()
        for film in filme:
            if id_film == film.get_id_film():
                self.__repo_filme.sterge_film_dupa_id(id_film)

    def cauta_film_service(self, id_film):
         return self.__repo_filme.cauta_film_dupa_id(id_film)

    def filme_random(self, numere):
        lista_filme = ["Scream", "It", "Scary movie", "Star wars", "Insidious", "Amsterdam", "Annabelle",
                       "Inside out", "Ice Age", "Scarface", "Pinguinii domnului Popper", "The Perfection", "Pinocchio"]
        lista_genuri = ["horror", "comedie", "animatie", "actiune", "sf", "anime", "clasic", "crime", "documentare",
                        "drama", "thriller"]
        lista_descrieri = ["a aparut in 1996", "a aparut in 2000", "a aparut in 1999", "a aparut in 1990",
                           "a aparut in 2003", "a aparut in 2005", "a aparut in 2022", "inspirat din fapte reale"]
        ln = 1
        while numere > 0:
            film = Film(ln, random.choice(lista_filme), random.choice(lista_descrieri), random.choice(lista_genuri))
            self.__repo_filme.adauga_film(film)
            numere = numere - 1
            ln = ln + 1
