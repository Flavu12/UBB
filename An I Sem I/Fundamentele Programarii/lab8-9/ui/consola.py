from business.clientService import ClientService
from business.filmService import FilmService
from teste.errors import *
from teste.input_data_validation import Validation_addFilm, Validation_addClient, Validation_updateFilm, \
    Validation_updateClient


class Consola:
    def __init__(self, filmService: FilmService, clientService: ClientService):
        self.__filmService = filmService
        self.__clientService = clientService

    def adaugaFilm(self):
        try:
            #in functie se vor citi de la tastatura datele filmului
            idFilm = input("Dati id-ul filmului: ")
            titluFilm = input("Dati titlul filmului: ")
            descriereFilm = input("Dati descrierea filmului: ")
            genFilm = input("Dati genul filmului: ")
            inchirieri_film = 0
            validation_addFilm = Validation_addFilm(idFilm, titluFilm,descriereFilm,genFilm)
            validation_addFilm.test_idFilm()
            validation_addFilm.test_TitluFilm()
            validation_addFilm.test_descriereFilm()
            validation_addFilm.test_genFilm()
            self.__filmService.adaugaFilm(idFilm,titluFilm,descriereFilm,genFilm,inchirieri_film)
        except KeyError as e:
            print(e)
        except IdError as ie:
            print(ie)
        except IdErrorEmpty as iee:
            print(iee)
        except IdErrorNumeric as ien:
            print(ien)
        except TitleErrorEmpty as tee:
            print(tee)
        except DescriptionErrorEmpty as dee:
            print(dee)
        except NameErrorEmpty as aee:
            print(aee)
        except NameErrorAlpha as aea:
            print(aea)


    def adaugaClient(self):
        try:
            # in functie se vor citi de la tastatura datele clientului
            idClient = input("Dati id-ul clientului: ")
            numeClient = input("Dati numele clientului: ")
            cnpClient = input("Dati cnp-ul clientului: ")
            lista_inchirieri_clienti = []
            validation_addClient = Validation_addClient(idClient, numeClient, cnpClient)
            validation_addClient.test_idClient()
            validation_addClient.test_nume()
            validation_addClient.test_cnpClient()
            self.__clientService.adaugaClient(idClient, numeClient, cnpClient, lista_inchirieri_clienti)
        except KeyError as e:
            print(e)
        except IdErrorEmpty as iee:
            print(iee)
        except IdError as ie:
            print(ie)
        except IdErrorNumeric as ien:
            print(ien)
        except NameErrorEmpty as aee:
            print(aee)
        except NameErrorAlpha as aea:
            print(aea)
        except CnpErrorEmpty as cee:
            print(cee)
        except CnpErrorNegative as cen:
            print(cen)
        except CnpErrorLength as cel:
            print(cel)
        except CnpErrorS as ces:
            print(ces)
        except CnpErrorNumeric as cenu:
            print(cenu)
        except CnpErrorInvalid as cei:
            print(cei)

    def modificaFilm(self):
        try:
            #in functie se vor citi date noi de la tastatura pentru un film identificat printr-un id
            idFilm = input("Dati id-ul filmului de modificat: ")
            titluNou = input("Dati noul titlu al filmului: ")
            descriereNoua = input("Dati noua descriere a filmului: ")
            genNou = input("Dati noul gen al filmului: ")
            inchirieri_filmNou = input("Dati noul numar de inchirieri al filmului: ")
            validation_modificaFilm = Validation_updateFilm(idFilm, titluNou, descriereNoua,genNou,inchirieri_filmNou)
            self.__filmService.modifica(idFilm,titluNou,descriereNoua,genNou,inchirieri_filmNou)
        except KeyError as e:
            print(e)
        except IdError as ie:
            print(ie)
        except IdErrorEmpty as iee:
            print(iee)
        except IdErrorNumeric as ien:
            print(ien)
        except TitleErrorEmpty as tee:
            print(tee)
        except DescriptionErrorEmpty as dee:
            print(dee)
        except NameErrorEmpty as aee:
            print(aee)
        except NameErrorAlpha as aea:
            print(aea)
        except InchiriereErrorValue as rev:
            print(rev)

    def modificaClient(self):
        try:
            # in functie se vor citi date noi de la tastatura pentru un client identificat printr-un id
            idClient = input("Dati id-ul clientului de modificat: ")
            numeClientNou = input("Dati noul nume al clientului: ")
            cnpClientNou = input("Dati noul cnp al clientului: ")
            lista_inchirieriNoua = []
            lista_len = input("Dati lungimea listei inchirierilor: ")
            i = 0
            while i < int(lista_len):
                f_id = input("Dati id-ul filmului pe care vreti sa il puneti in lista de inchirieri: ")
                lista_inchirieriNoua.append(f_id)
                i += 1
            validation_updateClient = Validation_updateClient(idClient, numeClientNou, cnpClientNou)
            validation_updateClient.test_idClient()
            validation_updateClient.test_numeClient()
            validation_updateClient.test_cnpClient()
            self.__clientService.modifica(idClient, numeClientNou, cnpClientNou, lista_inchirieriNoua)
        except KeyError as e:
            print(e)
        except IdErrorEmpty as iee:
            print(iee)
        except IdError as ie:
            print(ie)
        except IdErrorNumeric as ien:
            print(ien)
        except NameErrorEmpty as aee:
            print(aee)
        except NameErrorAlpha as aea:
            print(aea)
        except CnpErrorEmpty as cee:
            print(cee)
        except CnpErrorNegative as cen:
            print(cen)
        except CnpErrorLength as cel:
            print(cel)
        except CnpErrorS as ces:
            print(ces)
        except CnpErrorNumeric as cenu:
            print(cenu)
        except CnpErrorInvalid as cei:
            print(cei)

    def stergeFilm(self):
        try:
            # in functie se citeste id-ul filumului care ulterior va fi sters
            idFilm = input("Dati id-ul filmului pe care vreti sa il stergeti: ")
            self.__filmService.sterge(idFilm)
        except KeyError as e:
            print(e)

    def stergeClient(self):
        try:
            # in functie se citeste id-ul clientului care ulterior va fi sters
            idClient = input("Dati id-ul clientului pe care vreti sa il stergeti: ")
            self.__clientService.sterge(idClient)
        except KeyError as e:
            print(e)

    def findByIdFilm(self):
        try:
            # in functie se citeste id-ul filmului pentru a fi cautat
            idfilm = input("Dati id-ul filmului pe care vreti sa il gasiti: ")
            f = self.__filmService.findById(idfilm)
            if f is None:
                raise KeyError("there is no movie with the given id!")
            print(f)
        except KeyError as e:
            print(e)

    def findByIdClient(self):
        try:
            # in functie se citeste id-ul clientului prin care acesta va fi cautat
            idClient = input("Dati id-ul clientului pe care vreti sa il gasiti: ")
            c = self.__clientService.findById(idClient)
            if c is None:
                raise KeyError("here is no client with the given id!")
            print(c)
        except KeyError as e:
            print(e)

    def inchiriereFilm(self):
        try:
            # in functie se citeste id-ul filmului pe care utilizatorul doreste sa il inchirieze
            # iar mai apoi id-ul clientului caruia sa i se atribuie filmul inchiriat
            self.printAllMovies(self.__filmService.getAll())
            idFilmInchiriat = input("Dati id-ul filmului pe care vreti sa il inchiriati: ")
            self.__filmService.inchiriere_film_dupa_id(idFilmInchiriat)
            self.printAllClients(self.__clientService.getAll())
            idClientInchiriat = input("Dati id-ul clientului care va inchiria filmul: ")
            self.__clientService.inchiriere_film(idFilmInchiriat, idClientInchiriat)
        except KeyError as e:
            print(e)

    def inchiriere_film_sortare(self):
        try:
            # functia primeste o lista sortata descrescator dupa numarul de inchirieri
            # si apoi transmite lista primita catre o functie care o va afisa
            self.printAllMovies(self.__filmService.inchiriere_film_sortare())
        except KeyError as e:
            print(e)

    def sortare_dupa_nume_si_numar(self):
        try:
            # functia primeste o lista sortata crescator dupa nume si numarul de inchirieri
            # si apoi transmite lista primita catre o functie care o va afisa
            self.print_sortare_dupa_nume_si_numar(self.__clientService.sortare_dupa_nume_si_numar())
        except KeyError as e:
            print(e)

    def first_thirty_percent(self):
        try:
            # functia primeste o lista cu primii 30% clienti sortata crescator dupa numarul de inchirieri
            # si apoi transmite lista primita catre o functie care o va afisa
            self.print_sortare_dupa_nume_si_numar(self.__clientService.thirty_percent())
        except KeyError as e:
            print(e)

    def print_sortare_dupa_nume_si_numar(self, sortedList):
        # functia afiseaza o lista primita
        for o in sortedList:
            print(f"nume: {o.get_nume()}   FilmeInchiriate: {o.get_lista_inchirieri()}")

    def printAllMovies(self, listOfMovies):
        # functia afiseaza o lista primita
        for i in listOfMovies:
            print(i)

    def printAllClients(self, listOfClients):
        # functia afiseaza o lista primita
        for j in listOfClients:
            print(j)

    def printMenu(self):
        #meniul aplicatiei
        print("1. Adauga film")
        print("2. Modifica film")
        print("3. Sterge film")
        print("4. Gaseste film dupa id")
        print("5. Adauga client")
        print("6. Modifica client")
        print("7. Sterge client")
        print("8. Cauta client dupa id")
        print("9. Inchiriaza un film")
        print("10. Clienti cu filme inchiriate ordonate dupa nume sau dupa numarul de filme inchiriate")
        print("11. Cele mai inchiriate filme")
        print("12. Primii 30% clienti cu cele mai multe filme")
        print("f. Afiseaza toate filmele")
        print("c. Afiseaza toti clientii")
        print("x. Iesire")

    def Menu(self):
        #functia permite introducerea de la tastatura a unei optiuni din meniul dat
        while True:
            self.printMenu()
            op = input("Alege o optiune: ")
            if op == "1":
                self.adaugaFilm()
            elif op == "2":
                self.modificaFilm()
            elif op == "3":
                self.stergeFilm()
            elif op == "4":
                self.findByIdFilm()
            elif op == "5":
                self.adaugaClient()
            elif op == "6":
                self.modificaClient()
            elif op == "7":
                self.stergeClient()
            elif op == "8":
                self.findByIdClient()
            elif op == "9":
                self.inchiriereFilm()
            elif op == "10":
                self.sortare_dupa_nume_si_numar()
            elif op == "11":
                self.inchiriere_film_sortare()
            elif op == "12":
                self.first_thirty_percent()
            elif op == "f":
                self.printAllMovies(self.__filmService.getAll())
            elif op == "c":
                self.printAllClients(self.__clientService.getAll())
            elif op == "x":
                break
            else:
                print("Optiune invalida, reincercati!")

