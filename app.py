from flask import Flask
app = Flask(__name__)
@app.route("/")

def hello():
    return "Hello World! Myname is Sarawut Sittharod"
if __name__ == "__main__":
    app.run()