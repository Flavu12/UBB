BEGIN TRAN
SELECT * FROM Tipuri where id BETWEEN 1 AND 100;
WAITFOR DELAY '00:00:06'
SELECT * FROM Tipuri where id BETWEEN 1 AND 100;
COMMIT TRAN
--In aceeasi tranzactie, o interogare care specifica un interval de valori
--in clauza where a fost executata de doua ori si numarul de inregistrari
--incluse in cel de-al doilea result set este mai mare decat numarul de 
--inregistrari incluse in primul result set