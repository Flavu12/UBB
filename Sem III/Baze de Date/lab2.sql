--CREATE DATABASE Biblioteca

CREATE TABLE Biblioteci(
	id int PRIMARY KEY IDENTITY(1,1),
	locatie VARCHAR(50),
	program VARCHAR(50))

CREATE TABLE Sali_de_lectura(
	id int PRIMARY KEY IDENTITY(1,1),
	capacitate int,
	program VARCHAR(50),
	id_biblioteca int FOREIGN KEY REFERENCES Biblioteci(id))

CREATE TABLE Angajati(
	cnp int PRIMARY KEY IDENTITY(1,1),
	nume VARCHAR(30),
	prenume VARCHAR(30),
	id_biblioteca int FOREIGN KEY REFERENCES Biblioteci(id))

CREATE TABLE Edituri(
	id int PRIMARY KEY IDENTITY(1,1),
	nume VARCHAR(30),
	an_aparitie int)

CREATE TABLE Carti(
	id int PRIMARY KEY IDENTITY(1,1),
	titlu VARCHAR(30),
	descriere VARCHAR(200),
	an_aparitie int,
	id_editura int FOREIGN KEY REFERENCES Edituri(id))

CREATE TABLE Recenzii(
	id int PRIMARY KEY IDENTITY(1,1),
	continut VARCHAR(200),
	autor VARCHAR(50),
	pozitiv char(1),
	id_carte int FOREIGN KEY REFERENCES Carti(id))

CREATE TABLE Tipuri(
	id int PRIMARY KEY IDENTITY(1,1),
	denumire VARCHAR(30),
	descriere VARCHAR(100))

CREATE TABLE Autori(
	id int PRIMARY KEY IDENTITY(1,1),
	nume VARCHAR(30),
	prenume VARCHAR(30),
	data_nasterii DATE)

CREATE TABLE Biblioteci_Carti(
	id_biblioteca int FOREIGN KEY REFERENCES Biblioteci(id),
	id_carte int FOREIGN KEY REFERENCES Carti(id),
	PRIMARY KEY(id_biblioteca, id_carte),
	disponibilitate CHAR(1))

CREATE TABLE Carti_Tipuri(
	id_carte int FOREIGN KEY REFERENCES Carti(id),
	id_tip int FOREIGN KEY REFERENCES Tipuri(id),
	PRIMARY KEY(id_carte, id_tip),)

CREATE TABLE Carti_Autori(
	id_carte int FOREIGN KEY REFERENCES Carti(id),
	id_autor int FOREIGN KEY REFERENCES Autori(id),
	PRIMARY KEY(id_carte, id_autor),
	numar_capitole int)

--INTRODUCERE VALORI

INSERT INTO Biblioteci (locatie, program)
VALUES ('str. Nicolae Titulescu', 'Luni-Vineri 9:00-18:00');

INSERT INTO Biblioteci (locatie, program)
VALUES ('str. Observatorului', 'Luni-Duminica 7:00-14:00');

INSERT INTO Tipuri(denumire, descriere)
VALUES('Horror', 'Poate contine scene cu impact emotional')

INSERT INTO Tipuri(denumire, descriere)
VALUES('Romantic', 'Povestea de dragoste')

INSERT INTO Tipuri(denumire, descriere)
VALUES('SF', 'O lume plina de creaturi imaginare')

INSERT INTO Tipuri(denumire, descriere)
VALUES('Dezvoltare personala', 'Ghid pentru a te descoperi pe tine insuti')

INSERT INTO Tipuri(denumire, descriere)
VALUES('Parenting', 'Ghid pentru tinerii parinti')

INSERT INTO Edituri(nume, an_aparitie)
VALUES('Humanitas', 1980)


INSERT INTO Edituri(nume, an_aparitie)
VALUES('Artic', 2020)

INSERT INTO Edituri(nume, an_aparitie)
VALUES('ABC', 2000)

INSERT INTO Angajati(nume, prenume, id_biblioteca)
VALUES ('Popescu', 'Ana', 1);

INSERT INTO Angajati (nume, prenume, id_biblioteca)
VALUES ('Ionescu', 'Mihai', 1);

INSERT INTO Angajati (nume, prenume, id_biblioteca)
VALUES ('Pop', 'Elena', 2);

INSERT INTO Angajati (nume, prenume, id_biblioteca)
VALUES ('Ionel', 'Alexandru', 1);

INSERT INTO Angajati (nume, prenume, id_biblioteca)
VALUES ('Marian', 'Ion', 2);

INSERT INTO Angajati (nume, prenume, id_biblioteca)
VALUES ('Vasile', 'Ioana', 2);

