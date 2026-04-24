# clasele vor transmite erori pentru validarea datelor de intrare
class IdError(Exception):
    def __init__(self, id, message = "id cannot be negative!"):
        self.id = id
        self.message = message
        super().__init__(self.message)

class IdErrorEmpty(Exception):
    def __init__(self, id, message = "id cannot be empty!"):
        self.id = id
        self.message = message
        super().__init__(self.message)

class IdErrorNumeric(Exception):
    def __init__(self, id, message = "id must be numeric!"):
        self.id = id
        self.message = message
        super().__init__(self.message)

class TitleErrorEmpty(Exception):
    def __init__(self, titlu, message = "title cannot be empty!"):
        self.titlu = titlu
        self.message = message
        super().__init__(self.message)

class DescriptionErrorEmpty(Exception):
    def __init__(self, descriere, message = "description cannot be empty!"):
        self.descriere = descriere
        self.message = message
        super().__init__(self.message)

class GenErrorEmpty(Exception):
    def __init__(self, gen, message = "gen cannot be empty!"):
        self.gen = gen
        self.message = message
        super().__init__(self.message)

class GenErrorAlpha(Exception):
    def __init__(self, author, message = "gen must contain only alphabetical letters!"):
        self.author = author
        self.message = message
        super().__init__(self.message)

class NameErrorEmpty(Exception):
    def __init__(self, nume, message = "name cannot be empty!"):
        self.nume = nume
        self.message = message
        super().__init__(self.message)

class NameErrorAlpha(Exception):
    def __init__(self, nume, message = "name must contain only alphabetical letters!"):
        self.nume = nume
        self.message = message
        super().__init__(self.message)


class CnpErrorEmpty(Exception):
    def __init__(self, cnp, message = "cnp cannot be empty!"):
        self.cnp = cnp
        self.message = message
        super().__init__(self.message)

class CnpErrorNegative(Exception):
    def __init__(self, cnp, message = "cnp cannot be negative!"):
        self.cnp = cnp
        self.message = message
        super().__init__(self.message)

class CnpErrorLength(Exception):
    def __init__(self, cnp, message = "cnp must contain 13 digits!"):
        self.cnp = cnp
        self.message = message
        super().__init__(self.message)

class CnpErrorS(Exception):
    def __init__(self, cnp, message = "component S must be between 1 and 8!"):
        self.cnp = cnp
        self.message = message
        super().__init__(self.message)

class CnpErrorNumeric(Exception):
    def __init__(self, cnp, message = "cnp must contain only positive digits!"):
        self.cnp = cnp
        self.message = message
        super().__init__(self.message)


class CnpErrorInvalid(Exception):
    def __init__(self, cnp, message = "invalid cnp!"):
        self.cnp = cnp
        self.message = message
        super().__init__(self.message)

class InchiriereErrorValue(Exception):
    def __init__(self, inchiriere, message = "rent value cannot be negative!"):
        self.inchiriere = inchiriere
        self.message = message
        super().__init__(self.message)