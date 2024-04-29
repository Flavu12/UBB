--Tranzactia 1
BEGIN TRAN
UPDATE Carti SET titlu='DirtyReads' where id = 3
WAITFOR DELAY '00:00:07'
ROLLBACK TRAN;