INSERT INTO Angajati (nume, prenume, id_biblioteca)
VALUES ('Marinescu', 'Anca', 2);

INSERT INTO Angajati (nume, prenume, id_biblioteca)
VALUES ('Popa', 'Emilia', 2);

INSERT INTO Recenzii(continut, autor, pozitiv, id_carte)
VALUES('O cabodopera despre suspans si teroare', 'The Washington Post', 'A', 1)

INSERT INTO Recenzii (continut, autor, pozitiv, id_carte)
VALUES ('O carte minunata!', 'John Doe', 'A', 1);

INSERT INTO Recenzii (continut, autor, pozitiv, id_carte)
VALUES ('O carte pe care nu o poti lasa din mana', 'John A.', 'A', 1);

INSERT INTO Carti(titlu, descriere, an_aparitie, id_editura)
VALUES ('The Shining', 'Cartea prezinta destinul teribil al lui Jack Torrance si dezastrul unei familii', 1977, 1);

INSERT INTO Carti(titlu, descriere, an_aparitie, id_editura)
VALUES ('Fabule', 'Fabule alese pentru copii ale autorilor romani', 1999, 2);

INSERT INTO Carti(titlu, descriere, an_aparitie, id_editura)
VALUES ('Umbrele care ne despart', 'Din dusmani la indragostiti este un pas mic', 2021, 2);

INSERT INTO Carti(titlu, descriere, an_aparitie, id_editura)
VALUES ('Carrie', 'O adolescenta descopera ca detine puteri', 1980, 1);

INSERT INTO Carti(titlu, descriere, an_aparitie, id_editura)
VALUES ('Abecedar', 'Manual pentru clasa I', 2010, 3);


INSERT INTO Carti(titlu, descriere, an_aparitie, id_editura)
VALUES ('Secretele comunicarii', 'Pasi pentru a comunica in diferite situatii', 2020, 2);


INSERT INTO Carti(titlu, descriere, an_aparitie, id_editura)
VALUES ('Romeo si Julieta', 'lupta a doi indragostiti impotriva societatii', 1590, 1);


INSERT INTO Carti(titlu, descriere, an_aparitie, id_editura)
VALUES ('Aici si acum', 'Schimbarea se poate realiza doar in prezent', 2019, 3);

INSERT INTO Recenzii(continut, autor, pozitiv, id_carte)
VALUES('O carte cu povesti alese ', 'L. Blaga', 'A', 6)

INSERT INTO Recenzii(continut, autor, pozitiv, id_carte)
VALUES('O carte perfecta pentru copii', 'I. Alecu', 'A', 6)

INSERT INTO Recenzii(continut, autor, pozitiv, id_carte)
VALUES('Ma bucur ca pot sa ma bucur alaturi de copiii mei', 'M. Ioana', 'A', 6)

INSERT INTO Recenzii(continut, autor, pozitiv, id_carte)
VALUES('Ne asteptam la mai multe de la autor', 'M.M. Homes', 'F', 4)

INSERT INTO Recenzii(continut, autor, pozitiv, id_carte)
VALUES('un astfel de manual nu ar trebui sa aiba greseli gramaticale ', 'A.Vasile', 'F', 5)

INSERT INTO Carti(titlu, descriere, an_aparitie, id_editura)
VALUES ('Povesti', 'Carte pentru copii', 1999, 2);


INSERT INTO Autori(nume, prenume, data_nasterii)
VALUES('King', 'Stephen', '1947-09-21')


INSERT INTO Autori(nume, prenume, data_nasterii)
VALUES('Asachi', 'Gheorghe', '1788-03-01')


INSERT INTO Autori(nume, prenume, data_nasterii)
VALUES('Montefiore', 'Santa', '1970-02-02')


INSERT INTO Autori(nume, prenume, data_nasterii)
VALUES('Alexandrescu', 'Grigore', '1810-02-22')


INSERT INTO Autori(nume, prenume, data_nasterii)
VALUES('Mihailescu', 'Cleopatra', '1970-06-12')


INSERT INTO Autori(nume, prenume, data_nasterii)
VALUES('Pitila', 'Tudora', '1971-12-12')


INSERT INTO Autori(nume, prenume, data_nasterii)
VALUES('LevenSeller', 'Tricia', '1989-01-03')

INSERT INTO Sali_de_lectura(capacitate, program, id_biblioteca)
VALUES(200, '12:00-16:00', 1)

INSERT INTO Sali_de_lectura(capacitate, program, id_biblioteca)
VALUES(50, '14:00-18:00', 1)

INSERT INTO Sali_de_lectura(capacitate, program, id_biblioteca)
VALUES(50, '09:00-12:00', 2)

