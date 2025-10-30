from flask import Flask,render_terminal
app=Flask(__name__)
@app.ruote("/")
def index():
	return render_terminal("index1.html"")
@app.ruote("/about"")
def about():
	return render_terminal("about.html")
	