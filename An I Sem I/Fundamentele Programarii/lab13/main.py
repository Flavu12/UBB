"""
5) Generați bilete la PRONOSPORT pentru un bilet cu N meciuri. Pronosticurile pentru un meci
pot fi 1,X,2. Generați toate variantele astfel încât: pronosticul de la ultimul meci nu poate fi X
și există un maxim de două meciuri cu pronosticul 1.
EXEMPLUl:
n=3
1 1 2
1 x 1
1 x 2
1 2 1
1 2 2
x 1 1
x 1 2
x x 1
x x 2
x 2 1
x 2 2
2 1 1
2 1 2
2 x 1
2 x 2
2 2 1
2 2 2

"""

def solutie (lista,n):
    if len(lista) == n and lista[len(lista)-1] != 'X':
        return True
    return False

def consistenta(lista,n):

    if len(lista)>n:
        return False

    max1=0
    for i in range(0,len(lista)):
        if lista[i] == 1:
            max1+=1
    if max1 >2:
        return False
    return True




def backrec(lista,n,valori):
    lista.append(0)

    for i in range(3):
        lista[-1] = valori[i]
        if consistenta(lista,n):
            if solutie(lista,n):
                print(lista)
            backrec(lista[:],n,valori)

    lista.pop()


def consistenta_it(lista,n):


    if len(lista)>n:
        return False

    max1=0
    for i in range(0,len(lista)):
        if lista[i] == 0:
            max1+=1
    if max1 >2:
        return False
    return True


def solutie_it (lista,n):
    if len(lista) == n and lista[len(lista)-1] != 1:
        return True
    return False


def backiter(n,valori):
    lista = [-1]
    while len(lista)>0:
        chosen = False
       #while ul nu e ok
        while not chosen and lista[-1] < len(valori)-1:
            lista[-1] = lista[-1]+1  #aici ia indicii (0,1,2)
            chosen = consistenta_it(lista,n)
        if chosen:
            if solutie_it(lista,n):
                print([valori[i] for i in lista])
            else:
                lista.append(-1)
        else:
            lista = lista[:-1]




def main():
    n= int (input("n= "))
    valori = [1,'X',2]
    print("Backtracking recursiv")
    backrec([],n,valori)
    print("Backtraking iterativ")
    backiter(n,valori)

main()