INSERT INTO Sali_de_lectura(capacitate, program, id_biblioteca)
VALUES(100, '12:00-20:00', 2)

INSERT INTO Biblioteci_Carti(id_biblioteca, id_carte, disponibilitate)
VALUES(1,1,'F')

INSERT INTO Biblioteci_Carti(id_biblioteca, id_carte, disponibilitate)
VALUES(2,1002,'F')

INSERT INTO Biblioteci_Carti(id_biblioteca, id_carte, disponibilitate)
VALUES(2,1004,'A')

INSERT INTO Biblioteci_Carti(id_biblioteca, id_carte, disponibilitate)
VALUES(1,1004,'F')

INSERT INTO Biblioteci_Carti(id_biblioteca, id_carte, disponibilitate)
VALUES(2,1,'A')

INSERT INTO Biblioteci_Carti(id_biblioteca, id_carte, disponibilitate)
VALUES(1,5,'F')

INSERT INTO Biblioteci_Carti(id_biblioteca, id_carte, disponibilitate)
VALUES(2,5,'F')

INSERT INTO Biblioteci_Carti(id_biblioteca, id_carte, disponibilitate)
VALUES(1,3,'A')

INSERT INTO Biblioteci_Carti(id_biblioteca, id_carte, disponibilitate)
VALUES(2,3,'F')

INSERT INTO Biblioteci_Carti(id_biblioteca, id_carte, disponibilitate)
VALUES(2,4,'A')

INSERT INTO Carti_Autori(id_carte, id_autor, numar_capitole)
VALUES(1,2, 100)

INSERT INTO Carti_Autori(id_carte, id_autor, numar_capitole)
VALUES(2,3, 20)

INSERT INTO Carti_Autori(id_carte, id_autor, numar_capitole)
VALUES(2, 2, 25)

INSERT INTO Carti_Autori(id_carte, id_autor, numar_capitole)
VALUES(3, 6, 55)

INSERT INTO Carti_Autori(id_carte, id_autor, numar_capitole)
VALUES(5, 5, 10)

INSERT INTO Carti_Autori(id_carte, id_autor, numar_capitole)
VALUES(6,3, 10)

INSERT INTO Carti_Autori(id_carte, id_autor, numar_capitole)
VALUES(6,4, 15)

INSERT INTO Carti_Autori(id_carte, id_autor, numar_capitole)
VALUES(4,1, 75)

INSERT INTO Carti_Autori(id_carte, id_autor, numar_capitole)
VALUES(1004,1002, 45)

INSERT INTO Carti_Tipuri(id_carte, id_tip)
VALUES(1,1)

INSERT INTO Carti_Tipuri(id_carte, id_tip)
VALUES(3, 3)

INSERT INTO Carti_Tipuri(id_carte, id_tip)
VALUES(4, 1)

INSERT INTO Carti_Tipuri(id_carte, id_tip)
VALUES(4, 3)

INSERT INTO Carti_Tipuri(id_carte, id_tip)
VALUES(6, 3)

INSERT INTO Carti_Tipuri(id_carte, id_tip)
VALUES(3, 2)

INSERT INTO Carti_Tipuri(id_carte, id_tip)
VALUES(5, 5)

INSERT INTO Carti_Tipuri(id_carte, id_tip)
VALUES(2, 3)

INSERT INTO Carti_Tipuri(id_carte, id_tip)
VALUES(2, 5)


INSERT INTO Carti_Tipuri(id_carte, id_tip)
VALUES(1002, 4)

INSERT INTO Carti_Tipuri(id_carte, id_tip)
VALUES(1003, 2)


INSERT INTO Carti_Tipuri(id_carte, id_tip)
VALUES(1004, 4)


INSERT INTO Carti_Tipuri(id_carte, id_tip)
VALUES(1, 3)

Select * from Carti
Select * from Autori
Select * from Carti_Autori
Select * from Biblioteci_Carti
Select * from Biblioteci
Select * from Angajati
Select * from Recenzii
Select *from Edituri
Select * from Sali_de_lectura

--INTEROGARI

--La biblioteca cu id-ul 1 dorim sa aducem mai multe carti care au cerere crescuta si sunt inchiriate 
SELECT C.titlu, C.descriere
FROM Carti C
INNER JOIN Biblioteci_Carti BC ON C.id = BC.id_carte
WHERE BC.id_biblioteca = 1 AND BC.disponibilitate = 'F';

