from error.repo_error import RepoError
from error.validation_error import ValidError

class ui:

    def __init__(self, service_clienti, service_filme):
        self.__service_clienti = service_clienti
        self.__service_filme = service_filme
        self.__comenzi = {
            "adauga_client":self.__ui_adauga_client,
            "print_clienti":self.__ui_print_clienti,
            "sterge_client":self.__ui_sterge_client_si_filme,
            "adauga_film":self.__ui_adauga_film,
            "print_filme":self.__ui_print_filme,
            "sterge_film":self.__ui_sterge_film,
            "inchiriere":self.__ui_add_rent,
        }

    def __ui_add_rent(self):
        if len(self.__params) != 6:
            print("Invalid nr of parameters")
            return
        id_inch = int(self.__params[0])
        id_retur= int(self.__params[1])
        id_client = int(self.__params[2])
        id_film = int(self.__params[3])
        film = self.__service_filme.cauta_film_service(id_film)
        cliemt = self.__service_clienti.cauta_client_service(id_client)
        inch = Inchiere()


    def __ui_sterge_film(self):
        if len(self.__params) != 2:
            print("numar parametri invalid!")
            return
        id_client = int(self.__params[0])
        id_film = int(self.__params[1])
        self.__service_filme.sterge_film(id_client, id_film)
        print(f"filmul cu id-ul {id_film} al clientului cu id-ul {id_client} a fost sters!")

    def __ui_print_filme(self):
        if len(self.__params) != 0:
            print("numar parametri invalid!")
            return
        filme = self.__service_filme.get_all_filme_service()
        if len(filme) == 0:
            print("nu exista filme in aplicatie!")
            return
        for film in filme:
            print("id client:", film.get_id_client_film())
            print("id film:", film.get_id_film())
            print("titlu film:", film.get_titlu_film())
            print("descriere film:", film.get_descriere_film())
            print("gen film:", film.get_gen_film(),"\n")

    def __ui_adauga_film(self):
        if len(self.__params) != 5:
            print("numar parametri invalid!")
            return
        id_client = int(self.__params[0])
        id_film = int(self.__params[1])
        titlu_film = self.__params[2]
        descriere_film = self.__params[3]
        gen_film = self.__params[4]
        self.__service_filme.adauga_film_service(id_client, id_film, titlu_film, descriere_film, gen_film)
        print("film adaugat cu succes!")

    def __ui_sterge_client_si_filme(self):
        if len(self.__params) != 1:
            print("numar parametri invalid!")
            return
        id_client = int(self.__params[0])
        self.__service_filme.sterge_client_si_filmele_lui(id_client)
        print(f"clientul cu id-ul {id_client} si filmele lui sterse cu succes!")

    def __ui_print_clienti(self):
        if len(self.__params) !=0 :
            print("numar parametri invalid!")
            return
        clienti = self.__service_clienti.get_all_clienti_service()
        if len(clienti) == 0:
            print("nu exista clienti in aplicatie!")
            return
        for client in clienti:
            print("Id client:", client.get_id_client())
            print("Nume client:", client.get_nume_client())
            print("Cnp client:", client.get_cnp(), "\n")

    def __ui_adauga_client(self):
        if len(self.__params)!=3:
            print("numar parametri invalid!")
            return
        id_client = int(self.__params[0])
        nume = self.__params[1]
        cnp = int(self.__params[2])
        self.__service_clienti.adauga_client(id_client, nume, cnp)
        print("client adaugat cu succes!")

    def run(self):
        print("Lista de comenzi acceptate:\n")
        print("1. adauga_client [id_client] [nume] [cnp]")
        print("2. print_clienti")
        print("3. sterge_client [id_client]")
        print("4. adauga_film [id_client] [id_film] [titlu] [descriere] [gen]")
        print("5. print_filme")
        print("6. sterge_film [id_client] [id_film]")
        while True:
            comanda = input(">>>")
            comanda = comanda.strip()
            if comanda == "":
                continue
            if comanda == "exit":
                return
            parti = comanda.split()
            nume_comanda = parti[0]
            self.__params = parti[1:]
            if nume_comanda in self.__comenzi:
                try:
                    self.__comenzi[nume_comanda]()
                except ValueError:
                    print("Eroare ui: tip numeric invalid!")
                except ValidError as ve:
                    print(f"ValidError:{ve}")
                except RepoError as re:
                    print(f"Repo Error:{re}")
            else:
                 print("comanda invalida!")




