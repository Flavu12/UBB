BEGIN TRAN
WAITFOR DELAY '00:00:03'
INSERT INTO Tipuri(denumire, descriere) VALUES 
('denumire1', 'descriere1');
COMMIT TRAN