--o persoana doreste sa inchirieze o carte scrisa de Stephen King(cauta biblioteca unde cartea este disponibila)
SELECT DISTINCT B.locatie AS Biblioteca
FROM Biblioteci B
INNER JOIN Biblioteci_Carti BC ON B.id = BC.id_biblioteca
INNER JOIN Carti C ON BC.id_carte = C.id
INNER JOIN Carti_Autori CA ON C.id = CA.id_carte
INNER JOIN Autori A ON CA.id_autor = A.id
WHERE A.nume = 'King' AND A.prenume = 'Stephen' AND BC.disponibilitate = 'A';

--O profesoara doreste sa inchirieze carti pentru elevii sai si cauta autori care au cel putin 3 recenzii pozitive
SELECT A.nume, A.prenume
FROM Autori A
INNER JOIN Carti_Autori CA ON A.id = CA.id_autor
INNER JOIN Carti C ON CA.id_carte = C.id
INNER JOIN Recenzii R ON C.id = R.id_carte
WHERE R.pozitiv = 'A'
GROUP BY A.nume, A.prenume
HAVING COUNT(R.id) >= 3;

--Biblioteca doreste sa achizitioneze mai multe carti de la edituri care au recenzii pozitive
SELECT DISTINCT E.nume AS Editura
FROM Edituri E
INNER JOIN Carti C ON E.id = C.id_editura
INNER JOIN Recenzii R ON C.id = R.id_carte
WHERE R.pozitiv = 'A';

--Se doreste sa se achizitioneze mai multe carti cerute pentru fiecare biblioteca. Cautam cartile care nu sunt disponibile din fiecare biblioteca.

SELECT C.titlu AS TitluCarte, B.locatie AS LocatieBiblioteca
FROM Carti C
INNER JOIN Biblioteci_Carti BC ON C.id = BC.id_carte
INNER JOIN Biblioteci B ON BC.id_biblioteca = B.id
WHERE BC.disponibilitate = 'F';

--Dorim sa aflam numarul de angajati de le fiecare biblioteca

SELECT B.locatie AS Biblioteca, COUNT(A.cnp) AS NrAngajati
FROM Biblioteci B
LEFT JOIN Angajati A ON B.id = A.id_biblioteca
GROUP BY B.locatie;

--Dorim sa aflam cate carti avem la fiecare tip
SELECT T.denumire AS TipCarte, COUNT(C.id) AS NumarCarti
FROM Tipuri T
LEFT JOIN Carti_Tipuri CT ON T.id = CT.id_tip
LEFT JOIN Carti C ON CT.id_carte = C.id
GROUP BY T.denumire;

--3 grupe de studenti vor sa inchirieze o sala de lectura pentru o prezentare si doresc o sala cu capacitate mai mare de 80 de persoane
SELECT S.id AS SalaID, S.capacitate AS CapacitateSala
FROM Sali_de_lectura S
GROUP BY S.id, S.capacitate
HAVING S.capacitate >= 80;

--Cautam carti SF care sa contina recenzii pozitive
SELECT C.titlu, T.denumire, R.pozitiv
FROM Carti C
INNER JOIN Carti_Tipuri CT ON C.id = CT.id_carte
INNER JOIN Tipuri T ON CT.id_tip = T.id
INNER JOIN Recenzii R ON C.id = R.id_carte
WHERE T.denumire = 'SF' AND R.pozitiv = 'A';

--Cautam numarul de carti din biblioteca cu id-ul 2 scrise de fiecare autor
SELECT A.nume, A.prenume, COUNT(DISTINCT C.id) AS numar_carti
FROM Autori A
INNER JOIN Carti_Autori CA ON A.id = CA.id_autor
INNER JOIN Carti C ON CA.id_carte = C.id
INNER JOIN Biblioteci_Carti B ON C.id = B.id_carte
WHERE B.id_biblioteca = 2
GROUP BY A.nume, A.prenume;

--Studentii doresc carti mai actuale din biblioteca cu id-ul 2
SELECT C.titlu, A.nume, A.prenume
FROM Carti C
INNER JOIN Carti_Autori CA ON C.id = CA.id_carte
INNER JOIN Autori A ON CA.id_autor = A.id
INNER JOIN Biblioteci_Carti BC ON C.id = BC.id_carte
WHERE BC.id_biblioteca = 2 AND A.data_nasterii > '1970-01-01';

--Cautam autori cu carti disponibile din biblioteca cu id-ul 2
SELECT DISTINCT A.nume, A.prenume
FROM Autori A
INNER JOIN Carti_Autori CA ON A.id = CA.id_autor
INNER JOIN Carti C ON CA.id_carte = C.id
INNER JOIN Biblioteci_Carti BC ON C.id = BC.id_carte
WHERE BC.id_biblioteca = 2 AND BC.disponibilitate = 'A';






