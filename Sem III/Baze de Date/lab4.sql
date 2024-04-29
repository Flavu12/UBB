USE Biblioteca
/*

Tabela care are cheie primara si nu are cheie staina
-Autori
Tabela care are cheie primara si cheie straina
-Angajati
Tabela care are doua campuri ca si cheie primara
-Biblioteci_Carti

*/

Insert into Tables(Name)
values ('Autori'),
('Angajati'),
('Biblioteci_Carti');


Go
CREATE View View_Autori AS 
Select * From Autori;
Go

Go
Create View View_Angajati AS
SELECT B.locatie, COUNT(A.cnp) as Numar_Angajati
From Biblioteci B 
INNER JOIN Angajati A ON B.id = A.id_biblioteca
GROUP BY B.locatie;
GO

Create View View_Number_Carti_B AS
SELECT B.locatie, COUNT(BC.id_carte) AS NR_Carte
FROM Biblioteci B
INNER JOIN Biblioteci_Carti BC on B.id = BC.id_biblioteca
INNER JOIN Carti C on C.id = BC.id_carte
GROUP BY B.locatie
GO

-- Adaugam view urile in tabel

INSERT INTO Views(Name)
values('View_Autori'),
('View_Angajati'),
('View_Number_Carti_B');


-----------------------------------------------
--pentru autori

GO
Create procedure inserare_test_Autori @NoOfRows INT
AS 
BEGIN

	SET NOCOUNT ON;
	DECLARE @nume_autor varchar(30);
	DECLARE @prenume_autor varchar(100);
	DECLARE @data_nasterii DATE;
	DECLARE @n INT = 0;
	DECLARE @last_id INT = (SELECT MAX(Autori.id) From Autori);

	while  @n < @NoOfRows
	BEGIN
	set @nume_autor = 'test_nume ' + CONVERT(VARCHAR(10), @last_id);
	set @prenume_autor = 'test_prenume';
	SET @data_nasterii = GETDATE(); -- Data curentă
	INSERT INTO Autori(nume, prenume, data_nasterii)
	VALUES
	(@nume_autor, @prenume_autor, @data_nasterii)
	set @last_id = @last_id + 1
	set @n = @n + 1;
	END

	PRINT 'S-au insertat ' + CONVERT(VARCHAR(10), @NoOfRows) + ' valori in Autori';
	END

GO

EXEC inserare_test_Autori 5


--operatia inversa de stergere al autorilor creati

GO 
CREATE PROCEDURE sterge_test_Autori
AS
BEGIN
	SET NOCOUNT ON;
	DELETE FROM Autori
	WHERE Autori.nume LIKE 'test_nume %';
	PRINT 'S-au sters ' + CONVERT(VARCHAR(10), @@ROWCOUNT) + ' valori din Autori'
END

SELECT * FROM Autori

EXEC inserare_test_Autori 10
EXEC sterge_test_Autori


--pentru angajati 

SELECT * FROM Angajati


GO
Create procedure inserare_test_Angajati @NoOfRows INT
AS 
BEGIN

	SET NOCOUNT ON;
	
	DECLARE @Fk_1 INT = (SELECT TOP 1 id From Biblioteci);
	DECLARE @nume varchar(30);
	DECLARE @prenume varchar(30);
	DECLARE @n INT = 0;
	DECLARE @last_id INT = (SELECT MAX(Angajati.cnp) FROM Angajati)

	WHILE @n < @NoOfRows
	BEGIN
	SET @nume = 'test_nume ' + CONVERT(VARCHAR(10),@last_id);
	SET @prenume = 'test_prenume ' + CONVERT(VARCHAR(10), @last_id);
	INSERT INTO Angajati(nume,prenume, id_biblioteca)
	values(@nume,@prenume,@Fk_1)
	SET @last_id = @last_id + 1;
	SET @n = @n + 1;
	END

	PRINT 'S-au inserat ' + CONVERT(VARCHAR(10),@NoOfRows) + ' valori in Angajati.';

	END
GO


EXEC inserare_test_Angajati 100;


--stergere date angajati

GO
GO 
CREATE PROCEDURE sterge_test_Angajati
AS
BEGIN
	SET NOCOUNT ON;
	DELETE FROM Angajati
	WHERE Angajati.nume LIKE 'test_nume %';
	PRINT 'S-au sters ' + CONVERT(VARCHAR(10), @@ROWCOUNT) + ' valori din Angajati'
