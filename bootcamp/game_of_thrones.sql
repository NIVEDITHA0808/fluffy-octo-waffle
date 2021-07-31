--Create table

CREATE TABLE characters(
           character_id INTEGER PRIMARY KEY AUTOINCREMENT,
           name VARCHAR(20) NOT NULL,
           gender VARCHAR(1)
           aff_id integer references affiliation.id --foreign key
           
);

--Insert Data

INSERT INTO characters (name,gender,aff_id) VALUES('Eddard Stark', 'm',4);
INSERT INTO characters (name,gender,aff_id) VALUES('Jaime Lannister', 'm',1);
INSERT INTO characters (name,gender,aff_id) VALUES('Cersei Lannister', 'f',1);
INSERT INTO characters (name,gender,aff_id) VALUES('Sandor Clegane', 'm',4);       
INSERT INTO characters (name,gender,aff_id) VALUES('Petyr Baelish', 'm',1);


--Get Data
SELECT * FROM characters;

SELECT * FROM characters
WHERE gender ='f';

SELECT * FROM characters
ORDER BY characters.name DESC;

SELECT characters

--Drop table
DROP TABLE characters;

--update data

UPDATE characters
SET gender = 'f'
WHERE name = "Daenerys Targaryenk";
-- to modify table
 -- Alternative way to create foreign key
 
ALTER TABLE characters 
ADD aff_id INT
REFERENCES affiliation(id)
ON DELETE SET NULL;


-- table 2
create table affiliation (
       id integer primary key AUTOINCREMENT,
       name text unique not null,
       location text not null
);


insert into affiliation(name, location) values ('Lannister' , 'Kings Landing');
insert into affiliation(name, location) values ('Nights Watch' , 'Wall');
insert into affiliation(name, location) values('Targaryen' , 'Dragonstone');
insert into affiliation(name, location) values ('Stark'    , 'Winterfell');

select c.name, c.gender, a.name  from characters c, affiliation a where c.aff_id = a.id and a.location = "Winterfell";




