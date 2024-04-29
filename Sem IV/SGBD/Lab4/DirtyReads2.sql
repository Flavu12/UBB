--Tranzactia 2
SET TRANSACTION ISOLATION LEVEL READ UNCOMMITTED; --COMMITED
BEGIN TRAN
Select * FROM Carti
COMMIT TRAN

--A doua Tranzactie a citit date necomise(dirty reads)