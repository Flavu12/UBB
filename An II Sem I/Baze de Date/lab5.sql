USE Biblioteca
-- Funcții de Validare
-- Funcții de Validare Modificate

CREATE OR ALTER FUNCTION ValidateCarti_Autori(
  @id_carte INT,
  @id_autor INT,
  @numar_capitole INT
)

RETURNS VARCHAR(255)
AS
BEGIN
  DECLARE @erori VARCHAR(255)='';

  -- Verificarea cartii
  IF @id_carte NOT IN (SELECT id FROM Carti)
    SET @erori = @erori + ' ID carte invalid';

  -- Verificarea autorilor
  IF @id_autor NOT IN (SELECT id FROM Autori)
    SET @erori = @erori + ' ID autor invalid';

  -- Verificare numar_capitole
  IF @numar_capitole IS NULL
    SET @erori = @erori + ' Numar capitole invalid';

  RETURN @erori;
END;
GO


CREATE OR ALTER FUNCTION ValidateCarti(
  @id_carte INT,
  @titlu VARCHAR(255),
  @descriere VARCHAR(255),
  @an_aparitie INT,
  @id_editura INT

)
RETURNS VARCHAR(255)
AS
BEGIN
  DECLARE @erori VARCHAR(255)='';

  -- Verificarea ID-ului
  IF @id_carte < 0 
    SET @erori = 'ID carte invalid';

  -- Verificarea titlului
  IF LEN(@titlu) = 0 OR @titlu IS NULL
    SET @erori = @erori + ' Titlu invalid';
   
   
     -- Verificarea descriere
  IF LEN(@descriere) = 0 OR @descriere IS NULL
    SET @erori = @erori + ' Descriere invalida';


  -- Verificarea an_apatitie
  IF @an_aparitie < 0 
    SET @erori = 'An aparitie invalid';


  RETURN @erori;
END;
GO

CREATE OR ALTER FUNCTION IS_Valid_Carte_Autor(@id_carte INT, @id_autor INT)
RETURNS BIT
AS
BEGIN
    DECLARE @Result BIT;
    IF EXISTS (SELECT * FROM Carti_Autori WHERE id_carte = @id_carte AND id_autor = @id_autor)
        SET @Result = 1
    ELSE
        SET @Result = 0
    RETURN @Result;
END;
GO

SELECT * FROM Carti_Autori 
SELECT dbo.IS_Valid_Carte_Autor(3, 6) AS Is_Valid;

CREATE OR ALTER FUNCTION IS_Valid_Autori(@id_autor INT)
RETURNS varchar(50)
AS
BEGIN
    Declare @erori varchar(50)=''
	if @id_autor <0 
	begin 
	set @erori='Id invalid'
	end
		return @erori
END;
GO

SELECT * FROM Autori
SELECT dbo.IS_Valid_Autori(-1) AS Is_Valid;



CREATE OR ALTER FUNCTION IS_NOT_NULL(@string NVARCHAR(100))
RETURNS BIT
AS
BEGIN
    DECLARE @Result BIT;
    IF @string IS NOT NULL
        SET @Result = 1
    ELSE
        SET @Result = 0
    RETURN @Result;
END;
GO


-- Operații CRUD pe Autori
CREATE OR ALTER PROCEDURE Create_Autori
    @id_autor INT,
    @nume VARCHAR(255),
    @prenume VARCHAR(255),
    @data_nasterii VARCHAR(255),
    @erori VARCHAR(90) OUTPUT 
AS
BEGIN
    SET IDENTITY_INSERT Autori ON
    SET @erori = dbo.IS_Valid_Autori(@id_autor)

    IF @id_autor IN (SELECT id FROM Autori)
    BEGIN 
        THROW 50000, 'id existent', 1;
    END

    IF @erori = ''
    BEGIN 
        INSERT INTO Autori(id, nume, prenume, data_nasterii) VALUES (@id_autor, @nume, @prenume, @data_nasterii);
    END

    SET IDENTITY_INSERT Autori OFF
END
GO

DECLARE @erori VARCHAR(90)
EXEC Create_Autori 2000, 'Nume', 'Prenume', 'An_aparitie', @erori OUTPUT
PRINT @erori
GO

SELECT * from Autori


CREATE OR ALTER PROCEDURE UpdateAutori
     @id_autor INT,
    @nume VARCHAR(255),
    @prenume VARCHAR(255),
    @data_nasterii VARCHAR(255)
AS
BEGIN
  Declare @erori varchar(50)
  set @erori=dbo.IS_Valid_Autori(@id_autor)
   
  IF @erori!=''
  BEGIN 
    THROW 50000, @erori, 1;
  END;
  if @id_autor not in (select id from Autori)
  begin 
  THROW 50000, 'id inexistent', 1;
  end
  update Autori set
  nume=@nume, 
  prenume= @prenume,
  data_nasterii = @data_nasterii 
  where id = @id_autor;

