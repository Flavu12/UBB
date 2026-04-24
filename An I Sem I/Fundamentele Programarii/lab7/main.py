from Business.service_clienti import ServiceClienti
from Business.service_filme import ServiceFilme
from Validare.validator_client import ValidatorClient
from Validare.validator_film import ValidatorFilm
from Infrastructura.repo_clienti import RepoClienti
from Infrastructura.repo_filme import RepoFilme
from Prezentare.consola import ui

if __name__ == '__main__':
    validator_client = ValidatorClient()
    validator_film = ValidatorFilm()
    repo_clienti = RepoClienti()
    repo_filme = RepoFilme()
    service_clienti = ServiceClienti(validator_client, repo_clienti)
    service_filme = ServiceFilme(validator_film, repo_filme, repo_clienti)
    consola = ui(service_clienti, service_filme)
    consola.run()
