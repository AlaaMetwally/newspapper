Go To The vagrant directory and download the newspapper.sql
DataBase stpes in commands 
	go to the database ==> sudo su -u postgres
			   ==> psql
  	   create database ==> create database news;
       connect to database ==> \connect news
import newspapper.sql in postgresql ==> psql news < newspapper.sql 
		     quit from psql ==> \q

About The Project :
	   run the project ==> python question.py
the result of the project will be in the newspapper.log 
the project consists of two python files the questions.py consists of the 
print statements used for the output and the newspapper.py consists of the 
query and the connection of the database  
