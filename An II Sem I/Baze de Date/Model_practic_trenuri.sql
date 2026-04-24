--MODEL DE PRACTIC 
--Creeati o baza de date pentru gestiunea mersurilor trenurilor.
--Baza de date contine informatii despre rutele tuturor trenurilor.


--Entitatile de interes sunt: trenuri, tipuri de tren, statii si rute.
--Fiecare tren are un nume si apartine unui tip. Tipul trenului are o descriere.
--Fiecare rută are un nume, un tren asociat și o listă de stații cu ora sosirii
--și ora plecării pentru fiecare stație. 
--Ora sosirii și ora plecării sunt reprezentate ca perechi oră/minut 
--(exemplu: trenul ajunge la 5 PM și pleacă la 5:10 PM). Stația are un nume.


--1.Scrieți un script SQL care creează un model relațional pentru a reprezenta 
--datele. (4 puncte)

CREATE DATABASE Trenuri

CREATE TABLE Tipuri(
	id_tip int PRIMARY KEY IDENTITY(1,1),
	descriere VARCHAR(100))

CREATE TABLE Trenuri(
	id_tren int PRIMARY KEY IDENTITY(1,1),
	nume VARCHAR(50),
	id_tip int FOREIGN KEY REFERENCES Tipuri(id_tip))

CREATE TABLE Rute(
	id_ruta int PRIMARY KEY IDENTITY(1,1),
	nume VARCHAR(50),
	id_tren int FOREIGN KEY REFERENCES Trenuri(id_tren))

CREATE TABLE Statii(
	id_statie int PRIMARY KEY IDENTITY(1,1),
	nume VARCHAR(50))

CREATE TABLE Rute_Statii(
	id_ruta int FOREIGN KEY REFERENCES Rute(id_ruta),
	id_statie int FOREIGN KEY REFERENCES Statii(id_statie),
	PRIMARY KEY(id_ruta, id_statie),
	ora_plecare TIME,
	ora_sosire TIME)

	--INTRODUCERE DATE

INSERT INTO Tipuri (descriere)
VALUES ('IR'),('IC'),('R');
 
INSERT INTO Trenuri(nume, id_tip) VALUES
('531',2), ('532',2), ('1831',1), ('8000',3);
 
INSERT INTO Rute(nume, id_tren) VALUES
('Brasov-Cluj', 1), ('Cluj-Brasov', 2), ('Iasi-Timisoara',3),('Timisoara-Iasi',4);
 
INSERT INTO Statii(nume) VALUES
('Brasov'), ('Cluj'), ('Iasi'),('Timisoara'),('Dej');


--2) Creați o procedură stocată care primește o rută, o stație, ora sosirii, ora plecării
--și adaugă noua stație rutei. 
--Dacă stația există deja, se actualizează ora sosirii și ora plecării. (3 puncte)

CREATE OR ALTER PROCEDURE UpsertStatiiRute @id_ruta INT, @id_statie INT,
                                           @ora_sosire TIME, @ora_plecare TIME
AS
BEGIN
    IF(EXISTS(SELECT * FROM Rute_Statii WHERE id_ruta = @id_ruta and id_statie = @id_statie))
    BEGIN
        UPDATE Rute_Statii 
        SET ora_sosire = @ora_sosire, ora_plecare = @ora_plecare 
        WHERE id_ruta = @id_ruta and id_statie = @id_statie;
    END
    ELSE
    BEGIN
        INSERT INTO Rute_Statii(id_statie, id_ruta, ora_sosire, ora_plecare)
        VALUES (@id_statie, @id_ruta, @ora_sosire, @ora_plecare);
    END
END

SELECT * FROM Rute_Statii;
EXEC UpsertStatiiRute 1, 1, '16:40:20','20:15:00'
EXEC UpsertStatiiRute 1, 1, '17:40:21','21:15:00'


--3) Creați un view care afișează numele rutelor care conțin toate stațiile. (2 puncte)

create or alter view viewToateStatiile as
	select Rute.nume from Rute
	inner join Rute_Statii on Rute.id_ruta = Rute_Statii.id_ruta
	group by Rute.id_ruta, Rute.nume
	having count(*) = (select COUNT(*) from Statii)
go