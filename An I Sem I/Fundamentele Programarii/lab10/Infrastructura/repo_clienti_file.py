from Domeniu.Client import Client
from Infrastructura.repo_clienti import RepoClienti



class ClientFileRepository(RepoClienti):
    def __init__(self, file_name):
        super().__init__()
        self.__file_name = file_name
        self.__load_data()

    def __load_data(self):
        with open(self.__file_name) as f:
            for line in f:
                lista_clienti = line.split(",")
                if lista_clienti[2][len(lista_clienti[2])-1] == '\n':
                    lista_clienti[2] = lista_clienti[2][:-1]
                client = Client(lista_clienti[0], lista_clienti[1], lista_clienti[2], [])

        f.close()

    def adaugaClient(self, client):
        #with open(self.__file_name, "a") as f:
            #f.write("\n" + client.get_id() + "," + client.get_name() + "," + client.get_cnp() + "," + str(client.get_list_rent()))
        super().adauga_client(client)
        self.write_in_file()

    def modifica(self, clientNou):
        super().modifica_client(clientNou)
        self.write_in_file()

    def sterge(self, idClient):
        super().sterge_client_dupa_id(idClient)
        self.write_in_file()

    def write_in_file(self):
        f = open(self.__file_name, "w")
        lista_clienti = super().get_all()
        for client in lista_clienti:
            id = client.get_id_client()
            nume = client.get_nume()
            cnp = client.get_cnp()
            lista_inchirieri = client.get_lista_inchirieri()
            line = id + "," + nume + "," + cnp + "," + str(lista_inchirieri) + "\n"
            f.write(line)
        f.close()