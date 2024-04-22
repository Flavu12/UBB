--functie de validare a textului
CREATE OR ALTER FUNCTION dbo.validare_varchar (@text varchar(50))
RETURNS bit
AS
BEGIN
    DECLARE @flag bit
    SET @flag = 1

	IF @text is null or @text =''
		SET @flag=0;
	RETURN @flag;
END
GO

--functie de validare a unui id
CREATE OR ALTER FUNCTION dbo.validare_id (@id int)
RETURNS bit
AS
BEGIN
    DECLARE @flag bit
    SET @flag = 1

    IF @id IS NULL OR @id <= 0
        SET @flag = 0

    RETURN @flag
END
GO

CREATE OR ALTER FUNCTION dbo.validare_an (@an int)
RETURNS bit
AS
BEGIN
    DECLARE @flag bit
    SET @flag = 1

	IF @an is null or @an > 2024 
		SET @flag=0;
	RETURN @flag;
END
GO


CREATE OR ALTER PROCEDURE AddCarteTip 
	@titlu varchar(30), @descriereC varchar(200), @an_aparitie int, @id_editura int,
	@denumire varchar(30), @descriereT varchar(100) as
begin 
begin tran

	begin try
		-- validari texte
		if dbo.validare_varchar(@titlu) <> 1
			begin 
				raiserror('Titlu invalid',14,1);
			end
		if dbo.validare_varchar(@descriereC) <> 1
			begin 
				raiserror('Descriere Carte invalida',14,1);
			end
		if dbo.validare_varchar(@denumire) <> 1
			begin 
				raiserror('Denumire invalida',14,1);
			end
		if dbo.validare_varchar(@descriereT) <> 1
			begin 
				raiserror('Descriere Tip invalid',14,1);
			end

		-- validare an 
		if dbo.validare_an(@an_aparitie) <> 1
			begin 
				raiserror('An invalid',14,1);
			end

		--validare id
		if dbo.validare_id(@id_editura) <> 1
			begin 
				raiserror('Id invalid',14,1);
			end

		INSERT INTO Carti(titlu, descriere, an_aparitie, id_editura)
		values 
		(@titlu, @descriereC, @an_aparitie, @id_editura);

		print 'Carte adaugata'

		INSERT INTO Tipuri(denumire, descriere)
		values 
		(@denumire, @descriereT);

		print 'Tip adaugat'

		declare @Id_Carte int;
		declare @Id_Tip int;

		SELECT TOP 1 @Id_Carte = C.id
		FROM dbo.Carti as C
		WHERE C.titlu = @titlu;

		SELECT TOP 1 @Id_Tip = T.id
		FROM dbo.Tipuri as T
		WHERE T.denumire = @denumire;

		INSERT INTO Carti_Tipuri
		values 
		(@Id_Carte, @Id_Tip);

		commit tran
		select 'Transaction committed'
	end try

	begin catch
		rollback tran
		print ERROR_MESSAGE(); 
		select 'Transaction rollbacked'
	end catch
end

EXEC AddCarteTip 
    @titlu = 'Harry Potter si Piatra Filozofala',
    @descriereC = 'Prima carte din seria Harry Potter',
    @an_aparitie = 1997,
    @id_editura = 1,
    @denumire = 'Fictiune',
    @descriereT = 'Gen literar de fictiune';

SELECT * FROM Carti;
SELECT * FROM Tipuri;
SELECT * FROM Carti_Tipuri;

EXEC AddCarteTip 
    @titlu = 'Malakai',
    @descriereC = 'O poveste de dragoste',
    @an_aparitie = 3000,  
    @id_editura = 1,
    @denumire = 'Romanitc',
    @descriereT = 'Gen literar romantism';
SELECT * FROM Carti;
SELECT * FROM Tipuri;
SELECT * FROM Carti_Tipuri;
GO
------Prob 2

CREATE OR ALTER PROCEDURE AddCarte 
	@titlu varchar(30), @descriereC varchar(200), @an_aparitie int, @id_editura int as
