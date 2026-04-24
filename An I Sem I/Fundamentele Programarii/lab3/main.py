
def prim(a, b):
    # Verifica daca diferenta a doua numere este un numar prim prim sau nu
    # Date de intrare: a , b-numare intregi
    # Date de iesire: True daca diferenta este un numar prim si False in caz contrar
    dif = abs(a - b)
    if dif < 2:
        return 0
    if dif == 2:
        return 1
    if dif % 2 == 0:
        return 0
    for d in range(3, dif):
         if dif % d == 0:
             return 0
    return 1


def prop7(x):
    # Gaseste cea mai lunga secventa cu proprietatea ca orice doua elemente difera printr-un numar prim
    # Date de intrare: v- lista de numere naturale
    # Date de iesire: Secventa cea mai lunga care respecta proprietatea
    isol = 0
    jsol = 1
    i = 0
    m = len(x)
    while i < m:
        j = i + 1
        while j < m and prim(x[j - 1], x[j]) == 1:
            j = j + 1
        if j - i > jsol - isol:
            isol = i
            jsol = j
        i = j
    if isol == 0 and jsol == 1:
        return "Nu exista secventa cautata"
    return x[isol:jsol]


def prop5(x):
    isol = 0
    jsol = 1
    i = 0
    m = len(x)
    while i < m:
        j = i + 1
        while j < m and x[j - 1] == x[j]:
            j = j + 1
        if j - i > jsol - isol:
            isol = i
            jsol = j
        i = j
    if isol == 0 and jsol == 1:
        return "Nu exista secventa cautata"
    return x[isol:jsol]


def prop10(A):
    """
    returneaza secventa de lungime maxima in care diferentele (x[j+1] - x[j]) si (x[j+2] - x[j+1]) au semne contrare
    """
    k1 = 0; k2 = 0;K_1 = 0;K_2 = 0
    n = len(A)
    maxx = 0
    for i in range(n - 2):
        a = A[i + 1] - A[i]
        b = A[i + 2] - A[i + 1]
        if (a < 0 and b >= 0):
            k2 = i + 2
            if (k2 - k1 > maxx):
                maxx = k2 - k1
                K_1 = k1  # K_1 si K_2 pozitiile secventei maxime
                K_2 = k2

        elif (a >= 0 and b < 0):
            k2 = i + 2
            if (k2 - k1 > maxx):
                maxx = k2 - k1
                K_1 = k1  # K_1 si K_2 pozitiile secventei maxime
                K_2 = k2
        else:
            k1 = i + 1  #schimbam pozitia primului termen din secventa
    if (maxx > 0):  # verificam daca exista secventa
        return (A[K_1:K_2+1])
    else:
        return (A[0])

def printMenu():
    # Afiseaza meniul principal al aplicatiei
    print("1.Citirea unei liste de numere intregi")
    print("2.Secventa de lungime maxima care respecta proprietatea 7")
    print("3.Secventa de lungime maxima care respecta proprietatea 10")
    print("4.Secventa de lungime maxima care respecta proprietatea 5")
    print("5.Iesire din aplicatie")


def getList():
    # Citeste si afiseaza o lista de numere naturale
    m = int(input("Introdu numarul de elemente din lista : "))
    x = []
    print("Introdu elementele listei")
    for i in range(0, m):
        print(i, ".=")
        el = int(input())
        x.append(el)
    return x


def run():
    # Implementeaza interfata utilizatorului
    finish = False
    while not finish:
        printMenu()
        option = int(input("Introdu optiunea : "))
        if option == 1:
            lst = getList()
            n = len(lst)

        elif option == 2:
            print(prop7(lst))

        elif option == 3:
            print(prop10(lst))

        elif option == 4:
            print(prop5(lst))

        elif option == 5:
            print("Goodbye !")
            finish = True
        else:
            print("Ai introdus un numar care nu se afla in meniu")



# Test Functions

def test_prim():
    #Test pentru functia de numar prim
    assert prim(2, 1) == 0
    assert prim(7, 3) == 0
    assert prim(5, 3) == 1
    assert prim(4, 9) == 1
    assert prim(25, 50) == 0
    assert prim(1, 1) == 0


def test_solve7():
    # Test pentru functia prop7
    x = [1, 2, 3, 4, 5]
    assert prop7(x) == "Nu exista secventa cautata"
    x = [2, 4, 6, 8, 9, 11, 12]
    assert prop7(x) == [2, 4, 6, 8]
    x = [2, 5, 8, 13, 14]
    assert prop7(x) == [2, 5, 8, 13]
    x = [1, 1, 1, 1, 1]
    assert prop7(x) == "Nu exista secventa cautata"

def test_prop10():
    x = [1, 3, 2, 7, 8, 12]
    assert prop10(x) == [1, 3, 2, 7]
    x = [1, 1, 1, 1, 1]
    assert prop10(x) == 1
    x = [1, 2, 3, 4, 5]
    assert prop10(x) == 1

def test_prop5():
    x = [1, 2, 2, 2, 3, 4, 5, 5]
    assert prop5(x) == [2, 2, 2]
    x = [1, 1, 2, 2, 3, 3]
    assert prop5(x) == [1, 1]
    x = [1, 2, 3, 4, 5]
    assert prop5(x) == "Nu exista secventa cautata"



test_prim()
test_solve7()
test_prop10()
test_prop5()
run()