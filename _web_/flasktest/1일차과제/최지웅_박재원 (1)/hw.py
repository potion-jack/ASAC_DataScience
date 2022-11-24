from flask import Flask, render_template, request

app = Flask( __name__ )

@app.route("/")
def root():
    return "<h1>hello falsk</h1>" #response 

@app.route("/hwform")
def hwform():
    return render_template ('hwform.html')

@app.route("/formproc")
def formproc():
    height = int(request.args['height'])
    weight = int(request.args['weight'])
    standard = (height-100)*(0.85)
    mando = (weight/standard)*100
    if mando <=90:
        result = 'underweight'
        num=1
    elif 90<mando and mando<=110:
        result = 'normal'
        num=2
    elif 110<mando and mando<=120:
        result = 'overweight'
        num=3
    elif 120<mando:
        result = 'bman'
        num=4

    return render_template('hwformproc.html', height=height, weight=weight, result=result,num=num)


if __name__ == "__main__":
    app.run( host = '0.0.0.0', port=4000, debug=True)
    #웹서버 구동 ... requests 처리
