# 📌 Proiect: Gestionare listă de numere complexe

## 📖 Enunț
Creați un program care lucrează cu numere complexe de forma **a + bi**.  
Programul gestionează o listă de numere complexe și permite efectuarea repetată a unor operații asupra acesteia.

---

## ⚙️ Cerințe generale

- Folosiți:
  - **Dezvoltare incrementală bazată pe funcționalități**
  - **Dezvoltare dirijată de teste (TDD)**

- Planificați implementarea pe **3 iterații (3 laboratoare succesive)**  
  - La fiecare laborator se acordă notă pentru progres

- **Prima iterație** trebuie să conțină:
  - cel puțin **3 cerințe din funcționalitățile 3-5**

- Documentația trebuie să includă:
  - enunțul
  - lista de funcționalități
  - planul de iterații
  - scenarii de rulare
  - lista de taskuri (activități)

- Cerințe de implementare:
  - toate funcțiile trebuie să aibă **specificații**
  - toate funcțiile trebuie **testate cu `assert`**
  - NU se testează partea de UI (input/output)

- Separare clară:
  - **logica aplicației** ≠ **interfața utilizatorului**

- Structură:
  - Iterația 1: soluție **procedurală (un singur modul)**
  - Final: soluție **modulară**

- Validare:
  - toate datele de intrare trebuie validate
  - programul trebuie să semnaleze erorile

---

## 🧩 Funcționalități

### 1. ➕ Adăugare numere
- Adaugă număr complex la sfârșitul listei
- Inserare număr complex pe o poziție dată

---

### 2. ✏️ Modificare elemente
- Șterge element de pe o poziție dată
- Șterge elementele de pe un interval de poziții
- Înlocuiește toate aparițiile unui număr complex cu altul

---

### 3. 🔍 Căutare
- Tipărește partea imaginară pentru un interval de poziții
- Tipărește numerele cu modulul < 10
- Tipărește numerele cu modulul = 10

---

### 4. 🧮 Operații pe listă
- Suma numerelor dintr-o subsecvență
- Produsul numerelor dintr-o subsecvență
- Sortare descrescătoare după partea imaginară

---

### 5. 🧹 Filtrare
- Elimină numerele cu partea reală primă
- Elimină numerele în funcție de modul:
  - mai mic decât o valoare
  - egal cu o valoare
  - mai mare decât o valoare

---

### 6. ↩️ Undo
- Reface ultima operație care a modificat lista
- ⚠️ Nu se folosește `deepcopy`
