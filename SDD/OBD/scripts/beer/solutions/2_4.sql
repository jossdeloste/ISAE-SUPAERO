SELECT *
FROM (SELECT buveur FROM Frequente
      EXCEPT
      SELECT DISTINCT buveur FROM (Sert NATURAL JOIN Aime) NATURAL JOIN Frequente
     ) AS R;
