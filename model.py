import sqlite3
import datetime, time

def connect_db():
	return sqlite3.connect("tipsy.db")

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
	query ="""SELECT * FROM Users WHERE user_id=?"""
	c.execute(query, user_id)
	result = c.fetchone()
	fields = ["id", "email", "password", "name"]
	if result:
		return dict(zip(fields, result))


def complete_task(db, task_id):
	c = db.cursor
	now = datetime.datetime.now()
	query = """UPDATE Tasks SET completed_at=now WHERE id=?"""
	result = c.execute(query, task_id)
	db.commit()
	return result.lastrowid

def get_tasks(db, user_id):
	c = db.cursor
	query = """SELECT * FROM Tasks WHERE user_id=?"""
	c.execute(query, user_id)
	result = c.fetchone()
	list_dict = []
	fields = ["id", "title", "created_at", "completed_at", "user_id"]
	if user_id != None:
		for element in result:
			return list_dict.append(dict(zip(fields, element)))
	else:
		for tasks in Tasks:
			return list_dict.append(dict(zip(fields, tasks)))

def get_task(db, task_id):
	c = db.cursor
	query = """SELECT * FROM Tasks WHERE id=?"""
	c.execute(query, task_id)
	result = c.fetchone()
	fields = ["id", "title", "created_at", "completed_at", "user_id"]
	return dict(zip(fields, result))
