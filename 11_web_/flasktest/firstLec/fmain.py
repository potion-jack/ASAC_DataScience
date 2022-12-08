from flask import Flask, render_template ,request
from calculator import calcBMI

app = Flask( __name__ )

@app.route("/")
def root():
    return "<h1>hello flask</h1>"  #response

@app.route("/test")
def test():
    return "<h1>test flask</h1>"  #response

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
    print( request.args ) #get요청의 query string 데이터추출 
    myname = request.args['myname']
    myage = request.args['myage']
    return render_template('formproc.html',myname=myname,
             myage=myage,test='hello')
    # return f"<h1>이름:{myname} 나이:{myage}</h1>"


@app.route("/calcform")
def calcform():
    return render_template('calcform.html')

@app.route("/calcproc")
def calcproc():
    num1 = int( request.args['num1'] )
    num2 =  int( request.args['num2'] )
    return f"<h1>합:{num1+num2}"


@app.route("/bimanForm")
def bimanForm():
    return render_template('bimanForm.html')


@app.route("/bmiproc")
def bmiproc():
    # 함수설계: SRP, devide by conquer
    height = int(request.args['height'])
    weight = int(request.args['weight'])
    result, sajin = calcBMI( height, weight)

    return render_template('bmiproc.html', height=height, 
        weight=weight, result=result, sajin=sajin)


@app.route("/imageChangeForm")
def imageChangeForm():
    return render_template('imageChangeForm.html')

if __name__ == "__main__":
    app.run( host='0.0.0.0', port=4000, debug=True)
    # 웹서버 구동... requests 처리