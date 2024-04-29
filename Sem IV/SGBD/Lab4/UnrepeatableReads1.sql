--Tranzactia 1
BEGIN TRAN
SELECT * FROM Carti
WAITFOR DELAY '00:00:06'
SELECT * FROM Carti
COMMIT TRAN

--Aceeasi interogare executata de 2 ori in aceeasi tranzactie 
--a returnat doua valori diferite pentru aceeasi inregistrare