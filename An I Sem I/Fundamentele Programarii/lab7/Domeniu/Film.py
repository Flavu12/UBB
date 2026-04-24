class Film:

    def __init__(self, id_client_film, id_film, titlu_film, descriere_film, gen_film):
        self.__id_client_film = id_client_film
        self.__id_film = id_film
        self.__titlu_film = titlu_film
        self.__descriere_film = descriere_film
        self.__gen_film = gen_film
        self.__sters = False

    def get_descriere_film(self):
        '''
        gaseste descrierea unui film
        :return: string - descriere film
        '''
        return self.__descriere_film

    def get_gen_film(self):
        '''
        :return: string - gen film
        '''
        return self.__gen_film

    def get_id_film(self):
        '''
        :return: int - id film
        '''
        return self.__id_film

    def get_id_client_film(self):
        '''
        gaseste id-ul clientului care are asociat filmul film
        :return: int - id_client
        '''
        return self.__id_client_film

    def get_titlu_film(self):
        '''
        gaseste titlul filmului film
        :return: string - titlu_film
        '''
        return self.__titlu_film

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
        :return:
        '''
        self.__descriere_film = descriere

    def set_gen_film(self, gen):
        '''
        modifica genul filmului film la noul gen string - gen
        :param gen: string
        :return:
        '''
        self.__gen_film = gen

    def sterge(self):
        '''
        seteaza filmul film ca fiind sters
        :return: -
        '''
        self.__sters = True

    def get_sters(self):
        '''
        :return: 1, daca filmul e setat ca fiind sters si 0, daca filmul nu este setat ca fiind sters
        '''
        return self.__sters
