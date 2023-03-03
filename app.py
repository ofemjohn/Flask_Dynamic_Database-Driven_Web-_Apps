from flask import Flask, render_template

app = Flask(__name__)

JOBS = [
{
    "id": 1,
    "title": "MERN STACK",
    "location": "Bengalrus, India",
    "salary": "Rs. 1,00,00",
    "email": "www.john@gmail.com"
},
{
    "id": 2,
    "title": "FULL STACK",
    "location": "China",
    "salary": "Rs. 2,00,00",
    "email": "jhfg@gmail.com"
},
{
    "id": 3,
    "title": "DYSLEXIA",
    "location": "LAGOS, NIGERIA",
    "salary": "NG 345,000",
    "email": "dyslexia@gmail.com"
},
{
    "id": 4,
    "title": "COMPUTER SCIENCE",
    "location": "GHANA",
    "salary": "12345",
    "email": "favour@gmail.com"
}

]

@app.route("/")
@app.route("/home")
def hello_world():
    return render_template('/index.html', jobs=JOBS)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5003)