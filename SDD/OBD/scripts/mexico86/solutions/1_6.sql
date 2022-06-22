SELECT pays
FROM
(SELECT paysl AS pays FROM match WHERE butsl > butsv AND type = 'Finale'
 UNION
 SELECT paysv AS PAYS FROM match WHERE butsv > butsl AND type = 'Finale') AS R;
