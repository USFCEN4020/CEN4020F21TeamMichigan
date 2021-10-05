# inCollege

For the inCollege app from team Michigan

\*To use inCollege run
python inCollege.py

\*We're using postgresql
Create database type:
CREATE DATABASE incollege;

Please note: (host='localhost', port='5432', database='incollege', user='postgres', password='3600'), thanks.

Queries to create required tables:
CREATE TABLE auth (username VARCHAR(50) PRIMARY KEY, password VARCHAR(50) NOT NULL, first_name VARCHAR(50) NOT NULL, last_name VARCHAR(50) NOT NULL);

CREATE TABLE jobs (id SERIAL PRIMARY KEY, title VARCHAR(50) NOT NULL, description VARCHAR(255) NOT NULL, employer VARCHAR(50) NOT NULL, location VARCHAR(50) NOT NULL, name VARCHAR(50) NOT NULL, salary REAL);

CREATE TABLE control (username VARCHAR(50) PRIMARY KEY REFERENCES auth(username), email boolean, sms boolean , advertising boolean, language VARCHAR(20));

CREATE TABLE profile (username VARCHAR(50) PRIMARY KEY REFERENCES auth (username), title TEXT, major VARCHAR(70), university VARCHAR(70), about TEXT);

CREATE TABLE experiences (username VARCHAR(50) PRIMARY KEY REFERENCES auth (username), title VARCHAR(70), employer VARCHAR(70), date_started DATE, date_ended DATE, location VARCHAR(70), description TEXT);

CREATE TABLE education (username VARCHAR(50) PRIMARY KEY REFERENCES auth (username), school VARCHAR(70), degree VARCHAR(70), year_attended SMALLINT);

\*To set up your python 3 environment with the necessary libraries you'll need to install the packages in the requirements.txt
just look up 'psycopg2 install [inset your os]'
