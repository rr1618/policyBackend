# Import required modules
import csv
import sqlite3


# This File is used to  insert data into the data base using the csv files
# Connecting to the geeks database
connection = sqlite3.connect('db.sqlite3')

# Creating a cursor object to execute
# SQL queries on a database table
cursor = connection.cursor()

# Table Definition


# Creating the table into our
# database

no_records = 0;
# Opening the person-records.csv file
with open('customer.csv', 'r') as file:

	for row in file:

		cursor.execute("INSERT INTO mediAssist_customer  VALUES (?,?,?,?,?)" ,row.split(","))
		connection.commit()
		no_records += 1

with open('policy.csv', 'r') as file:

	for row in file:

		cursor.execute("INSERT INTO mediAssist_policy  VALUES (?,?,?,?,?,?,?,?,?,?)" ,row.split(","))
		connection.commit()
		no_records += 1

with open('vehicle.csv', 'r') as file:

	for row in file:

		cursor.execute("INSERT INTO mediAssist_vehicle  VALUES (?,?,?)" ,row.split(","))
		connection.commit()
		no_records += 1



connection.close()

print("no of row transferred",no_records)
