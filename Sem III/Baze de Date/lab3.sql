USE Biblioteca

--MODIFICAREA TIPULUI UNEI COLOANE
--procedura creata pentru a modifica tipul de date al coloanei data_nasterii
CREATE PROCEDURE SetDate
AS
    ALTER TABLE Autori
        ALTER COLUMN data_nasterii varchar(30)
GO

--procedura creata pentru a reveni la tipul de date standart al coloanei data_nasterii
CREATE PROCEDURE SetDateBack
AS
    ALTER TABLE Autori
        ALTER COLUMN data_nasterii date
GO

EXEC SetDate
SELECT *
FROM Autori
EXEC SetDateBack


--ADAUGARE DE CAMP NOU
--procedura creata pentru a aduga o coloana limba pentru tabelul carti
CREATE PROCEDURE AddLanguage
AS
    ALTER TABLE Carti
        ADD limba varchar(20)
GO

--procedura creata pentru a sterge coloana limba din tabelul carti
CREATE PROCEDURE RemoveLanguage
AS
    ALTER TABLE Carti
        DROP COLUMN limba
GO

EXEC AddLanguage
SELECT *
FROM Carti
EXEC RemoveLanguage

--ADAUGARE DE CONSTRANGERE DE "VALOARE IMPLICITA" PENTRU UN CAMP
--procedura de adaugare a constrangerii implicite pentru coloana limba
CREATE PROCEDURE DefaultLanguage
AS
    ALTER TABLE Carti
        ADD CONSTRAINT DefaultConstraint DEFAULT 'romana' FOR limba
GO

--procedura de stergere a constrangerii implicite pentru coloana limba
CREATE PROCEDURE RemoveDefault
AS
    ALTER TABLE Carti
        DROP CONSTRAINT DefaultConstraint
GO

EXEC DefaultLanguage
EXEC RemoveDefault

--CREEAZA/STERGE O TABELA

CREATE PROCEDURE CreeazaRezervare
AS
	CREATE TABLE Rezervari
	(
	id INT CONSTRAINT IdPrimaryKey PRIMARY KEY,
    nume VARCHAR(50) NOT NULL,
    prenume VARCHAR(30) NOT NULL,
    )
GO

CREATE PROCEDURE DropRezervare
AS
	DROP TABLE Rezervari
GO

EXEC CreeazaRezervare
EXEC DropRezervare

--CREEAZA/STERGE O CONSTRANGERE DE CHEIE STRAINA
CREATE PROCEDURE AddSForeignKey
AS
    ALTER TABLE Sali_de_lectura
    ADD CONSTRAINT SaliForeignKey
    FOREIGN KEY (id_biblioteca)
    REFERENCES Biblioteci(id);
GO

CREATE PROCEDURE RemoveSForeignKey
AS
    ALTER TABLE Sali_de_lectura
        DROP CONSTRAINT SaliForeignKey
GO

EXEC AddSForeignKey
EXEC RemoveSForeignKey


------------------------------------------------------------------------
CREATE TABLE VersionHistory
(
    VERSION INT
)

INSERT INTO VersionHistory
VALUES (0)
CREATE TABLE ProcedureTable
(
    UndoProcedure VARCHAR(100),
    RedoProcedure VARCHAR(100),
    Version       INT PRIMARY KEY
)
SELECT * FROM ProcedureTable
SELECT * FROM VersionHistory


CREATE PROCEDURE GoToVersion @Version INT
AS
DECLARE @var INT;
    SET @var = (SELECT TOP 1 VH.VERSION
                FROM VersionHistory VH)
DECLARE @statements CHAR(100);
DECLARE @procedure NVARCHAR(100);
DECLARE @var2 INT

WHILE @var != @Version
BEGIN
if @var > @Version
BEGIN
DECLARE UndoCursor CURSOR
    FOR SELECT PT.UndoProcedure
        FROM ProcedureTable PT
OPEN UndoCursor

SELECT @var2 = 0
WHILE @var2 != @var
    BEGIN
        FETCH FROM UndoCursor INTO @statements
        SELECT @var2 = @var2 + 1
    END
if @var = @Version
    BEGIN
        print 'Stop here'
        BREAK
    END
ELSE
    BEGIN
        SELECT @procedure = 'exec ' + @statements
        print @procedure
        print 'This was the procedure'
        EXEC sp_executesql @procedure
        UPDATE VersionHistory
        SET VERSION = VERSION - 1
        SET @var = @var - 1;
        FETCH FROM UndoCursor INTO @statements
    END
    CLOSE UndoCursor
    DEALLOCATE UndoCursor
END
    ELSE
    BEGIN
        DECLARE RedoCursor CURSOR FOR SELECT PT.RedoProcedure FROM ProcedureTable PT
        OPEN RedoCursor
SELECT @var2 = -1
WHILE @var2 != @var
    BEGIN
        FETCH FROM RedoCursor INTO @statements
        SELECT @var2 = @var2 + 1
    END
if @var = @Version
    BEGIN
        print 'Stop here'
        BREAK
    END
ELSE
    BEGIN
        SELECT @procedure = 'exec ' + @statements
        print @procedure
        print 'This was the procedure'
        EXEC sp_executesql @procedure
        UPDATE VersionHistory
        SET VERSION = VERSION + 1
        SET @var = @var + 1;
        FETCH FROM RedoCursor INTO @statements
    END
        CLOSE RedoCursor
        DEALLOCATE RedoCursor
    END
END



INSERT INTO ProcedureTable(UndoProcedure, RedoProcedure, Version)
VALUES
    ('SetDateBack', 'SetDate', 1),
    ('RemoveLanguage', 'AddLanguage', 2),
    ('DropRezervare', 'CreeazaRezervare', 3),
    ('RemoveDefault', 'DefaultLanguage', 4),
    ('RemoveSForeignKey', 'AddSForeignKey', 5)


SELECT * FROM ProcedureTable
EXECUTE GoToVersion @Version = 3
SELECT *
FROM VersionHistory

drop table ProcedureTable