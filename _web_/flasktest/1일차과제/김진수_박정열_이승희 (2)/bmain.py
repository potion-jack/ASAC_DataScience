from flask import Flask, render_template,request
import sys

app = Flask(__name__)

@app.route("/")
def root():
    return "<h1>비만도를 원하십니까</h1>" 

@app.route("/img1")
def img1():
    return render_template('img1.html')

@app.route("/form1")
def form1():
    return render_template('form1.html')

@app.route("/formproc1")
def formproc1():
    print(request.args)
    high = int(request.args['high'])
    wei= int(request.args['wei'])
    swei = (high-100)*0.85
    biman = int((wei/swei)*100)
    result = ""
    k = 0
    if biman <=90:
        result = "저체중"
        k = render_template('img1.html')
    elif 90<biman<=110:
        result = "정상"
        k = render_template('img2.html')
    elif 110<biman<=120:
        result="과제중"
        k = render_template('img3.html')
    elif biman>120:
        result = "비만"
        k = render_template('img4.html')
    return k+f"<h1>키:{high}</h1><h1>몸무게:{wei}</h1><h1>결과:{result}</h1>"

if __name__=="__main__":
    app.run(host='0.0.0.0',port=4001,debug=True)
    #웹서버 구동 ..request 처리 
    

