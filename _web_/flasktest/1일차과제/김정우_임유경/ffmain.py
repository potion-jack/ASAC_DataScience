from flask import Flask, render_template, request

app = Flask( __name__ ) #이 문자열에 __main__이 들어감.

@app.route("/")
def root():
    return "<h1>hello flask</h1>" #response

@app.route("/bmi")
def bmi():
    return render_template('bmi.html')

@app.route("/bmiproc")
def bmiproc():
    
    myki = int(request.args['myki'])
    mommuge = int(request.args['mommuge'])
    rere = mommuge*100/(myki-100)*0.85
    if rere <= 90:
        result = "저체중"
        sajin = "/static/low.jpg"
    elif 90<rere<=110:
        result = "정상"
        sajin = "/static/normal.jpg"
    elif 110<rere<=120:
        result = "과체중"
        sajin = "/static/high.jpg"
    else:
        result = "비만"
        sajin = "/static/fat.jpg"

    return render_template('bmiproc.html', myki=myki, mommuge=mommuge, result=result, sajin=sajin)

@app.route('/hw_2')
def hw_2():
    print(request.args)
    return render_template('hw_2.html')

@app.route('/hw_2_formproc')
def hw_2_formproc():
    # get 요청의 query string 데이터 추출
    print(request.args)
    return render_template('hw_2_formproc.html')


if __name__ == "__main__":
    app.run( host="0.0.0.0", port=4001, debug=True)
    # 웹서버 구동, requests 처리