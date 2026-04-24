def creeaza_numar_complex(parte_reala, parte_imaginara):
    '''
    :param parte_reala: float
    :param parte_imaginara: float
    :return: dictionar de tipul numar complex
    '''
    return {"parte_reala": parte_reala,
            "parte_imaginara": parte_imaginara
            }


def get_parte_reala(numar_complex):
    return numar_complex["parte_reala"]


def get_parte_imaginara(numar_complex):
    return numar_complex["parte_imaginara"]


def set_parte_reala(numar_complex, parte_reala):
    numar_complex["parte_reala"] = parte_reala


def set_parte_imaginara(numar_complex, parte_imaginara):
    numar_complex["parte_imaginara"] = parte_imaginara

