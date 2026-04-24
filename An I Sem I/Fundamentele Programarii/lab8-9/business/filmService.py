from domeniu.entitati import Film
from Infrastructura.filmRepository import FilmRepository


class FilmService:
    def __init__(self, filmRepository: FilmRepository):
        # in FilmService se va crea un nou FilmRepository
        self.__filmRepository = filmRepository

    def getAll(self):
        # returneaza o lista cu toate filmele
        return self.__filmRepository.getAll()

    def adaugaFilm(self, id, titlu, descriere, gen, nrf):
        # adauga un nou film in dictionar daca aceasta nu se afla deja in dictionar, in caz contar returneaza un KeyError
        film = Film(id, titlu, descriere, gen, nrf)
        self.__filmRepository.adaugaFilm(film)

    def modifica(self, id, titluNou, descriereNoua, genNou, nrfNou):
        # face update unui film daca se afla in dictionar, altfel returneaza un KeyError
        film = Film(id, titluNou, descriereNoua, genNou, nrfNou)
        self.__filmRepository.modifica(film)

    def sterge(self, id):
        # sterge un film dupa un id daca se afla in dictionar, altfel returneaza un KeyError
        self.__filmRepository.sterge(id)

    def findById(self, id):
        # in cazul in care exista un film dupa un id o sa returneze filmul altfel returneaza None
        return self.__filmRepository.getById(id)

    def inchiriere_film_dupa_id(self, idFilm):
        # verifica daca exista un film in dictionar dupa id-ul dat si incrementeaza cu 1 numarul de filme inchiriate
        # in caz contrar returneaza un KeyError
        if self.findById(idFilm) is None:
            raise KeyError("there is no movie with the given id!")
        film = self.__filmRepository.getById(idFilm)
        numar_carti_inchiriate = film.get_nrf()
        numar_carti_inchiriate += 1
        self.modifica(idFilm, film.get_titlu(), film.get_descriere(), film.get_gen(), numar_carti_inchiriate)

    def inchiriere_film_sortare(self):
        # returneaza o lista de filme sortata descrescator dupa numarul de filme inchiriate
        lista_filme = self.__filmRepository.getAll()
        aux = Film("0", "0", "0", "0", "0")
        for i in range(0, len(lista_filme) - 1):
            for j in range(i + 1, len(lista_filme)):
                if lista_filme[i].get_nrf() < lista_filme[j].get_nrf():
                    aux.set_id(lista_filme[i].get_id())
                    aux.set_titlu(lista_filme[i].get_titlu())
                    aux.set_descriere(lista_filme[i].get_descriere())
                    aux.set_gen(lista_filme[i].get_gen())
                    aux.set_nrf(lista_filme[i].get_nrf())

                    lista_filme[i].set_id(lista_filme[j].get_id())
                    lista_filme[i].set_titlu(lista_filme[j].get_titlu())
                    lista_filme[i].set_descriere(lista_filme[j].get_descriere())
                    lista_filme[i].set_gen(lista_filme[j].get_gen())
                    lista_filme[i].set_nrf(lista_filme[j].get_nrf())

                    lista_filme[j].set_id(aux.get_id())
                    lista_filme[j].set_titlu(aux.get_titlu())
                    lista_filme[j].set_descriere(aux.get_descriere())
                    lista_filme[j].set_gen(aux.get_gen())
                    lista_filme[j].set_nrf(aux.get_nrf())

        return lista_filme