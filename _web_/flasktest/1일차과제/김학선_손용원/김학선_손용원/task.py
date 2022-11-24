from flask import Flask, render_template, request # 클래스 가져오기


app = Flask( __name__ ) # "__main__" 임포트 된건가 아니면 실행된건가

@app.route("/", methods=["POST","GET"]) # 명령어
def bmical():
    bmi = ""
    weight = ""
    height = ""
    if request.method == "POST" and "weight" in request.form and "height" in request.form:
        weight = int(request.form.get("weight"))
        height = int(request.form.get("height"))
        bmi = weight/((height-100)*0.85)*100
    return render_template("bmi.html",bmi=bmi, weight=weight, height=height)




if __name__ == "__main__" :
    app.run(host = "0.0.0.0", port=4000, debug = True) # 포트번호 프로세스 식별자, 0.0.0.0 모든 요청에 대해서 응답하겠다.

