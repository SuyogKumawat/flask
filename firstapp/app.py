from flask import Flask,render_template
import subprocess

app=Flask("my app")

@app.route("/init")
def initial():
	return "<b>Hello We are using Flask<b/>"

@app.route("/render")
def dynamic():
	name="Arth Learner"
	return render_template("a.html",n=name)

@app.route("/home")
def homes():
	data=subprocess.getoutput("date/t")
	return data

	