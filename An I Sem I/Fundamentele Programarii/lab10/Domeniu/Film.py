class Film:

    def __init__(self, id_film, titlu_film, descriere_film, gen_film):
        self.__id_film = id_film
        self.__titlu_film = titlu_film
        self.__descriere_film = descriere_film
        self.__gen_film = gen_film
        self.__stare_film = True

    def get_id_film(self):
        # returneaza id-ul de tip int id_film al unui film
        return self.__id_film

    def get_titlu_film(self):
        # returneaza titlul de tip string titlu al unui film
        return self.__titlu_film

    def get_descriere_film(self):
        # returneaza descrierea de tip string al unui film
        return self.__descriere_film

    def get_gen_film(self):
        # returneaza genul de tip string al unui film
        return self.__gen_film

    def get_stare_film(self):
        # returneaza starea filmului de tip string al unui film
        return self.__stare_film

    def set_titlu_film(self, titlu):
        '''
        modifica titlul filmului film la noul titlu string - titlu
        :param titlu: string
        :return: -
        '''
        self.__titlu_film = titlu

    def set_descriere_film(self, descriere):
        '''
        modifica descrierea filmului film la noua descriere string - descriere
        :param descriere: string
        :return:-
        '''
        self.__descriere_film = descriere

    def set_gen_film(self, gen):
        '''
        modifica genul filmului film la noul gen string - gen
        :param gen: string
        :return:-
        '''
        self.__gen_film = gen

    def set_stare_film(self):
        '''
        modifica starea filmului film la noua stare string - stare
        :return:-
        '''
        self.__stare_film = False

    def __str__(self):
        '''
        afiseaza un film
        :return:
        '''
        return f"{self.__id_film} {self.__titlu_film} {self.__descriere_film} {self.__gen_film}" \
               f" {self.__stare_film}"
