from erori.repo_error import RepoError


class RepoInchirieri:

    def __init__(self):
        self.__inchirieri = {}

    def adauga_inchiriere(self, inchiriere):
        # adauga o inchiriere intr-un dictionar de inchirieri
        if inchiriere.get_id_inchiriere() in self.__inchirieri:
            raise RepoError("Inchiriere existenta!")
        self.__inchirieri[inchiriere.get_id_inchiriere()] = inchiriere

    def sterge_inchiriere_dupa_id(self, id_inchiriere):
        # sterge o inchiriere in functie de id-ul acesteia id_inchiriere din dictionarul de inchirieri
        if self.cauta_inchiriere_dupa_id(id_inchiriere) is None:
            raise RepoError("inchiriere Inexistenta")
        self.__inchirieri.pop(id_inchiriere)

    def cauta_inchiriere_dupa_id(self, id_inchiriere):
        # cauta o inchiriere in functie de id-ul acesteia id_inchiriere din dictionarul de inchirieri
        if id_inchiriere not in self.__inchirieri:
            raise RepoError("inchiriere inexistenta!")
        return self.__inchirieri[id_inchiriere]

    def modifica_inchiriere(self, inchiriere):
        # modifica o inchiriere din dictionarul de inchirieri
        if inchiriere.get_id_inchiriere() not in self.__inchirieri:
            raise RepoError("inchiriere inexistenta!")
        self.__inchirieri[inchiriere.get_id_inchiriere()] = inchiriere

    def get_all(self):
        # retuneaza o lista de inchirieri adaugate in dictionarul de inchirieri
        inchirieri = []
        for id_inchiriere in self.__inchirieri:
            inchirieri.append(self.__inchirieri[id_inchiriere])
        return inchirieri

    def __len__(self):
        # returneaza lungimea dictionarului de inchirieri
        return len(self.__inchirieri)