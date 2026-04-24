from Infrastructura.clientRepository import ClientRepository
from Infrastructura.filmRepository import FilmRepository
from business.clientService import ClientService
from business.filmService import FilmService
from teste.testAll import testAll
from ui.consola import Consola


def main():
    #functia apeleaza toate celelalte functii ale aplicatiei
    testAll()

    filmRepository = FilmRepository()
    clientRepository = ClientRepository()
    filmService = FilmService(filmRepository)
    clientService = ClientService(clientRepository, filmRepository)
    consola = Consola(filmService, clientService)

    consola.Menu()

main()
