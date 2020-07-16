DROP TABLE IF EXISTS sanctioned;

CREATE TABLE sanctioned (
  Individuals TEXT UNIQUE NOT NULL,
  Organizations TEXT UNIQUE NOT NULL,
  Countries TEXT UNIQUE NOT NULL
);