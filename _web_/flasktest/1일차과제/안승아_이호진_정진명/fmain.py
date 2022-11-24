from flask import Flask, render_template, request

app = Flask( __name__)

@app.route("/")
def root():
    return "<h1>hello flask</h1>"

@app.route("/test")
def test():
    return "<h1>test flask</h1>"

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

@app.route("/formproc")
def formproc():
    print(request.args) # query string 데이터 추출
    myname = request.args['myname']
    myage = request.args['myage']
    return render_template('formproc.html',myname=myname,myage=myage)
    # return f"<h1>이름:{myname} 나이:{myage}</h1>"

@app.route("/quiz")
def quiz():
    return render_template('quiz.html')

@app.route("/cal_proc")
def cal_proc():
    print(request.args) # query string 데이터 추출
    num1 = request.args['num1']
    num2 = request.args['num2']
    s = int(num1) + int(num2)

    return f"<h1>합은:{s}</h1"

@app.route("/hw1")
def hw1():
    return render_template('hw1.html')

@app.route("/hw1proc")
def hw1_proc():
    print(request.args) # query string 데이터 추출
    height = int(request.args['height'])
    weight = int(request.args['weight'])
    s_weight = (height-100)*0.85
    obesity = (weight)/(s_weight)*100 
    result = ''
    if obesity >= 120:

        result = "비만"
    
    elif obesity >= 110:

        result = "과체중"

    elif obesity >= 90:

        result = "정상"

    else:

        result = '저체중'

    return render_template('hw1proc.html',height=height,weight=weight,result=result)


if __name__ == "__main__":
    # 웹 서버 구동
    app.run(host='localhost',port=4000, debug=True) # host: 모든 클라이언트 ip 주소 처리, port: 프로세스 식별자
