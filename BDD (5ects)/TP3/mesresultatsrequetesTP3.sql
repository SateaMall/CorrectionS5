/*
USAGE :
Penser à remplir les champs Numéro carte, nom, prénom, date.

Utiliser ce fichier pour répondre aux différentes questions. 
Pour chaque requete vous avez le résultat que vous devez obtenir avec les données de la base BIBLIOTHEQUE.

Les requêtes sont affichées

Si vous ne voulez pas afficher à chaque fois vos requêtes vous pouvez les mettre en commentaire. 
Attention sous ORACLE pour les marques des commentaires (le slash et l'étoile) doivent être seuls sur une ligne.

*/


/*
Numéro de carte étudiant : 
Nom : 
Prénom : 
Date : 
*/

/*
Mise en page - Ne pas toucher
*/

CLEAR SCREEN
SET PAGESIZE 30
COLUMN COLUMN_NAME FORMAT A30
SET LINESIZE 300


prompt --- Q3 : modification de la relation mot_clefs

ALTER TABLE MOT_CLEF ADD MOTPARENT VARCHAR(16) REFERENCES MOT_CLEF(MOT);

/*
Table modifiee.
*/

prompt --- Q4 : ajout de la date de naissance des abonnés, du type parmi  {‘ADULTE’, ‘ENFANT}) et de leur catégorie dont les valeurs admissibles sont : {‘REGULIER’, ‘OCCASIONNEL’, ‘A PROBLEME’, ‘EXCLU’}.

ALTER TABLE ABONNE ADD DATE_NAI DATE;
ALTER TABLE ABONNE ADD TYPE_AB VARCHAR(6) CHECK (TYPE_AB IN ('ADULTE','ENFANT'));
ALTER TABLE ABONNE ADD CAT_AB VARCHAR(12) CHECK (CAT_AB IN ('REGULIER', 'OCCASIONNEL', 'A PROBLEME', 'EXCLU'));

/*
Table modifiee.
*/
         
prompt --- Q4 : describe

DESCRIBE ABONNE;

/*
Exemple de résultat obtenu en fonction des types retenuss
Nom		NULL ?		Type
--------------------------------------------------
NUM_AB 	NOT NULL 	NUMBER(6)
 NOM		NOT NULCOLUMN AGE TO DATE_NAI;NUMBER(3)
 DATE_NAI			DATE
 TYPE_AB			VARCHAR2(6)
 CAT_AB 			VARCHAR2(12)
*/

prompt -- Q4 : mises à jour qui violent la contrainte

UPDATE ABONNE
SET CAT_AB = 'AAAAAAAAAAAAAAAAAAA'
WHERE NUM_AB = 901001;


/*
Exemples d'erreurs obtenues :
ERREUR a la ligne 1 :
ORA-02290: violation de contraintes (P00000008868.DOM_CAT_AB) de verification

ORA-12899: valeur trop grande pour la colonne "P00000008868"."ABONNE"."TYPE_AB" (reelle : 8, maximum
 : 6)

*/

prompt --- Q5 - Augmentation de la taille des noms

ALTER TABLE ABONNE MODIFY NOM VARCHAR(20);

/*
Table modifiee.
*/

prompt --- Q5 - Verification que la taille des noms a bien été prise en compte

DESCRIBE ABONNE;

/*
Par rapport à la version précédente, le type de NOM a bien été modifié
Nom			NULL ?		Type
 -----------------------------------------------------
 NUM_AB 		NOT NULL 	NUMBER(6)
 NOM			NOT NULL 	VARCHAR2(20)
 PRENOM 				VARCHAR2(20)
 VILLE					VARCHAR2(13)
 AGE					NUMBER(3)
 TARIF					NUMBER(3)
 REDUC					NUMBER(3)
 DATE_NAI				DATE
 TYPE_AB				VARCHAR2(6)
 CAT_AB 				VARCHAR2(12)
*/

prompt --- Q6 - Ajout des auteurs dans la base

CREATE TABLE AUTEUR (
	ID_AUT NUMERIC(6,0),
	NOM VARCHAR(20), 
	PRENOM VARCHAR(20),
	NATIONALITE VARCHAR(16),
	CONSTRAINT AUTEURPK PRIMARY KEY (ID_AUT));

CREATE TABLE ECRIT (
	ID_AUT NUMERIC(6,0) REFERENCES AUTEUR(ID_AUT),
	ISBN VARCHAR(15) REFERENCES LIVRE(ISBN), 
	CONSTRAINT ECRITPK PRIMARY KEY (ID_AUT,ISBN));

/*
Table creee.


Table creee.
*/

prompt --- Q7 - Ajout de données dans le thésaurus