END

EXEC sterge_test_Angajati


--Biblioteci_Carti

select * from Biblioteci_Carti


Go 
CREATE PROCEDURE inserare_test_Biblioteci_Carti @NoOfRows INT
AS
BEGIN

	SET NOCOUNT ON;

	DECLARE @n INT = 0;
	DECLARE @Id_Biblioteca INT = (SELECT TOP 1 Biblioteci.id from Biblioteci);
	DECLARE @Id_Carte INT;
	DECLARE @disponibilitate CHAR;

	DECLARE cursorCarti CURSOR FAST_FORWARD FOR
			SELECT id FROM Carti where Carti.titlu LIKE 'test_titlu %';

	OPEN cursorCarti;

	FETCH NEXT FROM cursorCarti INTO @Id_Carte;
	WHILE (@n < @NoOfRows) AND (@@FETCH_STATUS = 0)
	BEGIN
		SET @disponibilitate = 'A';
		INSERT INTO Biblioteci_Carti(id_biblioteca,id_carte, disponibilitate) VALUES (@Id_Biblioteca, @Id_Carte, @disponibilitate)
		SET @n = @n + 1;

		FETCH NEXT FROM cursorCarti INTO @Id_Carte;

	END

	CLOSE cursorCarti;
	DEALLOCATE cursorCarti;

	PRINT 'S-au inserat ' + CONVERT(VARCHAR(10), @n) + ' valori in Biblioteci_Carti';

END
GO

	EXEC inserare_test_Biblioteci_Carti 20;

-- stergere Biblioteci_Carti

Go
CREATE PROCEDURE sterge_test_Biblioteci_Carti
AS
BEGIN
	SET NOCOUNT ON;
	DELETE FROM Biblioteci_Carti
	WHERE Biblioteci_Carti.disponibilitate = 'A';
	PRINT 'S-au sters ' + CONVERT(VARCHAR(10), @@ROWCOUNT) + ' valori din Biblioteci_Carti';
END
GO

EXEC sterge_test_Biblioteci_Carti

INSERT INTO Tests VALUES
('TEST_Autori_10000'),
('TEST_Angajati_10'),
('TEST_Biblioteci_Carti_10')
Go

INSERT INTO Tests VALUES
('TEST_Autori_10')
DELETE FROM Tests

select * from Tests
Drop TABLE Tests

select * from Tables

select * from TestTables

select * from TestViews

----- Fac legatura intre teste si tabele -----

INSERT INTO TestTables VALUES
	-- TEST_Autori_10
	(5, 1, 10000, 1),
	-- TEST_Angajati_10
	(6, 2, 10, 2),
	-- TEST_Biblioteci_Carti_10
	(7, 1, 10, 3);

INSERT INTO TestTables VALUES 
(7,3,10,4);

SELECT * FROM TestTables;
GO


----- Fac legatura intre teste si view-uri -----

INSERT INTO TestViews VALUES
	(5, 1),
	(6, 2),
	(7, 3);


GO
create procedure inserare_test @id_test INT
AS
BEGIN
	
	DECLARE @numeTest VARCHAR(30) = (SELECT T.Name from Tests T WHERE T.TestID = @id_test)
	DECLARE @numeTable VARCHAR(30);
	DECLARE @NoOfRows INT;
	DECLARE @procedura VARCHAR(30);

	DECLARE cursorTab CURSOR FORWARD_ONLY FOR
		SELECT Tab.Name, Test.NoOfRows FROM TestTables Test
		INNER JOIN Tables Tab ON Test.TableID = Tab.TableID
		WHERE Test.TestID = @id_test
		ORDER BY Test.Position;
	OPEN cursorTab;


	FETCH NEXT FROM cursorTab INTO @numeTable, @NoOfRows;
	WHILE (@numeTest NOT LIKE N'TEST_' + @numeTable + N'_' + CONVERT(VARCHAR(10),@NoOfRows)) AND (@@FETCH_STATUS = 0)
	BEGIN
		SET @procedura = N'inserare_test_' + @numeTable
		EXECUTE @procedura @NoOfRows
		FETCH NEXT FROM  cursorTab INTO @numeTable, @NoOfRows;
	END


	SET @procedura = N'inserare_test_' + @numeTable;
	EXEC @procedura @NoOfRows

	CLOSE cursorTab;
	DEALLOCATE cursorTab;

