from flask import Flask, render_template, request
import sys

app = Flask(__name__)

@app.route("/")
def root():
    return "<h1>hello flask....</h`>" 

@app.route("/test")
def test():
    return "</h1>test hello flask</h1>"

@app.route("/aa")
def aa():
    return render_template('a.html')

@app.route("/div")
def div():
    return render_template('div.html')

@app.route("/img")
def img():
    return render_template('img.html')

@app.route("/anchor")
def anchor():
    return render_template('anchor.html')

@app.route("/ul")
def ul():
    return render_template('ul.html')

@app.route("/table")
def table():
    return render_template('table.html')

@app.route("/form")
def form():
    return render_template('form.html')

@app.route("/calculator")
def calculator():
    return render_template('calculator.html')

@app.route("/calcform")
def calcform():
    return render_template('calcproc.html')

@app.route("/formproc")
def formproc():
    return render_template('formproc.html')

@app.route("/calcproc")
def calcproc():
    print(request.args)
    num1 = int(request.args['num1'] )
    num2 = int(request.args['num2'] )
    return f"<h1>합:{num1 + num2}"

    #render_template('formproc.html')
    #return f"<h1>이름:{myname} 나이:{myage}</h1>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4000,debug=True)
    # 웹 서버 구동