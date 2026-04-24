def menu():             # Se defineste functia meniu care contine toate cerintele
    print("[1]  Citeste o lista de numere complexe")
    print("[2]  Afisare lista de numere complexe")
    print("[3]  Adaugă număr complex la sfârșitul listei")
    print("[4]  Inserare număr complex pe o poziție dată")
    print("[5]  Sterge element de pe o pozitie data")
    print("[6]  Sterge elementele de pe un interval de pozitii")
    print("[7]  Înlocuiește toate aparițiile unui număr complex cu un alt număr complex")
    print("[8]  Tipărește partea imaginara pentru numerele din listă. Se dă intervalul de poziții (sub secvența)")
    print("[9]  Tipărește toate numerele complexe care au modulul mai mic decât 10")
    print("[10] Tipărește toate numerele complexe care au modulul egal cu 10")
    print("[11] Iesire din program")

##########################################################################
class Complex_numbers:          # Complex_numbers este o clasa creata pentru elemente de tip numar complex
    def __init__(self, real, img):  # numar de tipul x + yj
        self.x = real           # fiecare element de tip numar complex va avea o parte reala
        self.y = img            # si o parte imaginara

    def get_complex_number(self):  # metoda a clasei de afisare a numarului complex
        if self.y < 0:
            print("{}{}j".format(self.x, self.y), end=' ')
        else:
            print("{}+{}j".format(self.x, self.y), end=' ')

    def __add__(self, other):
        a = self.x + other.x  # adunarea partiilor reale
        b = self.y + other.y  # adunarea partiilor imaginare
        return a, b


##########################################################################

def Creeare_lista_numere_complexe():
    lista = []
    n = int(input("Introduceti numarul de elemente: "))
    for index in range(0, n):           # Se parcurge un for pana la n pentru a citi n numere complexe
        print("Sa se adauge elementul ", index + 1, " de forma a + bj.")
        a = int(input("a = "))  # citirea partii reale a elementului
        b = int(input("b = "))  # citirea partii imaginare a elementului
        element = Complex_numbers(a, b)  # creeare element
        lista.append(element)  # adaugare element in lista
    return lista


def Afisare_lista_numere_complexe(lista):
    for index in range(0, len(lista)):
        lista[index].get_complex_number()          # se foloseste metoda get_complex_number() din clasa Complex_numbers
        if index < len(lista) - 1:                 # pentru a afisa un numerele complexe
            print(",", end=' ')


def Inserare_numar_complex_la_sfarsitul_listei(lista):
    print("Sa se creeze elementul de forma a+bj care se va insera la capatul listei")
    a = int(input("a = "))  # citirea partii reale a elementului
    b = int(input("b = "))  # citirea partii imaginare a elementului
    element = Complex_numbers(a, b)  # creeare element
    lista.append(element) # inserare elenent in lista cu ajutorul functiei append care lipeste numarul la capatul listei


def Inserare_numar_complex_pe_o_pozitie_data(lista):
    print("Sa se creeze elementul de forma a+bj care se va insera pe o pozitie data")
    a = int(input("a = "))  # citirea partii reale a elementului
    b = int(input("b = "))  # citirea partii imaginare a elementului
    element = Complex_numbers(a, b)  # creeare element
    poz = int(input("Precizati pozitia pe care sa se insereze elementul nou: "))
    lista.insert(poz - 1, element)  # inserare elenent in lista cu ajutorul functiei insert


def Sterge_element_de_pe_o_pozitie_data(lista):
    poz = int(input("Precizati pozitia de pe care sa se stearga un element: "))
    lista.pop(poz - 1)              # Folosirea functiei pop pentru a sterge un element din lista


def Sterge_elementele_de_pe_un_interval_de_pozitii(lista):
    poz1 = int(input("Precizati pozitia inceputului intervalului: "))
    poz2 = int(input("Precizati pozitia sfarsitului intervalului: "))
    print("Se vor sterge elementele din lista de pe pozitiile din intervalul [", poz1, ",", poz2, "] ")
    lista1 = lista[0: poz1 - 1: 1]  # o lista temporara cu elemente pana la inceputul intervalului
    lista2 = lista[poz2: len(lista): 1]  # o lista temporara cu elemente de la sfarsitul intervalului
    lista = lista1 + lista2  # concatenam cele doua liste
    return lista  # returnam lista


