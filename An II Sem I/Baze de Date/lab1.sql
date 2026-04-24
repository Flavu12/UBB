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