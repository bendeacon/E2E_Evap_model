SET SQL_SAFE_UPDATES = 0;
show tables;
Select * FROM knimeproject.active;
ALTER Table knimeproject.active;
update knimeproject.active
SET vapour_pressure = 
    CASE 
        WHEN name = 'Ibuprofen' THEN 0.006266152
        WHEN name = 'PBSA – Ensulizole ' THEN 1.33
        WHEN name = 'Nicotinamide' THEN 1.49321074
        WHEN name = 'biochanin A' THEN 2.21E-07
        WHEN name = 'Chrysin' THEN 3.63E-07
        WHEN name = 'Ensulizole' THEN 1.93E-07
        WHEN name = 'alpha-Ergocryptine' THEN 2.91E-06
        WHEN name = 'Tetrandrine' THEN 3.69E-08
        WHEN name = 'Conessine' THEN 1.14E-05
        WHEN name = 'Indirubin' THEN 4.52E-07
        WHEN name = 'Caffeic acid' THEN 0.000323973
        WHEN name = 'Lactic acid' THEN 10.83911
        WHEN name = 'Benzophenone-3' THEN 0.000249313
		WHEN name = 'Naproxen' THEN 3.16E-05
		WHEN name = 'Glycolic acid' THEN 2.66645
		WHEN name = '2-OH-hexanoic acid' THEN 5.799524
		WHEN name = 'Niacinamide' THEN 1.24E-02
        ELSE NULL  -- Or default value if no match found
    END;
     
show tables;
Select * FROM knimeproject.active;
