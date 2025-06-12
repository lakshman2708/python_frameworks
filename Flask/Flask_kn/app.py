from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route('/')
def welcome():
    return 'Welcome'

@app.route('/success/<int:score>')
def success(score):
    return "The person has passed and the marks is "+ str(score)

@app.route('/fail/<int:score>')
def fail(score):
    return "The person has failed and the marks is "+ str(score)

@app.route('/results/<int:marks>')
def results(marks):
    res = ''
    if marks < 50:
        res = 'fail'
    else:
        res = 'success'
    return redirect(url_for(res,score = marks))

if __name__ == '__main__':
    app.run(debug=True)
    