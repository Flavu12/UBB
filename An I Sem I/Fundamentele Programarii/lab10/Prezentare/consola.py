from erori.repo_error import RepoError
from erori.validation_error import ValidError


class ui:

    def __init__(self, service_clienti, service_filme, service_inchirieri):
        self.__service_clienti = service_clienti
        self.__service_filme = service_filme
        self.__service_inchirieri = service_inchirieri
        self.__comenzi = {
            "adauga_client": self.__ui_adauga_client,
            "print_clienti": self.__ui_print_clienti,
            "sterge_client": self.__ui_sterge_client,
            "adauga_film": self.__ui_adauga_film,
            "print_filme": self.__ui_print_filme,
            "sterge_film": self.__ui_sterge_film,
            "random_filme": self.__ui_random_filme,
            "random_clienti": self.__ui_random_clienti,
            "cauta_film": self.__ui_cauta_film,
            "cauta_client": self.__ui_cauta_client,
            "adauga_inchiriere": self.__ui_adauga_inchiriere,
            "print_inchirieri": self.__ui_print_inchirieri,
            "sterge_film_si_inchirieri": self.__ui_sterge_inchiriere_film,
            "sterge_client_si_inchirieri": self.__ui_sterge_inchiriere_client,
            "returnare": self.__ui_returnare
        }

    def __ui_random_clienti(self):
        if len(self.__params) != 1:
            print('Invalid nr of params')
            return
        nr = int(self.__params[0])
        self.__service_clienti.clienti_random(nr)

    def __ui_adauga_film(self):
        if len(self.__params) != 4:
            print("numar parametri invalid!")
            return
        id_film = int(self.__params[0])
        titlu_film = self.__params[1]
        descriere_film = self.__params[2]
        gen_film = self.__params[3]
        self.__service_filme.adauga_film_service(id_film, titlu_film, descriere_film, gen_film)
        print("film adaugat cu succes!")

    def __ui_sterge_film(self):
        if len(self.__params) != 2:
            print("numar parametri invalid!")
            return
        id_film = int(self.__params[0])
        self.__service_filme.sterge_film(id_film)
        print(f"filmul cu id-ul {id_film}  a fost sters!")

    def __ui_print_filme(self):
        if len(self.__params) != 0:
            print("numar parametri invalid!")
            return
        filme = self.__service_filme.get_all_filme_service()
        if len(filme) == 0:
            print("nu exista filme in aplicatie!")
            return
        for film in filme:
            print("id film:", film.get_id_film())
            print("titlu film:", film.get_titlu_film())
            print("descriere film:", film.get_descriere_film())
            print("gen film:", film.get_gen_film(), "\n")

    def __ui_random_filme(self):
        if len(self.__params) != 1:
            print('Invalid nr of params')
            return
        nr = int(self.__params[0])
        self.__service_filme.filme_random(nr)

    def __ui_sterge_client(self):
        if len(self.__params) != 1:
            print("numar parametri invalid!")
            return
        id_client = int(self.__params[0])
        self.__service_clienti.sterge_client_service(id_client)

    def __ui_print_clienti(self):
        if len(self.__params) != 0:
            print("numar parametri invalid!")
            return
        clienti = self.__service_clienti.get_all_clienti_service()
        if len(clienti) == 0:
            print("nu exista clienti in aplicatie!")
            return
        for client in clienti:
            print("id client:", client.get_id_client())
            print("nume client:", client.get_nume_client())
            print("cnp client:", client.get_cnp(), "\n")

    def __ui_adauga_client(self):
        if len(self.__params) != 3:
            print("numar parametri invalid!")
            return
        id_client = int(self.__params[0])
        nume = self.__params[1]
        cnp = int(self.__params[2])
        self.__service_clienti.adauga_client_service(id_client, nume, cnp)
        print("client adaugat cu succes!")

    def __ui_cauta_film(self):
        id_film = int(self.__params[0])
        film = self.__service_filme.cauta_film_service(id_film)
        print(film)

    def __ui_cauta_client(self):
        id_client = int(self.__params[0])
        client = self.__service_clienti.cauta_clienti_service(id_client)
        print(client)

    def __ui_adauga_inchiriere(self):
        if len(self.__params) != 3:
            print("numar parametri invalid!")
            return
        id_inchiriere = int(self.__params[0])
        id_film = int(self.__params[1])
        id_client = int(self.__params[2])
        self.__service_inchirieri.adauga_inchiriere_service(id_inchiriere, id_film, id_client)
        print("inchiriere adaugata cu succes!")

    def __ui_print_inchirieri(self):
        if len(self.__params) != 0:
            print("numar parametri invalid!")
            return
        inchirieri = self.__service_inchirieri.get_all_inchirieri_service()
        if len(inchirieri) == 0:
            print("nu exista inchirieri in aplicatie!")
            return
        for inchiriere in inchirieri:
            print("id inchiriere:", inchiriere.get_id_inchiriere())
            print("id film:", inchiriere.get_id_film())
            print("id client:", inchiriere.get_id_client(), "\n")

    def __ui_sterge_inchiriere_film(self):
        if len(self.__params) != 1:
            print("numar parametri invalid!")
            return
        id_film = int(self.__params[0])
        self.__service_inchirieri.sterge_film_si_inchirieri(id_film)

    def __ui_sterge_inchiriere_client(self):
        if len(self.__params) != 1:
            print("numar parametri invalid!")
            return
        id_client = int(self.__params[0])
        self.__service_inchirieri.sterge_client_si_inchirieri(id_client)

    def __ui_returnare(self):
        if len(self.__params) != 1:
            print("numar parametri invalid!")
            return
        id_inchiriere = int(self.__params[0])
        self.__service_inchirieri.sterge_inchiriere_service(id_inchiriere)

    def run(self):
        print("Lista de comenzi acceptate:\n")
        print(" adauga_client [id_client] [nume] [cnp]")
        print(" print_clienti")
        print(" sterge_client [id_client]")
        print(" adauga_film [id_film] [titlu] [descriere] [gen]")
        print(" print_filme")
        print(" sterge_film [id_film]")
        print(" random_filme [numar]")
        print(" random_clienti [numar]")
        print(" cauta_film [id_film]")
        print(" cauta_client [id_client]")
        print(" adauga_inchiriere [id_inchiriere] [id_film] [id_client]")
        print(" print_inchirieri")
        print(" sterge_film_si_inchirieri [id_film]")
        print(" sterge_client_si_inchirieri [id_client]")
        print(" returnare")
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
