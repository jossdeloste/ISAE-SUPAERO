SELECT pays
FROM
(SELECT paysl as pays FROM match WHERE paysv = 'France'
 UNION
 SELECT paysv as pays FROM match WHERE paysl = 'France') AS R;
