DROP FUNCTION vainqueur(VARCHAR(20), VARCHAR(20), VARCHAR(6));

CREATE OR REPLACE FUNCTION vainqueur(equipel VARCHAR(20), equipev VARCHAR(20),
                                     typematch VARCHAR(6))
                  RETURNS VARCHAR(20) AS $vainqueur$
       DECLARE
        butsl INTEGER;
        butsv INTEGER;
       BEGIN
        butsl := match.butsl FROM match WHERE (paysl, paysv, type) =
                                              (equipel, equipev, typematch);
        butsv := match.butsv FROM match WHERE (paysl, paysv, type) =
                                              (equipel, equipev, typematch);

        IF (butsl > butsv) THEN
           RETURN equipel;
        ELSIF (butsl < butsv) THEN
           RETURN equipev;
        ELSE
           RETURN 'Match nul';
        END IF;
       END;
$vainqueur$ LANGUAGE plpgsql;

SELECT * FROM vainqueur('Espagne', 'Danemark', '1/8');
SELECT * FROM vainqueur('Brésil', 'France', '1/4');
