# inCollege

For the inCollege app from team Michigan

\*To use inCollege run
python inCollege.py

\*We're using postgresql
Create database type:
CREATE DATABASE incollege;

Please note: (host='localhost', port='5432', database='incollege', user='postgres', password='3600'), thanks.

Create table for users type:
CREATE TABLE auth (username VARCHAR(50) PRIMARY KEY, password VARCHAR(50) NOT NULL, first_name VARCHAR(50) NOT NULL, last_name VARCHAR(50) NOT NULL);

CREATE TABLE jobs (id SERIAL PRIMARY KEY, title VARCHAR(50) NOT NULL, description VARCHAR(255) NOT NULL, employer VARCHAR(50) NOT NULL, location VARCHAR(50) NOT NULL, name VARCHAR(50) NOT NULL, salary REAL);

CREATE TABLE control (username VARCHAR(50) PRIMARY KEY REFERENCES auth(username), email boolean, sms boolean , advertising boolean, language VARCHAR(20 );

\*To set up your python 3 environment with the necessary libraries you'll need to install the packages in the requirements.txt
just look up 'psycopg2 install [inset your os]'