INSERT INTO MOT_CLEF VALUES ('INDEX', NULL);
UPDATE MOT_CLEF SET MOTPARENT = 'INDEX' where MOT = 'LITTERATURE';
UPDATE MOT_CLEF SET MOTPARENT = 'LITTERATURE' where MOT = 'POESIE';
UPDATE MOT_CLEF SET MOTPARENT = 'LITTERATURE' where MOT = 'ROMAN';
UPDATE MOT_CLEF SET MOTPARENT = 'LITTERATURE' where MOT = 'ESSAI';
UPDATE MOT_CLEF SET MOTPARENT = 'LITTERATURE' where MOT = 'NOUVELLE';
UPDATE MOT_CLEF SET MOTPARENT = 'INDEX' where MOT = 'MEDECINE';
UPDATE MOT_CLEF SET MOTPARENT = 'INDEX' where MOT = 'SCIENCES';
UPDATE MOT_CLEF SET MOTPARENT = 'INDEX' where MOT = 'HISTOIRE';
UPDATE MOT_CLEF SET MOTPARENT = 'SCIENCES' where MOT = 'INFORMATIQUE';
UPDATE MOT_CLEF SET MOTPARENT = 'INFORMATIQUE' where MOT = 'BASES DE DONNEES';
UPDATE MOT_CLEF SET MOTPARENT = 'BASES DE DONNEES' where MOT = 'SQL';

/* 
Il faut au préalable insérer un tuple avec
INSERT INTO MOT_CLEF VALUES ('INDEX', NULL);

1 ligne modifiée.
*/

prompt --- Q8 - Creation des dates de naissances et du type d'abonné

UPDATE ABONNE SET DATE_NAI = (SELECT SYSDATE - (AGE * 356) FROM DUAL);
UPDATE ABONNE SET TYPE_AB = 'ADULTE' WHERE AGE >= 18;
UPDATE ABONNE SET TYPE_AB = 'ENFANT' WHERE AGE < 18;

/*
11 lignes mises a jour.


7 lignes mises a jour.
*/

prompt --- Q9 - Insertion d'auteurs 

INSERT INTO AUTEUR VALUES (101,'DUMAS','ALEXANDRE','FRANCAISE'); 
INSERT INTO AUTEUR VALUES (102,'SARTRE','JEAN-PAUL','FRANCAISE'); 
INSERT INTO AUTEUR VALUES (103,'GENEY','JEAN','FRANCAISE');
INSERT INTO AUTEUR VALUES (104,'VALLES','JULES','FRANCAISE');
INSERT INTO AUTEUR VALUES (105,'VILLON','FRANCOIS','FRANCAISE'); 
INSERT INTO AUTEUR VALUES (106,'ECO','UMBERTO','ITALIENNE');
INSERT INTO AUTEUR VALUES (107,'GARY','ROMAIN','FRANCAISE');
INSERT INTO AUTEUR VALUES (108,'ROCHEFORT','CHRISTIANE','FRANCAISE'); 
INSERT INTO AUTEUR VALUES (109,'STEINBECK','JOHN','AMERICAIN'); 
INSERT INTO AUTEUR VALUES (110,'HOFSTADTER','DOUGLAS','ALLEMAND'); 
INSERT INTO AUTEUR VALUES (111,'BOUZEGHOUB','MOKRANE','TUNISIENNE'); 
INSERT INTO AUTEUR VALUES (112,'GARDARIN','GEORGES','FRANCAISE');
INSERT INTO AUTEUR VALUES (113,'VALDURIEZ','PATRICK','FRANCAISE'); 
INSERT INTO AUTEUR VALUES (114,'ULLMAN','JEFFREY','AMERICAINE'); 
INSERT INTO AUTEUR VALUES (115,'DELOBEL','CLAUDE','FRANCAISE'); 
INSERT INTO AUTEUR VALUES (116,'DATE','JC','AMERICAINE');
INSERT INTO AUTEUR VALUES (117,'GELENBE','EROL','INDIENNE'); 
INSERT INTO AUTEUR VALUES (118,'FLORY','ANDRE','FRANCAISE');
INSERT INTO ECRIT VALUES (102,'1_104_1050_2'); 
INSERT INTO ECRIT VALUES (103,'0_15_270500_3'); 
INSERT INTO ECRIT VALUES (104,'0_85_4107_3'); 
INSERT INTO ECRIT VALUES (105,'0_112_3785_5'); 
INSERT INTO ECRIT VALUES (116,'0_201_14439_5'); 
INSERT INTO ECRIT VALUES (112,'0_12_27550_2'); 
INSERT INTO ECRIT VALUES (117,'0_12_27550_2'); 
INSERT INTO ECRIT VALUES (111,'0_8_7707_2'); 
INSERT INTO ECRIT VALUES (118,'0_8_7707_2'); 
INSERT INTO ECRIT VALUES (106,'1_22_1721_3'); 
INSERT INTO ECRIT VALUES (107,'3_505_13700_5'); 
INSERT INTO ECRIT VALUES (108,'0_18_47892_2'); 
INSERT INTO ECRIT VALUES (109,'9_782070_36'); 
INSERT INTO ECRIT VALUES (110,'2_7296_0040'); 
INSERT INTO ECRIT VALUES (111,'0_26_28079_6'); 
INSERT INTO ECRIT VALUES (112,'0_26_28079_6'); 
INSERT INTO ECRIT VALUES (113,'0_26_28079_6');

