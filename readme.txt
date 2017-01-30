				README
------------------------------------------------------------------------------------------
This project is on  Leave Travel Concession Management System for the employees of 
IIT-BHU, Varanasi. 
 Leave Travel Allowance as the name suggests is an allowance paid to the employee by the employer when the former is travelling with their family or alone.


Import the sql dump file 'ltc.sql' into your mysq by using the following command
$ mysqldump -u username -p -h localhost ltc < ltc.sql

This creates the database

LTC MANAGEMENT SYSTEM:
This portal can do the following things:
1)A new employee can register on the LTC portal.

2)An existing employee can see his profile by logging in the portal.

3)The login id is the employee_id and password is the department as in the database for the employees.
	eg. loginid=101 and password = cer

3)An existing employee can apply for Leave Travel Concession and Advance through the portal.

4)An existing employee can apply for claiming the money for LTC.

5)There is one admin whose :
	admin loginid = isha
	admin password = isha 

6)The admin on logging can see the list of those who have applied for advance and claim separately.
and can also see the no of employees who have applied for advance and claim.

7)For an existing employee, he will first apply for LTC and advance.
  He gets a sanction no (reference no) and saves it.
  He uses the no. when applying for claim for LTC. 

FOR RUNNING THE PROGRAM
1)cd into project/ltc
2)run source bin/activate
3)run python manage.py runserver
4)Run at localhost : 127.0.0.1:8000
------------------------------------------------------------------------------------------------
Made by : Isha Agarwal
	   14075063
	Department of Computer Science & Engg.	
