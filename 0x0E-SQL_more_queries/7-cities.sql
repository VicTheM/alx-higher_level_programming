-- creates DB, TABLE, PK and adds constraints

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

CREATE TABLE IF NOT EXISTS cities (
	id INT PRIMARY KEY,
	state_id INT FOREIGN KEY(state_id) REFERENCES states(id),
	name VARCHAR(256) NOT NULL
	);
