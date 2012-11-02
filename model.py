import sqlite3
from time import datetime, time, strptime

def connect_db():
	return sqlite3connect("tipsy.db")

def new_user(db, email, password, name):
	c = db.cursor()
	query = """INSERT INTO Users VALUES (NULL, ?, ?, ?)"""
	result = c.execute(query, (email, password, name))
	db.commit()
	return result.lastrowid

def authenticate(db, email, password):
	c = db.cursor()
	query = """SELECT * FROM Users WHERE email=? AND password=?"""
	c.execute(query, (email, password))
	result = c.fetchone()
	fields = ["id", "email", "password", "name"]
	if result:
		return dict(zip(fields, result))
	return None

def new_task(db, title, user_id):
	c = db.cursor()
	query = """INSERT INTO Tasks VALUES (NULL, ?, NULL, NULL, ?)"""
	result = c.execute(query, (title, user_id))
	db.commit()
	return result.lastrowid

def get_user(db, user_id):
	c = db.cursor
	query ="""SELECT * FROM Users WHERE id=?"""
	c.execute(query, user_id)
	result = c.fetchone()
	fields = ["id", "email", "password", "name"]
	if result:
		return dict(zip(fields, result))


def complete_task(db, task_id):
	c = db.cursor
	query = """UPDATE tasks column="completed_at" WHERE id=?"""
	result = c.execute(query, task_id)
	db.commit

def get_tasks(db, user_id):
	pass

def get_task(db, task_id):
	pass
