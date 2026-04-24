from error.validation_error import ValidError

class ValidatorFilm:

    def __init__(self):
        pass

    def valideaza_film(self, film):
        '''
        valideaza un film. in cazul in care unul dintre parametri este invalid va arunca urmatoarele erori:
        - pentru id client invalid: "Id client invalid!\n"
        - pentru id film invalid: "Id film invalid!\n"
        - pentru titlul filmului invalid: "Titlu film invalid!\n"
        - pentru descriere invalida: "Descriere film invalida!\n"
        - pentru gen invalid: "Gen film invalid!\n"
        :param film: film
        :return: -
        '''
        erori = ""
        if film.get_id_client_film()<=0:
            erori += "Id client invalid!\n"
        if film.get_id_film()<=0:
            erori += "Id film invalid!\n"
        if film.get_titlu_film() == "":
            erori += "Titlu film invalid!\n"
        if film.get_descriere_film() == "":
            erori += "Descriere film invalida!\n"
        if film.get_gen_film() == "":
            erori += "Gen film invalid!\n"
        if len(erori) > 0:
            raise ValidError(erori)

