#!/usr/local/bin/python
# -*- coding=UTF-8 -*-
import os, sys
from flask import Flask, render_template, request, redirect, session
import model


app = Flask(__name__)

@app.route("/")
def index():
	user_name="Éléonore"
	return render_template("index.html", user_name=user_name.decode("UTF-8"))

@app.route("/Tasks")
def list_tasks():
	db = model.connect_db()
	return render_template("list_tasks.html", list_all_tasks=model.get_tasks(db, None))

# @app.route("/new_task")
# def new_task():
# 	return redirect("new_task.html")

@app.route("/save_task", methods=["POST"])
def save_task():
	task_title = request.form['task_title']
	db = model.connect_db()
	task_id = model.new_task(db, task_title, 1)
	return redirect("/Tasks")

@app.route("/login", methods=["POST"])
def login():
	email = request.form['email']
	password = request.form['password']
	db = model.connect_db()
	auth_user = model.authenticate(db, email, password)
	if auth_user != None:
		return redirect("/Tasks")

@app.route("/logout", methods=["GET"])
def logout():
	return redirect("/")

@app.route("/task_completed", methods=["POST"])
def task_completed():
	db = model.connect_db()
	# task_id = request.p[item['id']]
	# return redirect("/Tasks", completed_at=model.complete_task(db, task_id))
	return redirect("/Tasks")

if __name__ == "__main__":
	app.run(debug=True)