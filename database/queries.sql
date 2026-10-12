
SELECT table_name FROM user_tables;


SELECT AVG(Βαθμός) as Μέσος_Όρος
FROM ΒΑΘΜΟΛΟΓΙΑ
WHERE Κωδικός_μαθ = 'CS101';



SELECT * FROM ΦΟΙΤΗΤΗΣ 
WHERE Έτος_εισ BETWEEN 1990 AND 2020;

SELECT * FROM ΜΑΘΗΜΑ
WHERE Τύπος = 'Υποχρεωτικό';


SELECT * FROM ΦΟΙΤΗΤΗΣ
ORDER BY Επώνυμο ASC;


SELECT * FROM ΜΑΘΗΜΑ
WHERE Τύπος = 'Επιλογής';