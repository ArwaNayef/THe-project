from flask import Flask, render_template, request
app=Flask(__name__)

@app.route("/")
def home():
	return render_template("Home.html")

@app.route("/health")
def health():
	return render_template("Health.html")


@app.route("/english")
def english():
	return render_template("English.html")


@app.route("/programming")
def programming():
	return render_template("Programming.html")

@app.route("/different")
def different():
	return render_template("Different.html")	



if __name__ == "__main__":
	app.run()
