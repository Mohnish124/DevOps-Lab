from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to Flask Application - User Authentication Feature"
if __name__ == "__main__":
    app.run(debug=True)