def Inlocuieste_toate_aparitiile_unui_numar_complex_cu_un_alt_numar_complex(lista):
    print("Sa se creeze elementul de forma a+bj care va inlocui in lista un element dat")
    a_nou = int(input("a = "))  # citirea partii reale a elementului
    b_nou = int(input("b = "))  # citirea partii imaginare a elementului
    element_nou = Complex_numbers(a_nou, b_nou)  # creeare element

    print("Sa se precizeze elementul de forma a+bj care va fi inlocuit in lista de elementul creeat aterior")
    a_lista = int(input("a = "))  # citirea partii reale a elementului
    b_lista = int(input("b = "))  # citirea partii imaginare a elementului

    for index in range(0, len(lista)):  # parcurgem lista pentru a gasi elemente egale cu cel de-al doi-le numar citit
        if a_lista == lista[index].x and b_lista == lista[index].y:  # daca gasim elemente egale cu numarul care trebie
            lista[index] = element_nou                               # inlocuit in lista, le inlocuim


def Tipareste_partea_imaginara_pentru_numerele_din_lista_din_interval_dat(lista):
    poz1 = int(input("Precizati pozitia inceputului intervalului: "))
    poz2 = int(input("Precizati pozitia sfarsitului intervalului: "))
    print("Se av tipari partea imaginara a elementelor din lista de pe pozitiile din intervalul [", poz1, ",", poz2, "] ")
    for index in range(poz1 - 1, poz2):         # Se parcurge intervalul citit de la tastatura
        print(lista[index].y, end=' ')          # Ne folosim de clasa Complex_numbers pentru a printa in User Interface
        if index < poz2 - 1:                    # doar partea imaginara a elementelor din interval
            print(',', end = ' ')


def Tipareste_toate_numerele_complexe_care_au_modulul_mai_mic_decat_10(lista):
    for index in range(0, len(lista)):      # se parcurge lista
        if abs(lista[index].x**2 + lista[index].y**2) < 10:    # se calculeaza modulul fiecarui numar complex, verificand
            lista[index].get_complex_number()                  # daca este acesta este < 10
            print("; ", end = ' ')                              # se afiseaza numarul complex


def Tipareste_toate_numerele_complexe_care_au_modulul_egal_cu_10(lista):
    for index in range(0, len(lista)):      # se parcurge lista
        if abs(lista[index].x**2 + lista[index].y**2) == 10:   # se calculeaza modulul fiecarui numar complex, verificand
            lista[index].get_complex_number()                  # daca acesta este egal cu 10
            print("; ", end = ' ')                              # se afiseaza numarul complex

def run():          #  Functia run() este rulata ca functie principala
    menu()
    print()
    option = int(input("Introduceti o optiune: "))
    lista = []
    while option != 11:
        if option == 1:
            # ruleaza optiunea 1
            print("optiunea 1 a fost apelata")
            lista = Creeare_lista_numere_complexe()
        elif option == 2:
            # ruleaza optiunea 2
            print("optiunea 2 a fost apelata")
            Afisare_lista_numere_complexe(lista)
            print('\n')
        elif option == 3:
            # ruleaza optiunea 3
            print("optiunea 3 a fost apelata")
            Inserare_numar_complex_la_sfarsitul_listei(lista)
            print('\n')
        elif option == 4:
            print("optiunea 4 a fost apelata")
            Inserare_numar_complex_pe_o_pozitie_data(lista)
            print('\n')
        elif option == 5:
            print("optiunea 5 a fost apelata")
            Sterge_element_de_pe_o_pozitie_data(lista)
            print('\n')
        elif option == 6:
            print("optiunea 6 a fost apelata")
            lista = Sterge_elementele_de_pe_un_interval_de_pozitii(lista)
            print('\n')
        elif option == 7:
            print("optiunea 7 a fost apelata")
            Inlocuieste_toate_aparitiile_unui_numar_complex_cu_un_alt_numar_complex(lista)
            print('\n')
        elif option == 8:
            print("optiunea 8 a fost apelata")
            Tipareste_partea_imaginara_pentru_numerele_din_lista_din_interval_dat(lista)
            print('\n')
        elif option == 9:
            print("optiunea 9 a fost apelata")
            Tipareste_toate_numerele_complexe_care_au_modulul_mai_mic_decat_10(lista)
            print('\n')
        elif option == 10:
            print("optiunea 10 a fost apelata")
            Tipareste_toate_numerele_complexe_care_au_modulul_egal_cu_10(lista)
            print('\n')
        else:
            print("Optiune invalida")

        menu()
        print()
        option = int(input("Introduceti o optiune: "))


if __name__ == "__main__":
    run()
