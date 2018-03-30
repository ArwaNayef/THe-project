from flask import Flask
app=Flask(__name__)

@app.route("/")
def home():
	return "hello"

@app.route("/health")
def health():


@app.route("/english")
def english():


@app.route("/programming")
def programming():


@app.route("/different")
def different():
	



if __name__ == "__main__":
	app.run()
