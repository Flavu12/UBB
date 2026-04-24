class ValidError(Exception):
    pass

class IdError(Exception):
    def __init__(self, id, message = "id-ul nu poate fi negativ!"):
        self.id = id
        self.message = message
        super().__init__(self.message)

class IdErrorEmpty(Exception):
    def __init__(self, id, message = "id nu poate fi gol!"):
        self.id = id
        self.message = message
        super().__init__(self.message)

class IdErrorNumeric(Exception):
    def __init__(self, id, message = "id trebuie sa fie format din numere!"):
        self.id = id
        self.message = message
        super().__init__(self.message)