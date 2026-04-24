class Client:

    def __init__(self, id_client, nume, cnp):
        self.__id_client = id_client
        self.__nume = nume
        self.__cnp = cnp
        self.__sters = False

    def sterge_client(self):
        '''
        seteaza un client ca fiind sters
        :return: -
        '''
        self.__sters = True

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

    def set_nume_client(self, nume):
        '''
        seteaza numele unui client la noul nume string
        :param nume: string
        :return: -
        '''
        self.__nume = nume

    def get_cnp(self):
        '''
        gaseste cnp-ul unui client
        :return: int - cnp
        '''
        return self.__cnp

    def __str__(self):
        '''
        afiseaza un client
        :return:
        '''
        return f"{self.__id_client} {self.__nume} {self.__cnp}"
