class Client:

    def __init__(self, id_client, nume, cnp, lista_inchirieri = []):
        self.__id_client = id_client
        self.__nume = nume
        self.__cnp = cnp
        self.__lista_inchirieri = lista_inchirieri

    def get_id_client(self):
        '''
        gaseste id-ul unui client
        :return: int - id_client
        '''
        return self.__id_client

    def get_nume_client(self):
        '''
        gaseste numele unui client
        :return: string - nume
        '''
        return self.__nume

    def get_cnp(self):
        '''
        gaseste cnp-ul unui client
        :return: int - cnp
        '''
        return self.__cnp

    def get_lista_inchirieri(self):
        # returneaza lista de filme inchiriate
        return self.__lista_inchirieri

    def set_nume_client(self, nume):
        '''
        seteaza numele unui client la noul nume string
        :param nume: string
        :return: -
        '''
        self.__nume = nume

    def set_lista_inchirieri(self, lista_inchirieriNoua):
        # atribuie o noua lista de filme inchiriate de catre client
        self.__lista_inchirieri = lista_inchirieriNoua

    def __str__(self):
        '''
        afiseaza un client
        :return:
        '''
        return f"{self.__id_client} {self.__nume} {self.__cnp} {self.__lista_inchirieri}"
