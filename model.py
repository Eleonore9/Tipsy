import sqlite3
import datetime, time
import copy

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
	now = datetime.datetime.now()
	query = """INSERT INTO Tasks VALUES (NULL, ?, ?, NULL, ?)"""
	result = c.execute(query, (title, now, user_id))
	db.commit()
	return result.lastrowid

def get_user(db, user_id):
	c = db.cursor()
	query = """SELECT * FROM Users WHERE id=?"""
	c.execute(query, (user_id,))
	result = c.fetchone()
	fields = ["id", "email", "password", "name"]
	if result:
		return dict(zip(fields, result))

def get_username(db, email, password):
	c = db.cursor()
	query = """SELECT name FROM Users WHERE email=? AND password=?"""
	c.execute(query, (email, password))
	result = c.fetchone()
	fields = ["name"]
	if result:
		return dict(zip(fields, result))

def complete_task(db, task_id):
	c = db.cursor()
	now = datetime.datetime.now()
	query = """UPDATE Tasks SET completed_at=? WHERE id=?"""
	result = c.execute(query, (now, task_id))
	db.commit()
	return result.lastrowid

def get_tasks(db, user_id):
	c = db.cursor()
	#query = """SELECT * FROM Tasks WHERE user_id=?"""
	# ids = []
	# titles = []
	# creation =[]
	# completion = []
	# users = []
	results = []
	fields = ["id", "title", "created_at", "completed_at", "user_id"]

	if user_id:
		rows = c.execute("SELECT * FROM Tasks WHERE user_id=?", [user_id])
	else:
		rows = c.execute("SELECT * FROM Tasks")
	for row in rows:
		#c.execute(query, (user_id,))
		#result = c.fetchone()
		#print row
		tuples = zip(fields, row)
		results.append(dict(tuples))
		# ids.append(row[0])
		# titles.append(row[1])
		# creation.append(row[2])
		# completion.append(row[3])
		# users.append(row[4])
	return results
	# result = [ids, titles, creation, completion, users]
	# #print result
	# list_dict = []
	# if user_id != None:
	# 	#count = 0
	# 	#while count < len(fields):
	# 		#dico = dict(zip(fields[count], result[count]))
	# 		#count += 1
	# 	dico = dict(zip(fields, result))
	# 	list_dict.append(copy.copy(dico))
	# 	#return list_dict
	# 	return list_dict
	# elif TypeError:
	# 	return c.execute("SELECT * FROM Tasks")

def get_task(db, task_id):
	c = db.cursor()
	query = """SELECT * FROM Tasks WHERE id=?"""
	c.execute(query, (task_id,))
	result = c.fetchone()
	fields = ["id", "title", "created_at", "completed_at", "user_id"]
	return dict(zip(fields, result))