begin 
begin tran

	begin try
		-- validari texte
		if dbo.validare_varchar(@titlu) <> 1
			begin 
				raiserror('Titlu invalid',14,1);
			end
		if dbo.validare_varchar(@descriereC) <> 1
			begin 
				raiserror('Descriere Carte invalida',14,1);
			end

		-- validare an 
		if dbo.validare_an(@an_aparitie) <> 1
			begin 
				raiserror('An invalid',14,1);
			end

		--validare id
		if dbo.validare_id(@id_editura) <> 1
			begin 
				raiserror('Id invalid',14,1);
			end

		INSERT INTO Carti(titlu, descriere, an_aparitie, id_editura)
		values 
		(@titlu, @descriereC, @an_aparitie, @id_editura);

		print 'Carte adaugata'
commit tran
		print 'Transaction committed'
	end try

	begin catch
		rollback tran
		print ERROR_MESSAGE(); 
		print 'Transaction rollbacked'
		return 0
	end catch
	return 1
end
go

CREATE OR ALTER PROCEDURE AddTip 
	@denumire varchar(30), @descriereT varchar(100) as
begin 
begin tran

	begin try
		-- validari texte
		
		if dbo.validare_varchar(@denumire) <> 1
			begin 
				raiserror('Denumire invalida',14,1);
			end
		if dbo.validare_varchar(@descriereT) <> 1
			begin 
				raiserror('Descriere Tip invalid',14,1);
			end

		INSERT INTO Tipuri(denumire, descriere)
		values 
		(@denumire, @descriereT);

		print 'Tip adaugat'
commit tran
		print 'Transaction committed'
	end try

	begin catch
		rollback tran
		print ERROR_MESSAGE(); 
		print 'Transaction rollbacked'
		return 0
	end catch
	return 1
end
go
CREATE OR ALTER PROCEDURE AddCarteTip2 
	@titlu varchar(30), @descriereC varchar(200), @an_aparitie int, @id_editura int,
	@denumire varchar(30), @descriereT varchar(100) as
begin
		declare @carte_adaugata int;
		declare @tip_adaugat int;

		EXEC @carte_adaugata = AddCarte @titlu, @descriereC, @an_aparitie, @id_editura;
		EXECUTE @tip_adaugat = AddTip @denumire, @descriereT;
		
		if @carte_adaugata <> 1
			begin
				print 'Cartea nu a putut fi adaugata, nu se poate adauga Carti_Tipuri'
				return 0
			end

		if @tip_adaugat <> 1
			begin
			print 'Tipul nu a putut fi adaugat, nu se poate adauga Carti_Tipuri'
				return 0
			end

		declare @Id_Carte int;
		declare @Id_Tip int;

		SELECT TOP 1 @Id_Carte = C.id
		FROM dbo.Carti as C
		WHERE C.titlu = @titlu;

		SELECT TOP 1 @Id_Tip = T.id
		FROM dbo.Tipuri as T
		WHERE T.denumire = @denumire;

		INSERT INTO Carti_Tipuri
		values 
		(@Id_Carte, @Id_Tip);
end

EXEC AddCarteTip2 
    @titlu = 'Gandeste-te la un numar',
    @descriereC = 'O carte despre un detectiv',
    @an_aparitie = 2010,
    @id_editura = 1,
    @denumire = 'Politist',
    @descriereT = 'crime si rezolvari de cazuri';

SELECT * FROM Carti;
SELECT * FROM Tipuri;
SELECT * FROM Carti_Tipuri;

EXEC AddCarteTip2 
    @titlu = 'Malakai',
    @descriereC = 'O poveste de dragoste',
    @an_aparitie = 3000,  
    @id_editura = 1,
    @denumire = 'Romantic',
    @descriereT = 'Gen literar romantism';
SELECT * FROM Carti;
SELECT * FROM Tipuri;
SELECT * FROM Carti_Tipuri;

EXEC AddCarteTip2 
    @titlu = 'Pacatul meu',
    @descriereC = 'O poveste dramatica',
    @an_aparitie = 2020,  
    @id_editura = 1,
    @denumire = '',
    @descriereT = 'drame adolescentine';
SELECT * FROM Carti;
SELECT * FROM Tipuri;
SELECT * FROM Carti_Tipuri;

DBCC LOG(Biblioteca, 0);