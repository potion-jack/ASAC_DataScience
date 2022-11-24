from flask import Flask, render_template, request
import sys

app = Flask(__name__) 

@app.route("/") 
def root():
    return "<h1>hello flask<h1>"

@app.route("/weight")
def weigh():
     return render_template("weight.html")

@app.route("/action")
def action():
    tall = request.args['tall']
    weight =request.args['weight']
    normal = (int(tall) - 100) * 0.85
    bmi = (int(weight) / normal)*100
    if bmi <=90:
        result="저체중"
        image="/static/image/1.jpg"
    elif 90<=bmi<=110:
        result="정상"
        image="/static/image/2.jpg"
    elif 110<=bmi<=120:
        result="과체중"
        image="/static/image/3.jpg"
    else:
        result="비만"
        image="/static/image/4.jpg"
    return render_template('action.html',tall=tall, 
                        weight=weight, result=result,image=image)


if __name__ == "__main__":
    app.run(host='0.0.0.0',port = 4000, debug = True)