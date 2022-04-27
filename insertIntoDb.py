# Import required modules
import csv
import sqlite3
import psycopg2

connection = psycopg2.connect(database="d8cpvu6blcd0la",
						user='aziifjamteljua',
						password='c0bf00eb34cc5f361cd4453321bd073aeac6e1aee8a02d6b954f34cac0122c88',
						host='ec2-52-3-200-138.compute-1.amazonaws.com',
						port='5432')

connection.autocommit = True
cursor = connection.cursor()


# This File is used to  insert data into the data base using the csv files
# Connecting to the geeks database
# connection = sqlite3.connect('db.sqlite3')

# Creating a cursor object to execute
# SQL queries on a database table
# cursor = connection.cursor()

# Table Definition


# Creating the table into our
# database

no_records = 0;
# Opening the person-records.csv file
# with open('customer.csv', 'r') as file:
# 	reader = csv.reader(file)
# 	for row in reader:
# 		cursor.execute("INSERT INTO mediAssist_customer  VALUES (%s,%s,%s,%s,%s)" ,row)
# 		connection.commit()
# 		no_records += 1

with open('vehicle.csv', 'r') as file:
	reader = csv.reader(file)
	for row in reader:
		cursor.execute("INSERT INTO mediAssist_vehicle  VALUES (%s,%s,%s)" ,row)
		connection.commit()
		no_records += 1

with open('policy.csv', 'r') as file:
	reader = csv.reader(file)
	for row in reader:
		cursor.execute("INSERT INTO mediAssist_policy  VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)" ,row)
		connection.commit()
		no_records += 1



connection.close()

print("no of row transferred",no_records)
