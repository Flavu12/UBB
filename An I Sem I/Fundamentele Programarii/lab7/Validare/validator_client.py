from error.validation_error import ValidError

class ValidatorClient:

    def __init__(self):
        pass

    def valideaza(self, client):
        '''
        valideaza un client. In cazul in care unul sau mai multi parametri este invalid va arunca urmatoarele erori:
        - pentru id client invalid: "Id invalid!\n"
        - pentru nume client invalid: "Nume invalid!\n"
        - pentru cnp invalid: "Cnp invalid!\n"
        :param client: client
        :return: -
        '''
        erori = ""
        if client.get_id_client() <= 0:
            erori += "Id invalid!\n"
        if client.get_nume_client() == "":
            erori += "Nume invalid!\n"
        if client.get_cnp() <= 999999999999 or client.get_cnp() >= 10000000000000:
            erori += "Cnp invalid!\n"
        if len(erori) > 0:
            raise ValidError(erori)