END
GO
 
 select * from Autori
 UpdateAutori 6,'Nume2','Prenume2','data_nasterii'

 CREATE OR ALTER PROCEDURE Toate 
  @NumeTabel NVARCHAR(50)
AS
BEGIN
  DECLARE @SqlQuery NVARCHAR(MAX);

  SET @SqlQuery = 'SELECT * FROM ' + QUOTENAME(@NumeTabel);

  EXEC sp_executesql @SqlQuery;
END;
GO

CREATE OR ALTER PROCEDURE Delete_Autori
    @id_autor INT
AS
BEGIN
    if @id_autor in (select id from Autori)
  begin 
  delete From Autori where id = @id_autor
  end
  else begin THROW 50000, 'id inexistent', 1; end 
END
GO


Delete_Autori 2000



-- Operații CRUD pe Carte
CREATE OR ALTER PROCEDURE Create_Carte
  @id_carte INT,
  @titlu VARCHAR(255),
  @descriere VARCHAR(255),
  @an_aparitie INT,
  @id_editura INT
AS
BEGIN
	IF (SELECT OBJECTPROPERTY(OBJECT_ID('carti'), 'TableHasIdentity')) = 1
        SET IDENTITY_INSERT Autori OFF
	SET IDENTITY_INSERT Carti ON
    Declare @erori varchar(50)
	set @erori=dbo.ValidateCarti(@id_carte,@titlu,@descriere,@an_aparitie, @id_editura)
    IF @erori!=''
	BEGIN 
		THROW 50000, @erori, 1;
	END;
	if @id_carte in (select id from Carti)
	begin 
	THROW 50000, 'id existent', 1;
		end
	INSERT INTO Carti(id,titlu,descriere,an_aparitie, id_editura) VALUES (@id_carte,@titlu,@descriere,@an_aparitie, @id_editura);
	SET IDENTITY_INSERT Carte OFF
END
GO

Select * from Carti
Create_Carte 7, 'Chimista','thriller',1999, 1

CREATE OR ALTER PROCEDURE Update_Carte
  @id_carte INT,
  @titlu VARCHAR(255),
  @descriere VARCHAR(255),
  @an_aparitie INT,
  @id_editura INT
AS
BEGIN
     Declare @erori varchar(90)
	 set @erori=dbo.ValidateCarti(@id_carte,@titlu,@descriere,@an_aparitie, @id_editura)
  
	 IF @erori!=''
     BEGIN 
       THROW 50000, @erori, 1;
     END;
  
	 if @id_carte not in (select id from Carti)
	 begin 
	 THROW 50000, 'id inexistent', 1;
     end

  Update Carti  set  titlu= @titlu , descriere = @descriere , an_aparitie = @an_aparitie, id_editura= @id_editura
  where id=@id_carte
END;
GO

select * from Carti  
Update_Carte 5,'Titlu','interesanta',1


CREATE OR ALTER PROCEDURE Delete_Carte
    @id_carte INT
 
AS
BEGIN   
 
  if @id_carte in (select id from Carti)
  begin 
  delete From Carti where id =@id_carte
  end
  else begin THROW 50000, 'id inexistent', 1; end 
END
GO

Delete_Carte 5


-- Operații CRUD pe Carti_Autori

CREATE OR ALTER PROCEDURE Create_Carti_Autori
  @id_carte INT,
  @id_autor INT,
  @nr_capitole INT,
  @erori VARCHAR(90) OUTPUT
AS
BEGIN
    -- Dezactivăm IDENTITY_INSERT pentru autori dacă este necesar
    IF (SELECT OBJECTPROPERTY(OBJECT_ID('autori'), 'TableHasIdentity')) = 1
        SET IDENTITY_INSERT Autori OFF

    -- Activăm IDENTITY_INSERT pentru Carti_Autori
   -- SET IDENTITY_INSERT Carti_Autori ON

    -- Verificarea și validarea datelor de intrare
    SET @erori = dbo.ValidateCarti_Autori(@id_carte, @id_autor, @nr_capitole)
    IF EXISTS(SELECT * FROM Carti_Autori  WHERE id_carte = @id_carte AND id_autor = @id_autor)
        SET @erori = @erori + ' Deja exista'

    -- Gestionarea erorilor
    IF @erori = ''
    BEGIN
        INSERT INTO Carti_Autori(id_carte,id_autor,numar_capitole) 
        VALUES (@id_carte, @id_autor, @nr_capitole)
    END

    -- Dezactivăm IDENTITY_INSERT pentru Carti_Autori după finalizare
    --SET IDENTITY_INSERT Carti_Autori OFF
END;
GO


