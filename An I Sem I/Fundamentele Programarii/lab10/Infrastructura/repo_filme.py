from erori.repo_error import RepoError


class RepoFilme:

    def __init__(self):
        self.__filme = {}

    def adauga_film(self, film):
        '''
        se va adauga un film la un dictionar de filme
        :param film:
        :return: -
        '''
        if film.get_id_film() in self.__filme:
            raise RepoError("film deja existent!")
        self.__filme[film.get_id_film()] = film

    def sterge_film_dupa_id(self, id_film):
        '''
        se va sterge un film din dictionarul de filme dupa id-ul lui
        :param id_film: int
        :return: dictionarul de filme fara filmul cu id-ul ales
        '''
        if self.cauta_film_dupa_id(id_film) is None:
            raise RepoError("film Inexistent")
        self.__filme.pop(id_film)

    def cauta_film_dupa_id(self, id_film):
        '''
        se va cauta un film din dictionarul de filme dupa id-ul lui
        :param id_film:int
        :return: filmul cu id-ul specificat
        '''
        if id_film not in self.__filme:
            raise RepoError("film inexistent!")
        return self.__filme[id_film]

    def modifica_film(self, film):
        '''
        se va modifica un film din dictionarul de filme dupa id-ul de film
        :param film:
        :return:-
        '''
        if film.get_id_film() not in self.__filme:
            raise RepoError("film inexistent!")
        self.__filme[film.get_id_film()] = film

    def get_all(self):
        '''
        returneaza o lista de filme din dictionarul de filme
        :return:
        '''
        filme = []
        for id_film in self.__filme:
            filme.append(self.__filme[id_film])
        return filme

    def __len__(self):
        return len(self.__filme)
