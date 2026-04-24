class FilmRepository:
    def __init__(self):
        # se va crea un dictionar pentru a stoca datele filmului
        self.__all_movies_dict ={}

    def getAll(self):
        #returneaza o lista cu toate filmele
        return list(self.__all_movies_dict.values())

    def getById(self, idFilm):
        # in cazul in care exista un film dupa un id returneaza filmul altfel returneaza None
        if idFilm in self.__all_movies_dict:
            return self.__all_movies_dict[idFilm]
        return None

    def adaugaFilm(self, film):
        #adauga un nou film in dictionar daca acesta nu se afla deja in dictionare, in caz contrar, returnaza None
        if self.getById(film.get_id()) is not None:
            raise KeyError("there is already a movie with the given id!")
        self.__all_movies_dict[film.get_id()] = film

    def modifica(self, filmNou):
        #face update unui film daca se afla in dictionar, altfel returneaza un Keyerror
        if self.getById(filmNou.get_id()) is None:
            raise KeyError("there is no movie with the given id!")
        self.__all_movies_dict[filmNou.get_id()] = filmNou

    def sterge(self, idFilm):
        #sterge un film dupa un id daca se afla in dictionar, altfel returneaza un KeyError
        if self.getById(idFilm) is None:
            raise KeyError("there is no movie with the given id!")
        self.__all_movies_dict.pop(idFilm)