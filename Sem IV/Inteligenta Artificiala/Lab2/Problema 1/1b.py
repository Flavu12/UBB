
#1.b. Sa se vizualizeze:

#distributia salariilor acestor angajati pe categorii de salar
#distributia salariilor acestor angajati pe categorii de salar si echipa din care fac parte
#angajatii care pot fi considerati "outlieri"

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data/employees.csv")

# Vizualizarea distribuției salariilor pe categorii de salar
plt.figure(figsize=(10, 6))
sns.histplot(data=df, x='Salary', bins=20, kde=True)
plt.title("Distribuția salariilor angajaților")
plt.xlabel("Salariu")
plt.ylabel("Număr de angajați")
plt.show()

# Vizualizarea distribuției salariilor pe categorii de salar și echipa
plt.figure(figsize=(12, 8))
sns.boxplot(data=df, x='Team', y='Salary')
plt.title("Distribuția salariilor angajaților pe echipă")
plt.xlabel("Echipă")
plt.ylabel("Salariu")
plt.xticks(rotation=45)
plt.show()

# Vizualizarea angajaților outlieri în raport cu salariul și echipa
# Identificarea "outlierilor" în funcție de salariu
plt.figure(figsize=(12, 6))
sns.boxplot(x=employees_date['Salary'])
plt.title('Identificarea "outlierilor" in functie de salariu')
plt.xlabel('Salariu')
plt.show()