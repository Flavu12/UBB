class Inchiriere:
    def __init__(self, id_inchiriere, id_film, id_client):
        self.__id_inchiriere = id_inchiriere
        self.__id_film = id_film
        self.__id_client = id_client

    def get_id_film(self):
        # returneaza id-ul filmului din inchiriere
        return self.__id_film

    def get_id_inchiriere(self):
        # returneaza id-ul inchirierii
        return self.__id_inchiriere

    def get_id_client(self):
        #returneaza id-ul clientului care are inchirierea
        return self.__id_client


    def __str__(self):
        '''
        afiseaza inchirierile unui film
        :return:
        '''
        return f"{self.__id_inchiriere} {self.__id_film} {self.__id_client}"
