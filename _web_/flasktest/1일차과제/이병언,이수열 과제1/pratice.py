from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def form():
    
    return render_template('form.html', bmi=0)

@app.route("/formproc")
def formproc():
    print(request.args) # get요청의 query string 데이터 추출하는 속성
    myheight = int(request.args['myheight'])
    myweight = int(request.args['myweight'])
    bmi = (myweight/(myheight - 100)*0.85)*100
    return render_template("form.html",myheight=myheight, myweight=myweight,bmi=bmi)

if __name__ == "__main__":
    app.run(host = '0.0.0.0', port = 4000, debug = True)