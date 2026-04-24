from Business.service_inchirieri import ServiceInchirieri
from Domeniu.Inchiriere import Inchiriere
from Infrastructura.repo_clienti import RepoClienti
from Infrastructura.repo_filme import RepoFilme
from Infrastructura.repo_inchirieri import RepoInchirieri
from erori.repo_error import RepoError


def teste_domeniu():
    inchiriere = Inchiriere("1", "2", "3")

    assert inchiriere.get_id_inchiriere() == "1"
    assert inchiriere.get_id_film() == "2"
    assert inchiriere.get_id_client() == "3"


# Teste Repository


def test_adauga_inchiriere_repo():
    inchiriere_repo = RepoInchirieri()
    inchiriere1 = Inchiriere("1", "2", "3")

    inchiriere_repo.adauga_inchiriere(inchiriere1)

    inchirieri = inchiriere_repo.get_all()
    assert len(inchirieri) == 1
    assert inchirieri[0].get_id_inchiriere() == "1"
    inchiriere2 = Inchiriere("1", "3", "5")
    try:
        inchiriere_repo.adauga_inchiriere(inchiriere2)
        assert False
    except RepoError:
        ...


def test_get_all_repo():
    inchiriere_repo = RepoInchirieri()
    inchiriere1 = Inchiriere("1", "2", "3")
    inchiriere2 = Inchiriere("2", "3", "5")
    inchiriere_repo.adauga_inchiriere(inchiriere1)
    inchiriere_repo.adauga_inchiriere(inchiriere2)

    inchirieri = inchiriere_repo.get_all()
    assert len(inchirieri) == 2
    assert inchirieri[0].get_id_inchiriere() == "1"
    assert inchirieri[1].get_id_inchiriere() == "2"


def test_cauta_dupa_id_repo():
    inchiriere_repo = RepoInchirieri()
    inchiriere1 = Inchiriere("1", "2", "3")
    inchiriere_repo.adauga_inchiriere(inchiriere1)

    inchiriere = inchiriere_repo.cauta_inchiriere_dupa_id("1")

    assert inchiriere.get_id_film() == "2"


def test_modifica_repo():
    inchiriere_repo = RepoInchirieri()
    inchiriere1 = Inchiriere("1", "2", "3")
    inchiriere2 = Inchiriere("1", "3", "5")
    inchiriere3 = Inchiriere("2", "4", "4")

    inchiriere_repo.adauga_inchiriere(inchiriere1)
    inchiriere_repo.modifica_inchiriere(inchiriere2)



    try:
        inchiriere_repo.modifica_inchiriere(inchiriere3)
        assert False
    except RepoError:
        ...


def test_sterge_repo():
    inchiriere_repo = RepoInchirieri()
    inchiriere1 = Inchiriere("1", "2", "3")
    inchiriere_repo.adauga_inchiriere(inchiriere1)

    inchiriere_repo.sterge_inchiriere_dupa_id(inchiriere1.get_id_inchiriere())

    assert len(inchiriere_repo.get_all()) == 0

    try:
        inchiriere_repo.sterge_inchiriere_dupa_id("23423")
        assert False
    except RepoError:
        ...

# Teste Service


def test_adauga_inchiriere_service():
    inchiriere_repo = RepoInchirieri()
    filme_repo = RepoFilme()
    clienti_repo = RepoClienti()
    inchiriere_service = ServiceInchirieri(inchiriere_repo, filme_repo, clienti_repo)
    inchiriere_service.adauga_inchiriere_service("1", "2", "3")

    inchirieri = inchiriere_service.get_all_inchirieri_service()
    assert len(inchirieri) == 1
    assert inchirieri[0].get_id_inchiriere() == "1"

    try:
        inchiriere_service.adauga_inchiriere_service("1", "4", "5")
        assert False
    except RepoError:
        ...

def test_sterge_inchiriere_service():
    inchiriere_repo = RepoInchirieri()
    filme_repo = RepoFilme()
    clienti_repo = RepoClienti()
    inchiriere_service = ServiceInchirieri(inchiriere_repo, filme_repo, clienti_repo)
    inchiriere_service.adauga_inchiriere_service("1", "2", "3")


    inchiriere_service.sterge_inchiriere_service("1")

    inchirieri = inchiriere_service.get_all_inchirieri_service()
    assert len(inchirieri) == 0

    try:
        inchiriere_service.sterge_inchiriere_service("12")
        assert False
    except RepoError:
        ...


def test_get_all_service():
    inchiriere_repo = RepoInchirieri()
    filme_repo = RepoFilme()
    clienti_repo = RepoClienti()
    inchiriere_service = ServiceInchirieri(inchiriere_repo, filme_repo, clienti_repo)
    inchiriere_service.adauga_inchiriere_service("1", "2", "3")
    inchiriere_service.adauga_inchiriere_service("2", "4", "5")

    inchirieri = inchiriere_service.get_all_inchirieri_service()
    assert len(inchirieri) == 2
    assert inchirieri[0].get_id_inchiriere() == "1"
    assert inchirieri[1].get_id_inchiriere() == "2"


def ruleaza_toate_testele_inchirieri():
    teste_domeniu()
    test_adauga_inchiriere_repo()
    test_get_all_repo()
    test_cauta_dupa_id_repo()
    test_modifica_repo()
    test_sterge_repo()
    test_adauga_inchiriere_service()
    test_sterge_inchiriere_service()
    test_get_all_service()
