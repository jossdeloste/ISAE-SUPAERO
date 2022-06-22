CREATE VIEW matchbutsglobal AS
(SELECT paysl, paysv, SUM(buts) AS buts, type, date
 FROM ((SELECT paysl, paysv, butsv AS buts, type, date
        FROM match)
       UNION ALL
       (SELECT paysl, paysv, butsl AS buts, type, date
        FROM match)) AS R
 GROUP BY paysl, paysv, type, date);
