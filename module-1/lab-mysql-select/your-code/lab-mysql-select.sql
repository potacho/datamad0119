#[lab-mysql-select]octavio

#Descargo fichero 'publications.sql'
#Importo datos utilizando el wizard de Workbench: Administration → Data Import/Restore → Import from Self-Contained File → Select File → Default Target Schema → Start Import

USE publications;



#Challenge 1 - Who Have Published What At Where?

#Sin usar INNER JOIN
SELECT 
authors.au_id AS 'Author ID', 
authors.au_lname AS 'Last Name', 
authors.au_fname AS 'First Name', 
titles.title AS 'Book Title', 
publishers.pub_name AS 'Book Publisher'
FROM authors, titles, titleauthor, publishers 
WHERE titles.title_id=titleauthor.title_id 
AND titleauthor.au_id=authors.au_id AND titles.pub_id=publishers.pub_id;

#Usando INNER JOIN
SELECT 
authors.au_id AS 'Author ID', 
authors.au_lname AS 'Last Name', 
authors.au_fname AS 'First Name', 
titles.title AS 'Book Title', 
publishers.pub_name AS 'Book Publisher'
FROM authors
INNER JOIN titleauthor ON authors.au_id = titleauthor.au_id
INNER JOIN titles ON titleauthor.title_id = titles.title_id
INNER JOIN publishers ON titles.pub_id = publishers.pub_id;



#Challenge 2 - Who Have Published How Many At Where?

#Sin usar INNER JOIN
SELECT 
authors.au_id AS 'Author ID', 
authors.au_lname AS 'Last Name', 
authors.au_fname AS 'First Name', 
ANY_VALUE(publishers.pub_name) AS 'Book Publisher', 
COUNT(titleauthor.au_id) AS 'Number of Titles'
FROM authors, titleauthor, titles, publishers 
WHERE titles.title_id=titleauthor.title_id 
AND titleauthor.au_id=authors.au_id AND titles.pub_id=publishers.pub_id
GROUP BY authors.au_id;

#Usando INNER JOIN
SELECT
authors.au_id AS 'Author ID', 
authors.au_lname AS 'Last Name', 
authors.au_fname AS 'First Name', 
publishers.pub_name AS 'Book Publisher',
COUNT(titleauthor.au_id) AS 'Number of Titles'
FROM authors
INNER JOIN titleauthor ON authors.au_id = titleauthor.au_id
INNER JOIN titles ON titleauthor.title_id = titles.title_id
INNER JOIN publishers ON titles.pub_id = publishers.pub_id
GROUP BY authors.au_id, authors.au_fname, authors.au_lname, publishers.pub_name;



#Challenge 3 - Best Selling Authors



#Challenge 4 - Best Selling Authors Ranking



#Bonus Challenge - Most Profiting Authors

