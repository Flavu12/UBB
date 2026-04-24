from error.repo_error import RepoError


class RepoFilme:

    def __init__(self):
        self.__filme = []

    def adauga_film(self, film):
        '''
        adauga un film in lista de filme
        :param film: film
        :return: -
        '''
        ok = 0
        for i in range(0, len(self.__filme)):
            if self.__filme[i] == film:
                ok = 1
        if ok == 1:
            raise RepoError("Film existent!")
        self.__filme.append(film)

    def sterge_film_dupa_id(self, id_film):
        '''
        sterge filmul cu id-ul int id_film
        :param id_film: int - id film
        :return: - (din dictionarul de filme se sterge filmul cu id-ul id film
        '''
        ok = 0
        for cauta_film in self.__filme:
            if cauta_film.get_id_film() == id_film:
                ok = 1
        if ok == 0:
            raise RepoError("Film inexistent!")
        for film in self.__filme:
            if film.get_id_film() == id_film:
                self.__filme.remove(film)

    def cauta_film_dupa_id(self, id_film):
        '''
        cauta un film dupa id-ul intreg id_film
        :param id_film: int - id film
        :return: filmul film cu id-ul int id_film
        '''
        ok = 0
        for cauta_film in self.__filme:
            if cauta_film.get_id_film() == id_film():
                ok = 1
        if ok == 0:
            raise RepoError("Film inexistent!")
        for film in self.__filme:
            if film.get_id_film() == id_film:
                return film

    def modifica_film(self, film):
        '''
        modifica un film din dictionarul de filme
        :param film: film
        :return: -
        '''
        ok = 0
        for cauta_film in self.__filme:
            if cauta_film.get_id_film() == film.get_id_film():
                ok = 1
        if ok == 0:
            raise RepoError("Film inexistent!")
        id = film.get_id_film()
        for cauta_film in self.__filme:
            if cauta_film.get_id_film() == id:
                self.__filme.remove(cauta_film)
        self.__filme.append(film)

    def get_all_filme(self):
        '''
        :return: returneaza dictionarul de filme
        '''
        filme = []
        for film in self.__filme:
            filme.append(film)
        return filme
