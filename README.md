# inCollege

For the inCollege app from team Michigan

\*To use inCollege run
python inCollege.py

\*We're using postgresql
Create database type:
CREATE DATABASE incollege;

Please note: (host='localhost', port='5432', database='incollege', user='postgres', password='3600'), thanks.

\*To set up your python 3 environment with the necessary libraries you'll need to install the packages in the requirements.txt
just look up 'psycopg2 install [inset your os]'

list of all tables in the database with column names:
    auth:
        username, password, first_name, last_name
    control:
        username, email, sms, advertising, language
    experiences:
        username, title, employer, date_started, date_ended, location, description
    education:
        username, school, degree, year_attended
