# 📌 Proiect: Aplicație pentru firmă de închiriere filme

## 📖 Enunț

Scrieți o aplicație pentru o firmă de închiriere de filme.

Aplicația stochează informații despre:

- **Filme**: `<id>`, `<titlu>`, `<descriere>`, `<gen>`, etc.
- **Clienți**: `<id>`, `<nume>`, `<CNP>`, etc.

Aplicația permite gestionarea filmelor, clienților, închirierilor și generarea de rapoarte.

---

## ⚙️ Cerințe generale

- Folosiți **dezvoltarea iterativă bazată pe funcționalități**
- Identificați și planificați funcționalitățile pe **3 iterații**
- Folosiți **dezvoltare dirijată de teste (TDD)**
- Toate funcțiile trebuie:
  - specificate
  - testate
- Folosiți **arhitectură stratificată**:
  - UI
  - Controller
  - Domain
  - Repository
- Validați datele de intrare
- Pentru intrări invalide, aplicația trebuie să afișeze mesaje de eroare corespunzătoare
- Folosiți **excepții** pentru tratarea erorilor

---

## 🧱 Arhitectura aplicației

### 1. UI
Responsabil pentru interacțiunea cu utilizatorul:
- afișare meniu
- citire date
- afișare rezultate
- afișare mesaje de eroare

### 2. Controller
Responsabil pentru logica aplicației:
- coordonează operațiile
- apelează repository-ul
- gestionează validările și excepțiile

### 3. Domain
Conține entitățile principale:
- `Film`
- `Client`
- `Inchiriere`

### 4. Repository
Responsabil pentru stocarea datelor:
- adăugare
- ștergere
- modificare
- căutare
- listare

---

## 🧩 Lista de funcționalități

### 1. Gestiune filme
- Adaugă film
- Șterge film
- Modifică film
- Listează filme
- Caută film

---

### 2. Gestiune clienți
- Adaugă client
- Șterge client
- Modifică client
- Listează clienți
- Caută client

---

### 3. Închiriere / returnare filme
- Închiriere film de către un client
- Returnare film
- Verificare disponibilitate film

---

### 4. Rapoarte
- Clienți cu filme închiriate ordonați după nume
- Clienți cu filme închiriate ordonați după numărul de filme închiriate
- Cele mai închiriate filme
- Primii 30% clienți cu cele mai multe filme închiriate

---

## 🔄 Plan de iterații

### Iterația 1

Funcționalități implementate:

- Adăugare film
- Ștergere film
- Listare filme
- Adăugare client
- Listare clienți
- Ștergere client

---

### Iterația 2

Funcționalități implementate:

- Modificare film
- Modificare client
- Căutare film
- Căutare client
- Închiriere film
- Returnare film

---

### Iterația 3

Funcționalități implementate:

- Clienți cu filme închiriate ordonați după nume
- Clienți cu filme închiriate ordonați după numărul de filme închiriate
- Cele mai închiriate filme
- Primii 30% clienți cu cele mai multe filme închiriate
