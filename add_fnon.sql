SET SQL_SAFE_UPDATES = 0;
show tables;
Select * FROM knimeproject.active;
ALTER Table knimeproject.active;
#ADD Fnon varchar(255);
update knimeproject.active
SET Fnon = 
    CASE 
        WHEN name = 'Ibuprofen' THEN 0.0081
        WHEN name = 'PBSA – Ensulizole ' THEN -1
        WHEN name = 'Nicotinamide' THEN 0.9998
        WHEN name = 'biochanin A' THEN 0.9837
        WHEN name = 'Chrysin' THEN 0.4145
        WHEN name = 'Ensulizole' THEN 0.0053
        WHEN name = 'alpha-Ergocryptine' THEN 0.7721
        WHEN name = 'Tetrandrine' THEN -1
        WHEN name = 'Conessine' THEN 0.000213
        WHEN name = 'Indirubin' THEN -1
        WHEN name = 'Caffeic acid' THEN 0.0019
        WHEN name = 'Lactic acid' THEN 0.00078
        WHEN name = 'Benzophenone-3' THEN 0.9943
		WHEN name = 'Naproxen' THEN 0.0099
		WHEN name = 'Glycolic acid' THEN 0.0013
		WHEN name = '2-OH-hexanoic acid' THEN -1
		WHEN name = 'Niacinamide' THEN 0.9998
        ELSE NULL  -- Or default value if no match found
    END;
     
show tables;
Select * FROM knimeproject.active;
