#!/usr/bin/python3
"""
Script to list all states from a MySQL database hbtn_Oe_O_usa
"""
import MySQLdb
import sys

if __name__ == "__main__":
    con = MySQLdb.connect(
	host="localhost", port=3306, user=argv[1],
	password=argv[2], database=argv[3])
    cursor = con.cursor()
    cursor.execute("SELECT = FROM states ORDER BY id ASC")
    db = cursor.fetchall()
    for i in db:
	print(i)
    cursor.close()
    db.close()
