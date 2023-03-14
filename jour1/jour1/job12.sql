INSERT INTO etudiants (id,nom,prenom,age,email)
VALUES(6,"Dupuis","Martin",18,"martin.dupuis@laplateforme.io");

SELECT * FROM etudiants WHERE nom LIKE '%Dupuis%';