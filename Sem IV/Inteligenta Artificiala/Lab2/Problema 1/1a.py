#Se cunosc date despre angajatii unei companii, date salvate in fisierul "data/employees.csv".

#1.a. Sa se stabileasca:
#numarul de angajati
#numar si tipul informatiilor (proprietatilor) detinute pentru un angajat
#numarul de angajati pentru care se detin date complete
#valorile minime, maxime, medii pentru fiecare proprietate
#in cazul proprietatilor nenumerice, cate valori posibile are fiecare astfel de proprietate
#daca sunt valori lipsa si cum se poate rezolva aceasta problema

import pandas as pd
df = pd.read_csv("data/employees.csv")

#Numărul de angajați
nr_angajati = df.shape[0]
print("Numărul de angajați:", nr_angajati)

#Numărul și tipul de informații (proprietăți) pentru un angajat
nr_proprietati = df.shape[1]
tip_proprietati = df.dtypes
print("Numărul și tipul de informații (proprietăți) pentru un angajat: ", nr_proprietati)
print("Proprietăți:", tip_proprietati)

# Numărul de angajați pentru care se detin date complete
nr_date_complete = df.dropna().shape[0]
print("Numărul de angajați pentru care se detin date complete:", nr_date_complete)

# Valorile minime, maxime, medii pentru fiecare proprietate numerică
numeric_properties = df.select_dtypes(include=['number'])
valori_min = numeric_properties.min()
print("Valorile minime:")
print(valori_min)
valori_max = numeric_properties.max()
print("Valorile maxime:")
print(valori_max)
valori_medii = numeric_properties.mean()
print("Valorile medii:")
print(valori_medii)

#În cazul proprietăților nenumerice, numărul de valori posibile pentru fiecare proprietate
prop_nenumerice = df.select_dtypes(exclude=['number'])
nr_posibile = prop_nenumerice.apply(lambda x: x.nunique())
print(" Numărul de valori posibile pentru proprietățile nenumerice:")
print(nr_posibile)

#Dacă sunt valori lipsă și cum se poate rezolva această problemă
valori_lipsa = df.isnull().sum()
print("Valori lipsă:")
print(valori_lipsa)
