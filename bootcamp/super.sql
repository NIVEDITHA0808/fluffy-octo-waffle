CREATE TABLE heroes(
              id serial PRIMARY KEY,
              name VARCHAR(100) NOT NULL,
              gender VARCHAR(20) NOT NULL
);

SELECT * FROM heroes;

DROP TABLE heroes;

