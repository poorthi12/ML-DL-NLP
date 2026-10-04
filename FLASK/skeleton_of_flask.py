from flask import Flask
app = Flask(__name__)

@app.route("/")
def welcome():
    return "Hi bro How Are You"
@app.route("/next")
def next():
    return "it is jus a next page"

if __name__=="__main__":
    app.run(debug=True)