SET SQL_SAFE_UPDATES = 0;
show tables;
Select * FROM knimeproject.active;
ALTER Table knimeproject.active;
#ADD Fu varchar(255);
update knimeproject.active
SET Fu = 
    CASE 
        WHEN name = 'Ibuprofen' THEN 0.01
        WHEN name = 'PBSA – Ensulizole ' THEN -1
        WHEN name = 'Nicotinamide' THEN 0.7198
        WHEN name = 'biochanin A' THEN 0.0259
        WHEN name = 'Chrysin' THEN 0.0204
        WHEN name = 'Ensulizole' THEN 0.0882
        WHEN name = 'alpha-Ergocryptine' THEN 0.1651
        WHEN name = 'Tetrandrine' THEN -1
        WHEN name = 'Conessine' THEN 0.1524
        WHEN name = 'Indirubin' THEN -1
        WHEN name = 'Caffeic acid' THEN 0.3463
        WHEN name = 'Lactic acid' THEN 0.93
        WHEN name = 'Benzophenone-3' THEN 0.0293
		WHEN name = 'Naproxen' THEN 0.002
		WHEN name = 'Glycolic acid' THEN 0.9361
		WHEN name = '2-OH-hexanoic acid' THEN -1
		WHEN name = 'Niacinamide' THEN 0.7198
        ELSE NULL  -- Or default value if no match found
    END;
     
show tables;
Select * FROM knimeproject.active;
