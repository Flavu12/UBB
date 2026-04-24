from teste.errors import *


class Validation_addFilm():
    def __init__(self, idFilm, titlu, descriere, gen):
        self.idFilm = idFilm
        self.titlu = titlu
        self.descriere = descriere
        self.gen = gen

    def test_idFilm(self):
        if len(self.idFilm) == 0:
            raise IdErrorEmpty(self.idFilm)
        if self.idFilm[0] == "-":
            raise IdError(self.idFilm)
        if self.idFilm.isnumeric() == False:
            raise IdErrorNumeric(self.idFilm)

    def test_TitluFilm(self):
        if len(self.titlu) == 0:
            raise TitleErrorEmpty(self.titlu)

    def test_descriereFilm(self):
        if len(self.descriere) == 0:
            raise DescriptionErrorEmpty(self.descriere)

    def test_genFilm(self):
        if len(self.gen) == 0:
            raise GenErrorEmpty(self.gen)


class Validation_addClient():
    def __init__(self, idClient, nume, cnp):
        self.idClient = idClient
        self.nume = nume
        self.cnp = cnp

    def test_idClient(self):
        if len(self.idClient) == 0:
            raise IdErrorEmpty(self.idClient)
        if self.idClient[0] == "-":
            raise IdError(self.idClient)
        if self.idClient.isnumeric() == False:
            raise IdErrorNumeric(self.idClient)

    def test_nume(self):
        if len(self.nume) == 0:
            raise NameErrorEmpty(self.nume)
        nume_client = self.nume.split()
        for nume in nume_client:
            if nume.isalpha() == False:
                raise NameErrorAlpha(nume)

    def test_cnpClient(self):
        if len(self.cnp) == 0:
            raise CnpErrorEmpty(self.cnp)
        if self.cnp[0] == "-":
            raise CnpErrorNegative(self.cnp)
        if self.cnp.isnumeric() == False:
            raise CnpErrorNumeric(self.cnp)
        if not len(self.cnp) == 13:
            raise CnpErrorLength(self.cnp)

        #------S------#
        if not (int(self.cnp[0]) >= 1 and int(self.cnp[0]) <= 8):
            raise CnpErrorS(self.cnp)
        # ------S------#

        if self.cnp[11] == "0":
            raise CnpErrorInvalid(self.cnp)

class Validation_updateFilm():
    def __init__(self, idFilm, titluFilm, descriereFilm, genFilm, inchirieri_film):
        self.idFilm = idFilm
        self.titluFilm = titluFilm
        self.descriereFilm = descriereFilm
        self.genFilm = genFilm
        self.inchirieri_film = inchirieri_film

    def test_idFilm(self):
        if len(self.idFilm) == 0:
            raise IdErrorEmpty(self.idFilm)
        if self.idFilm[0] == "-":
            raise IdError(self.idFilm)
        if self.idFilm.isnumeric() == False:
            raise IdErrorNumeric(self.idFilm)

    def test_titluFilm(self):
        if len(self.titluFilm) == 0:
            raise TitleErrorEmpty(self.titluFilm)

    def test_descriereFilm(self):
        if len(self.descriereFilm) == 0:
            raise DescriptionErrorEmpty(self.descriereFilm)

    def test_genFilm(self):
        if len(self.genFilm) == 0:
            raise GenErrorEmpty(self.genFilm)

    def test_inchirieri_film(self):
        if int(self.inchirieri_film) < 0:
            raise InchiriereErrorValue(self.inchirieri_film)

class Validation_updateClient():
    def __init__(self, idClient, numeClient, cnpClient):
        self.idClient = idClient
        self.numeClient = numeClient
        self.cnpClient = cnpClient

    def test_idClient(self):
        if len(self.idClient) == 0:
            raise IdErrorEmpty(self.idClient)
        if self.idClient[0] == "-":
            raise IdError(self.idClient)
        if self.idClient.isnumeric() == False:
            raise IdErrorNumeric(self.idClient)

    def test_numeClient(self):
        if len(self.numeClient) == 0:
            raise NameErrorEmpty(self.numeClient)

        nume_client = self.numeClient.split()
        for nume in nume_client:
            if nume.isalpha() == False:
                raise NameErrorAlpha(nume)


    def test_cnpClient(self):
        if len(self.cnpClient) == 0:
            raise CnpErrorEmpty(self.cnpClient)
        if self.cnpClient[0] == "-":
            raise CnpErrorNegative(self.cnpClient)
        if self.cnpClient.isnumeric() == False:
            raise CnpErrorNumeric(self.cnpClient)
        if not len(self.cnpClient) == 13:
            raise CnpErrorLength(self.cnpClient)

        #------S------#
        if not (int(self.cnpClient[0]) >= 1 and int(self.cnpClient[0]) <= 8):
            raise CnpErrorS(self.cnpClient)
        # ------S------#

        if self.cnpClient[11] == "0":
            raise CnpErrorInvalid(self.cnpClient)