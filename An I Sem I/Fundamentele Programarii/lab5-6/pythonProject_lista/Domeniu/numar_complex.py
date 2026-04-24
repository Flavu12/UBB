def creeaza_numar_complex(parte_reala, parte_imaginara):
    '''
    :param parte_reala: float
    :param parte_imaginara: float
    :return: lista de tipul numar complex
    '''
    return [parte_reala, parte_imaginara]


def get_parte_reala(numar_complex):
    '''
    Returneaza partea reala float al numarului complex numar_complex
    :param numar_complex: numar_complex
    :return: float - partea reala a numarului complex numar_complex
    '''
    return numar_complex[0]


def get_parte_imaginara(numar_complex):
    '''
    Returneaza partea imaginara float al numarului complex numar_complex
    :param numar_complex: numar_complex
    :return: float- partea imaginara a numarului complex numar_complex
    '''
    return numar_complex[1]


def set_parte_reala(numar_complex, parte_reala_noua):
    '''
    Seteaza partea reala float al numarului complex numar_complex la floatul parte_reala_noua
    :param numar_complex: numar_complex
    :param parte_reala_noua: float
    :return: -
    '''
    numar_complex[0] = parte_reala_noua


def set_parte_imaginara(numar_complex, parte_imaginara_noua):
    '''
    Seteaza partea imaginara float al numarului complex numar_complex la floatul parte_imaginara_noua
    :param numar_complex: numar_complex
    :param parte_imaginara_noua: float
    :return: -
    '''
    numar_complex[1] = parte_imaginara_noua