END 


EXEC inserare_test 5

GO 
Create procedure stergere_testgen @id_test INT
AS
BEGIN
	DECLARE @numeTest VARCHAR(30) = (SELECT T.Name from Tests T WHERE T.TestID = @id_test)
	DECLARE @numeTable VARCHAR(30);
	DECLARE @NoOfRows INT;
	DECLARE @procedura VARCHAR(30);

	DECLARE cursorTab CURSOR FORWARD_ONLY FOR
		SELECT Tab.Name, Test.NoOfRows FROM TestTables Test
		INNER JOIN Tables Tab ON Test.TableID = Tab.TableID
		WHERE Test.TestID = @id_test
		ORDER BY Test.Position DESC;
	OPEN cursorTab;


	FETCH NEXT FROM cursorTab INTO @numeTable, @NoOfRows;
	WHILE (@numeTest NOT LIKE N'TEST_' + @numeTable + N'_' + CONVERT(VARCHAR(10),@NoOfRows)) AND (@@FETCH_STATUS = 0)
	BEGIN
		SET @procedura = N'sterge_test_' + @numeTable
		EXECUTE @procedura 
		FETCH NEXT FROM  cursorTab INTO @numeTable, @NoOfRows;
	END

	SET @procedura = N'sterge_test_' + @numeTable;
	EXECUTE @procedura 

	CLOSE cursorTab;
	DEALLOCATE cursorTab;
END


select * from Tests

EXEC inserare_test 5
select * from Autori
EXEC stergere_testgen 5
EXEC sterge_test_Autori

GO
CREATE PROCEDURE view_testgen @id_test INT
AS
BEGIN

	DECLARE @viewName VARCHAR(50)=
		(SELECT V.Name FROM Views V
		INNER JOIN TestViews TV ON TV.ViewID = V.ViewID
		WHERE TV.TestID = @id_test);

	DECLARE @comanda VARCHAR(55) = N'SELECT * FROM ' + @viewName;

	EXECUTE (@comanda);

END
select * from Tests

drop procedure run_test
GO
CREATE PROCEDURE run_test @id_test INT
AS
BEGIN
	
	DECLARE @startTime DATETIME;
	DECLARE @inerTime DATETIME;
	DECLARE @endTime DATETIME;

	SET @startTime = GETDATE();

	EXECUTE stergere_testgen @id_test;
	EXECUTE inserare_test @id_test;

	SET @inerTime = GETDATE();
	
	EXECUTE view_testgen @id_test;

	SET @endTime = GETDATE();

	DECLARE @testName VARCHAR(30) = 
	(SELECT T.Name FROM Tests T WHERE T.TestID = @id_test);
	INSERT INTO TestRuns Values(@testName, @startTime, @endTime);

	DECLARE @viewID INT =
		(SELECT V.ViewID FROM Views V
		INNER JOIN TestViews TV ON TV.ViewID = V.ViewID
		WHERE TV.TestID = @id_test);
	DECLARE @tableID INT =
		(SELECT TB.TableID FROM Tests T
		INNER JOIN TestTables TT ON T.TestID = TT.TestID
		INNER JOIN Tables TB ON TB.TableID = TT.TableID
		WHERE T.TestID = @id_test);
	DECLARE @testRunID INT = 
		(SELECT TOP 1 T.TestRunID FROM TestRuns T
		WHERE T.Description = @testName
		ORDER BY T.TestRunID DESC);

	INSERT INTO TestRunTables VALUES (@testRunID, @tableID, @startTime, @inerTime);
	INSERT INTO TestRunViews VALUES (@testRunID, @viewID, @inerTime, @endTime);

	PRINT CHAR(10) + '---> TEST DONE ' + CONVERT(VARCHAR(10), DATEDIFF(millisecond, @startTime, @endTime)) + ' milisecunde.'
END

EXECUTE run_test 5;

EXec sterge_test_Autori
SELECT * FROM Tests
Select * from TestTables
Select * from TestViews
SELECT * FROM TABLES
SELECT * FROM VIEWS
SELECT * FROM TestRunViews
SELECT * from TestRunTables
SELECT * FROM TestRuns
SELECT* from TestTables