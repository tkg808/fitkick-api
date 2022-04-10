-- Allows resetting the database.
DROP DATABASE IF EXISTS fitkick;
DROP USER IF EXISTS fitkickuser;

CREATE DATABASE fitkick;
CREATE USER fitkickuser WITH PASSWORD 'fitkick';
GRANT ALL PRIVILEGES ON DATABASE fitkick TO fitkickuser;