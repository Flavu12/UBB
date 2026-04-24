from domeniu.entitati import Client
from Infrastructura.clientRepository import ClientRepository
from Infrastructura.filmRepository import FilmRepository


class ClientService:
    def __init__(self, clientRepository: ClientRepository, filmRepository: FilmRepository):
        # in ClientService se va crea un nou ClientRepository
        # in ClientService se va crea un nou FilmRepository
        self.__clientRepository = clientRepository
        self.__filmRepository = filmRepository

    def getAll(self):
        # returneaza o lista cu toti clientii
        return self.__clientRepository.getAll()

    def adaugaClient(self, idClient, nume, cnp, lista_inchirieri):
        # adauga un nou client in dictionar daca acesta nu se afla deja in dictionar, in caz contar returneaza un KeyError
        client = Client(idClient, nume, cnp, lista_inchirieri)
        self.__clientRepository.adaugaClient(client)

    def modifica(self, idClient, numeNou, cnpNou, lista_inchirieriNoua):
        # face update unui client daca se afla in dictionar, altfel returneaza un KeyError
        client = Client(idClient, numeNou, cnpNou, lista_inchirieriNoua)
        self.__clientRepository.modifica(client)

    def sterge(self, idClient):
        # sterge un client dupa un id daca se afla in dictionar, altfel returneaza un KeyError
        self.__clientRepository.sterge(idClient)

    def findById(self, idClient):
        # in cazul in care exista un client dupa un id returneaza clientul altfel returneaza None
        return self.__clientRepository.getById(idClient)

    def inchiriere_film(self, idFilm, idClient):
        # verifica daca exista un client in dictionar dupa id-ul dat si adauga listei de filme inchiriate id-ul filmului transmis
        # in caz contrar modifica numarul de inchirieri la filmul cu id-ul transmis cu -1 si returneaza un KeyError
        if self.findById(idClient) is None:
            film = self.__filmRepository.getById(idFilm)
            numar_inchirieri = film.get_nrf()
            numar_inchirieri -= 1
            film.set_nrf(numar_inchirieri)
            self.__filmRepository.modifica(film)
            raise KeyError("there is no client with the given id!")
        client = self.__clientRepository.getById(idClient)
        lista_inchirieri = client.get_lista_inchirieri()
        lista_inchirieri.append(idFilm)
        self.modifica(idClient, client.get_nume(), client.get_cnp(), lista_inchirieri)

    def sortare_dupa_nume_si_numar(self):
        # sorteaza crescator lista de clienti cu filme inchiriate dupa nume iar mai apoi dupa numarul de filme inchiriate
        lista_clienti = self.getAll()
        for i in lista_clienti:
            if len(i.get_lista_inchirieri()) == 0:
                lista_clienti.remove(i)

        aux = Client("0", "0", "0", [])

        for i in range(0, len(lista_clienti) - 1):
            for j in range(i + 1, len(lista_clienti)):
                nume1 = lista_clienti[i].get_nume()
                nume2 = lista_clienti[j].get_nume()
                if nume1 > nume2:
                    aux.set_id(lista_clienti[i].get_id())
                    aux.set_nume(lista_clienti[i].get_nume())
                    aux.set_cnp(lista_clienti[i].get_cnp())
                    aux.set_lista_inchirieri(lista_clienti[i].get_lista_inchirieri())

                    lista_clienti[i].set_id(lista_clienti[j].get_id())
                    lista_clienti[i].set_nume(lista_clienti[j].get_nume())
                    lista_clienti[i].set_cnp(lista_clienti[j].get_cnp())
                    lista_clienti[i].set_lista_inchirieri(lista_clienti[j].get_lista_inchirieri())

                    lista_clienti[j].set_id(aux.get_id())
                    lista_clienti[j].set_nume(aux.get_nume())
                    lista_clienti[j].set_cnp(aux.get_cnp())
                    lista_clienti[j].set_lista_inchirieri(aux.get_lista_inchirieri())

        for i in range(0, len(lista_clienti) - 1):
            for j in range(i + 1, len(lista_clienti)):
                l1 = lista_clienti[i].get_lista_inchirieri()
                l1l = len(l1)
                l2 = lista_clienti[j].get_lista_inchirieri()
                l2l = len(l2)
                if l1l > l2l:
                    aux.set_id(lista_clienti[i].get_id())
                    aux.set_nume(lista_clienti[i].get_nume())
                    aux.set_cnp(lista_clienti[i].get_cnp())
                    aux.set_lista_inchirieri(lista_clienti[i].get_lista_inchirieri())

                    lista_clienti[i].set_id(lista_clienti[j].get_id())
                    lista_clienti[i].set_nume(lista_clienti[j].get_nume())
                    lista_clienti[i].set_cnp(lista_clienti[j].get_cnp())
                    lista_clienti[i].set_lista_inchirieri(lista_clienti[j].get_lista_inchirieri())

                    lista_clienti[j].set_id(aux.get_id())
                    lista_clienti[j].set_nume(aux.get_nume())
                    lista_clienti[j].set_cnp(aux.get_cnp())
                    lista_clienti[j].set_lista_inchirieri(aux.get_lista_inchirieri())

        return lista_clienti

    def thirty_percent(self):
        # sorteaza crescator lista de clienti cu filme inchiriate dupa numarul de filme inchiriate
        # si returneaza o lista cu primii 30% din lista
        l = self.getAll()
        for i in l:
            if len(i.get_lista_inchirieri()) == 0:
                l.remove(i)
        aux1 = Client("0", "0", "0", [])
        for i in range(0, len(l) - 1):
            for j in range(i + 1, len(l)):
                list1 = l[i].get_lista_inchirieri()
                list1_len = len(list1)
                list2 = l[j].get_lista_inchirieri()
                list2_len = len(list2)
                if (list1_len < list2_len):
                    aux1.set_id(l[i].get_id())
                    aux1.set_nume(l[i].get_nume())
                    aux1.set_cnp(l[i].get_cnp())
                    aux1.set_lista_inchirieri(l[i].get_lista_inchirieri())

                    l[i].set_id(l[j].get_id())
                    l[i].set_nume(l[j].get_nume())
                    l[i].set_cnp(l[j].get_cnp())
                    l[i].set_lista_inchirieri(l[j].get_lista_inchirieri())

                    l[j].set_id(aux1.get_id())
                    l[j].set_nume(aux1.get_nume())
                    l[j].set_cnp(aux1.get_cnp())
                    l[j].set_lista_inchirieri(aux1.get_lista_inchirieri())

        rez_list = []
        len_rez_list = (30 * len(l)) // 100
        len_rez_list += 1
        for i in range(0, len_rez_list):
            rez_list.append(l[i])
        return rez_list
