class Film:
    def __init__(self, id, titlu, descriere, gen, nrf):
        #se vor atribui valori atributelor din clasa Film
        self.__id = id
        self.__titlu = titlu
        self.__descriere = descriere
        self.__gen = gen
        self.__nrf = nrf

    def get_id(self):
        #returneaza id-ul filmului
        return self.__id

    def get_titlu(self):
        #returneaza titlul filmului
        return self.__titlu

    def get_descriere(self):
        #returneaza descrierea filmului
        return self.__descriere

    def get_gen(self):
        #returneaza genul filmului
        return self.__gen

    def get_nrf(self):
        #returneaza numarul de filme inchiriate
        return self.__nrf

    def set_id(self, idNou):
        #atribuie un nou id
        self.__id = idNou

    def set_titlu(self, titluNou):
        #atribuie un nou titlu
        self.__titlu = titluNou

    def set_descriere(self, descriereNoua):
        #atribuie o noua descriere
        self.__descriere = descriereNoua

    def set_gen(self, genNou):
        #atribuie un gen nou
        self.__gen = genNou

    def set_nrf(self, nrfNou):
        #atribuie o valoare noua pentru numarul de filme inchiriate
        self.__nrf = nrfNou

    def __str__(self):
        #returneaza un sir de caractere care contine toate atributele filmului impreuna cu valorile lor
        return f"id: {self.__id} titlu: {self.__titlu} descriere: {self.__descriere} gen: {self.__gen} nrf: {self.__nrf}"

class Client:
    def __init__(self, idClient, nume, cnp, lista_inchirieri =[]):
        #se vor atribui valorile din clasa Client
        self.__idClient = idClient
        self.__nume = nume
        self.__cnp = cnp
        self.__lista_inchirieri = lista_inchirieri

    def get_id(self):
        #returneaza id-ul clientului
        return self.__idClient

    def get_nume(self):
        #returneaza numele clientului
        return self.__nume

    def get_cnp(self):
        #returneaza cnp-ul clientului
        return self.__cnp

    def get_lista_inchirieri(self):
        #returneaza lista de filme inchiriate
        return self.__lista_inchirieri

    def set_id(self, idNou):
        #atribuie un nou id clientului
        self.__idClient = idNou

    def set_nume(self, numeNou):
        #atribuie un nou nume clientului
        self.__nume = numeNou

    def set_cnp(self, cnpNou):
        #atribuie un nou cnp clientului
        self.__cnp = cnpNou

    def set_lista_inchirieri(self, lista_inchirieriNoua):
        #atribuie o noua lista de filme inchiriate de catre client
        self.__lista_inchirieri = lista_inchirieriNoua

    def __str__(self):
        #returneaza un sir de caractere care contine toate atributele clientului impreuna cu valorile acestora
        return f"id: {self.__idClient} nume: {self.__nume} cnp: {self.__cnp} Filme inchiriate: {self.__lista_inchirieri}"
