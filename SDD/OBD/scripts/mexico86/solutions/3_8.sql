SELECT pays, total
FROM (SELECT (butsparequipe(nom)).pays, (butsparequipe(nom)).total
      FROM pays) AS R1
WHERE total = (SELECT MAX(total)
               FROM (SELECT (butsparequipe(nom)).pays, (butsparequipe(nom)).total
                     FROM pays) AS R2);
