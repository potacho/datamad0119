#Lab | Advanced MySQL

#Challenge 1 - Most Profiting Authors

#STEP 1: Generación de la sub-query con title_id, au_id y los ingresos por registro. 
"""
SELECT
	tit.title_id AS titID_1,
	aut.au_id AS autID_1, 
	(tit.price * sal.qty * tit.royalty / 100 * tau.royaltyper / 100) AS prof_1
FROM authors AS aut
	INNER JOIN titleauthor AS tau ON aut.au_id = tau.au_id
	INNER JOIN titles AS tit ON tau.title_id = tit.title_id
	INNER JOIN sales AS sal ON sal.title_id = tit.title_id);
#GROUP BY (NO APLICA EN ESTE NIVEL)
"""

#STEP 2: Generación de la sub-query con title_id, au_id y la suma de los ingresos por autor. 
"""
SELECT
	STEP_1.titID_1 AS titID_2,
	STEP_1.autID_1 AS autID_2, 
	SUM(STEP_1.prof_1) AS sum_prof_1
FROM (
	SELECT
		tit.title_id AS titID_1,
		aut.au_id AS autID_1, 
		(tit.price * sal.qty * tit.royalty / 100 * tau.royaltyper / 100) AS prof_1
	FROM authors AS aut
		INNER JOIN titleauthor AS tau ON aut.au_id = tau.au_id
		INNER JOIN titles AS tit ON tau.title_id = tit.title_id
		INNER JOIN sales AS sal ON sal.title_id = tit.title_id) 
    #GROUP BY (NO APLICA EN ESTE NIVEL)
    AS STEP_1
GROUP BY autID_1, titID_1; ###Asi me funciona pero no entiendo porque no me vale solo haciendo el GROUP BY autID_1?###
"""

#STEP 3: Query definitva con au_id y la suma de los ingresos por autor incluyendo todos los titulos x autor.
SELECT
	DISTINCT(STEP_2.autID_2) AS 'Author ID', 
    STEP_2.sum_prof_1 AS 'Profit'
FROM (
	SELECT
		STEP_1.titID_1 AS titID_2,
		STEP_1.autID_1 AS autID_2, 
		SUM(STEP_1.prof_1) AS sum_prof_1
	FROM (
		SELECT
		    tit.title_id AS titID_1,
		    aut.au_id AS autID_1, 
		    (tit.price * sal.qty * tit.royalty / 100 * tau.royaltyper / 100) AS prof_1
		FROM authors AS aut
		    INNER JOIN titleauthor AS tau ON aut.au_id = tau.au_id
		    INNER JOIN titles AS tit ON tau.title_id = tit.title_id
		    INNER JOIN sales AS sal ON sal.title_id = tit.title_id) 
        #GROUP BY (NO APLICA EN ESTE NIVEL)
        AS STEP_1
	GROUP BY autID_1, titID_1) 
    AS STEP_2
GROUP BY STEP_2.autID_2, STEP_2.sum_prof_1
ORDER BY STEP_2.sum_prof_1 DESC
LIMIT 3;



#Challenge 2 - Alternative Solution

#Se crea la sub-tabla STEP_1:
CREATE TEMPORARY TABLE STEP_1
SELECT
	tit.title_id AS titID_1,
	aut.au_id AS autID_1, 
	(tit.price * sal.qty * tit.royalty / 100 * tau.royaltyper / 100) AS prof_1
FROM authors AS aut
	INNER JOIN titleauthor AS tau ON aut.au_id = tau.au_id
	INNER JOIN titles AS tit ON tau.title_id = tit.title_id
	INNER JOIN sales AS sal ON sal.title_id = tit.title_id;

#Se crea la sub-tabla STEP_2:
CREATE TEMPORARY TABLE STEP_2
SELECT
	STEP_1.titID_1 AS titID_2,
	STEP_1.autID_1 AS autID_2, 
	SUM(STEP_1.prof_1) AS sum_prof_1
FROM STEP_1
GROUP BY autID_1, titID_1;

#Se hace la query final sobre la tabla temporal STEP_2.
SELECT
	DISTINCT(STEP_2.autID_2) AS 'Author ID', 
    STEP_2.sum_prof_1 AS 'Profit'
FROM STEP_2
GROUP BY STEP_2.autID_2, STEP_2.sum_prof_1
ORDER BY STEP_2.sum_prof_1 DESC
LIMIT 3;



#Challenge 3 - Creación de la tabla 'most_profiting_authors'
CREATE TABLE most_profiting_authors
SELECT
	DISTINCT(STEP_2.autID_2) AS 'Author ID', 
    STEP_2.sum_prof_1 AS 'Profit'
FROM (
	SELECT
		STEP_1.titID_1 AS titID_2,
		STEP_1.autID_1 AS autID_2, 
		SUM(STEP_1.prof_1) AS sum_prof_1
	FROM (
		SELECT
		    tit.title_id AS titID_1,
		    aut.au_id AS autID_1, 
		    (tit.price * sal.qty * tit.royalty / 100 * tau.royaltyper / 100) AS prof_1
		FROM authors AS aut
		    INNER JOIN titleauthor AS tau ON aut.au_id = tau.au_id
		    INNER JOIN titles AS tit ON tau.title_id = tit.title_id
		    INNER JOIN sales AS sal ON sal.title_id = tit.title_id) 
        #GROUP BY (NO APLICA EN ESTE NIVEL)
        AS STEP_1
	GROUP BY autID_1, titID_1) 
    AS STEP_2
GROUP BY STEP_2.autID_2, STEP_2.sum_prof_1
ORDER BY STEP_2.sum_prof_1 DESC;

