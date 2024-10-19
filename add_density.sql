SET SQL_SAFE_UPDATES = 0;
show tables;
Select * FROM knimeproject.active;
ALTER Table knimeproject.active;
update knimeproject.active
SET Density = 
    CASE 
        WHEN name = 'Ibuprofen' THEN 1030
        WHEN name = 'PBSA – Ensulizole ' THEN 1500
        WHEN name = 'Nicotinamide' THEN 1181
        WHEN name = 'biochanin A' THEN 1420
        WHEN name = 'Chrysin' THEN 1466
        WHEN name = 'Ensulizole' THEN 1.93E-07
        WHEN name = 'alpha-Ergocryptine' THEN 1433
        WHEN name = 'Tetrandrine' THEN 1173
        WHEN name = 'Conessine' THEN 979
        WHEN name = 'Indirubin' THEN 262263
        WHEN name = 'Caffeic acid' THEN 1421
        WHEN name = 'Lactic acid' THEN 1204
        WHEN name = 'Benzophenone-3' THEN 1201
		WHEN name = 'Naproxen' THEN 1198
		WHEN name = 'Glycolic acid' THEN 1248
		WHEN name = '2-OH-hexanoic acid' THEN 930
		WHEN name = 'Niacinamide' THEN 1205
        ELSE NULL  -- Or default value if no match found
    END;
     
show tables;
Select * FROM knimeproject.active;
