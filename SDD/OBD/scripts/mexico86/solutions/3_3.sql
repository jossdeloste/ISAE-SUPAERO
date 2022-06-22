SELECT SUM(buts) AS buts
FROM ((SELECT butsl AS buts
       FROM match
       WHERE paysl = 'France')
      UNION ALL
      (SELECT butsv AS buts
       FROM match
       WHERE paysv = 'France')) AS R;