DECLARE @erori VARCHAR(90)
EXEC Create_Carti_Autori 7, 1, 50, @erori OUTPUT
PRINT @erori
GO

Select * from Carti_Autori  


CREATE OR ALTER PROCEDURE Update_Carti_Autori
  @id_carte INT,
  @id_autor INT,
  @nr_capitole INT
AS
BEGIN
    DECLARE @erori VARCHAR(90);
    SET @erori = dbo.ValidateCarti_Autori(@id_carte, @id_autor, @nr_capitole);

    IF @erori != ''
    BEGIN
        THROW 50000, @erori, 1;
    END;

    IF NOT EXISTS (SELECT * FROM Carti_Autori WHERE id_carte = @id_carte AND id_autor = @id_autor)
    BEGIN
        THROW 50001, 'Record does not exist for specified id_carte and id_autor', 1;
    END;

    UPDATE Carti_Autori
    SET numar_capitole = @nr_capitole
    WHERE id_carte = @id_carte AND id_autor = @id_autor;
END;
GO



Select * From Carti_Autori 
Update_Carti_Autori 7,1,100

CREATE OR ALTER PROCEDURE Delete_Carti_Autori
    @id_carte int,
  @id_autor INT,
  @mesaj varchar(50) output
 
AS
BEGIN    

  if   exists( select * from Carti_Autori where id_carte=@id_carte and id_autor =@id_autor)
  begin 
  delete From Carti_Autori  where id_carte=@id_carte and id_autor =@id_autor
  end
  else begin THROW 50000, 'id inexistent', 1; end 
  set @mesaj='sters cu succes'
END;
GO

DECLARE @mesaj VARCHAR(90)
EXEC Delete_Carti_Autori 7, 1, @mesaj OUTPUT
PRINT @mesaj

Select * From Carti_Autori



-- Constrângeri pe tabelă și coloană


ALTER TABLE Autori
ADD CONSTRAINT CK_Autori_Name CHECK (LEN(nume) < 20);


ALTER TABLE Carti
ADD CONSTRAINT CK_Carti_descriere CHECK (LEN(descriere) < 30);

ALTER TABLE Carti_Autori 
ADD CONSTRAINT FK_Carti_Autori_id_carte FOREIGN KEY (id_carte) REFERENCES Carti(id),
    CONSTRAINT FK_Carti_Autori_id_autor FOREIGN KEY (id_autor) REFERENCES Autori(id);

-- Indexuri Non-Clustered
CREATE NONCLUSTERED INDEX index_Nume1 ON Autori (prenume, data_nasterii) INCLUDE (nume);
CREATE NONCLUSTERED INDEX index_NumeCarti1 ON Carti (titlu,an_aparitie,id_editura) INCLUDE (descriere);
CREATE NONCLUSTERED INDEX index_DataCarti_Autori1 ON Carti_Autori (id_carte,id_autor) INCLUDE (numar_capitole);
CREATE NONCLUSTERED INDEX index_CarteId ON Carti_Autori(id_carte);
Select *from Carti_Autori
Select *from Carti
Select* from Autori

CREATE OR ALTER VIEW View_AutoriPerCarte
AS
SELECT 
    c.titlu AS titluCarte,
    COUNT(ca.id_autor) AS numarAutor
FROM 
    Carti c
INNER JOIN 
    Carti_Autori ca ON c.id = ca.id_carte 
GROUP BY 
    c.titlu;
GO


Select * from View_AutoriPerCarte


-- View for Profesori
CREATE OR ALTER VIEW View_Autori
AS
SELECT
    a.id,
    a.nume AS NumeAutor,
    a.prenume AS PrenumeAutor,
    a.data_nasterii AS DataNasteriiAutor,
    c.titlu AS TitluCarte,
    c.descriere AS DescriereCarte,
    c.an_aparitie AS AnAparitieCarte
FROM
    Autori a
INNER JOIN
    Carti_Autori ca ON a.id = ca.id_autor
INNER JOIN
    Carti c ON ca.id_carte = c.id
WHERE
    a.id = 1

Select * from View_Autori


SELECT 
    OBJECT_NAME(ius.object_id) AS TableName,
    i.name AS IndexName,
    ius.user_seeks,
    ius.user_scans
FROM 
    sys.dm_db_index_usage_stats ius
    INNER JOIN sys.indexes i ON ius.object_id = i.object_id AND ius.index_id = i.index_id
WHERE 
    OBJECTPROPERTY(ius.object_id, 'IsUserTable') = 1
    AND ius.database_id = DB_ID('Biblioteca') 
    AND (
        OBJECT_NAME(ius.object_id) = 'Autori' OR
        OBJECT_NAME(ius.object_id) = 'Carti' OR
        OBJECT_NAME(ius.object_id) = 'Carti_Autori'
    )
ORDER BY 
    TableName, IndexName;