/*
1 ligne créee.

autant de fois qu'il y a d'insertion
*/

prompt --- Q10 - Quels sont les différents propriétaires des tables ? 

select distinct  owner from all_tables;

/*
La dernière valeur correspond à votre identifiant UNIX.
----------------------------------------------------------------------------------------------------
----------------------------
SYSTEM
AUDSYS
XDB
SYS
P00000008868
*/


prompt --- Q11 - Quels sont les noms de tous les attributs de la relation ABONNE ?

select column_name from user_tab_columns where table_name = 'ABONNE';

/*
COLUMN_NAME
------------------------------
NUM_AB
NOM
PRENOM
VILLE
AGE
TARIF
REDUC
DATE_NAI
TYPE_AB
CAT_AB

10 lignes selectionnees.
*/

prompt --- Q12 - Quel est le nombre d'attributs définis dans la BD BIBLIO ?

select count(*) from user_tab_columns;


prompt --- Q13 - Quelles sont toutes les contraintes d'intégrité définies sur les relations de données de la base BIBLIO ?

select CONSTRAINT_NAME, TABLE_NAME  from USER_CONSTRAINTS where CONSTRAINT_NAME like '%PK';


prompt --- Q14 - Création de la relation TESTINDEX

/*
VOTRE REPONSE ICI
*/

/*
Table créée.
*/
prompt --- Q14 - Création de l'index

/*
VOTRE REPONSE ICI
*/


/*
Index créé.
*/

prompt --- Q14 - Essai de deux insertions

/*
VOTRE REPONSE ICI
*/

/*
Les valeurs peuvent changer :
1 ligne creee.

.......

*
ERREUR a la ligne 1 :
ORA-00001: violation de contrainte unique (P00000008868.CLE_TESTINDEX)
*/

prompt --- Q14 - Affichage de l'index dans les tables systèmes


/*
VOTRE REPONSE ICI
*/

/*
INDEX_NAME		INDEX_TYPE
-----------------------------------
CLE_TESTINDEX		NORMAL
*/


prompt --- Q15 - Existe-t-il, dans la base BIBLIO, une relation pour laquelle aucun index n’a été spécifié ?

/*
VOTRE REPONSE ICI
*/

/*
aucune ligne selectionnee
*/


prompt --- Q16 - Création vue ABONNE_MONTP


create view ABONNE_MONTP AS (SELECT NUM_AB,NOM, PRENOM FROM ABONNE WHERE VILLE = 'MONTPELLIER');
INSERT INTO ABONNE_MONTP VALUES (988888,'PAUL','OUI');


/*
Vue creee.
*/

prompt --- Q16 - Insertion d'un tuple dans la vue

/*
VOTRE REPONSE ICI
*/

/*
1 ligne creee.
*/

prompt --- Q16 - Visualisation d'abonne

/*
VOTRE REPONSE ICI
*/

/*
    NUM_AB NOM			PRENOM		     VILLE		  AGE
---------- -------------------- -------------------- ------------- ----------
     TARIF	REDUC DATE_NAI	 TYPE_A CAT_AB
---------- ---------- ---------- ------ ------------
.....
950001	  FAURE

12 lignes sélectionnées.
*/
...

prompt --- Q17 : Vérifier que la vue a bien été créée dans les tables systèmes.

/*
VOTRE REPONSE ICI
*/

/*
VIEW_NAME
--------------------------------------------------------------------------------
ABONNE_MONTP
*/

prompt --- Q18 - vue ETAT_ETAT EXEMPLAIRE

/*
VOTRE REPONSE ICI
*/

/*
Vue créée.
*/

prompt --- Q18 - tentative d'insertion dans la vue d'un tuple erroné

/*
VOTRE REPONSE ICI
*/

/*
INSERT INTO ...
            *
ERREUR a la ligne 1 :
ORA-01402: vue WITH CHECK OPTION - violation de clause WHERE
*/

prompt --- Q19 - Creation de la vue EMP

/*
VOTRE REPONSE ICI
*/

/*
Vue créée.
*/

prompt --- Q20 - Test d'une inserion invalide

/*
VOTRE REPONSE ICI
*/

 /*
INSERT INTO ...
            *
ERREUR a la ligne 1 :
ORA-01402: vue WITH CHECK OPTION - violation de clause WHERE
*/

