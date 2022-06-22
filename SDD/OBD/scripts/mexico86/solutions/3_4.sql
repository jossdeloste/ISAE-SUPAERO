SELECT groupe, SUM(buts)
FROM (SELECT groupe, (butsl + butsv) AS buts
      FROM pays JOIN (SELECT paysl, butsl, butsv
                      FROM match
                      WHERE type = 'Poule') AS R
                ON (nom = paysl)) AS R
GROUP BY groupe
ORDER BY groupe;
