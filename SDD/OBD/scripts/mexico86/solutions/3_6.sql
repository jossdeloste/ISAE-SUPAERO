DROP FUNCTION butsparequipe(VARCHAR(20));

CREATE OR REPLACE FUNCTION butsparequipe(equipe VARCHAR(20))
                  RETURNS TABLE(total BIGINT, moyenne NUMERIC) AS $butsparequipe$
       BEGIN
        RETURN QUERY SELECT SUM(buts), AVG(buts)
                     FROM ((SELECT butsl AS buts FROM match WHERE (paysl = equipe))
                           UNION ALL
                           (SELECT butsv AS buts FROM match WHERE (paysv = equipe))
                          ) AS R;
       END;
$butsparequipe$ LANGUAGE plpgsql;

SELECT * FROM butsparequipe('France');

DROP FUNCTION butsparequipe(VARCHAR(20));

CREATE OR REPLACE FUNCTION butsparequipe(equipe VARCHAR(20))
                  RETURNS TABLE(pays VARCHAR(20), total BIGINT, moyenne NUMERIC)
                  AS $butsparequipe$
       BEGIN
        RETURN QUERY SELECT equipe as pays, SUM(buts), AVG(buts)
                     FROM ((SELECT butsl AS buts FROM match WHERE (paysl = equipe))
                           UNION ALL
                           (SELECT butsv AS buts FROM match WHERE (paysv = equipe))
                          ) AS R;
       END;
$butsparequipe$ LANGUAGE plpgsql;

SELECT * FROM butsparequipe('France');
