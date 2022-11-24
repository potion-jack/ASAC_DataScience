from flask import Flask, render_template, request
import sys

app = Flask(__name__)

@app.route("/")
def root():
    return render_template("main.html")

@app.route("/be")
def be():
    return render_template("be.html")

@app.route("/bee")
def bee():
    height = int(request.args["height"])
    weight = int(request.args["weight"])
    if weight/((height-100)*0.85)*100 <= 90:
        return render_template("bee.html", weight=weight, height=height, result="저체중")
    elif 90< weight/((height-100)*0.85)*100 <= 110:
        return render_template("bee.html", weight=weight, height=height, result="정상")
    elif 110< weight/((height-100)*0.85)*100 <= 120:
        return render_template("bee.html", weight=weight, height=height, result="과체중")
    else :
        return render_template("bee.html", weight=weight, height=height, result="비만")


@app.route('/movie')
def movie():
    page = int(request.args['page'] if 'page' in request.args  else '0')
    if 'action' in request.args:
        if request.args['action'] == '이전':
            page = (page - 1) % 4
        else:
            page = (page + 1) % 4
    
    return render_template('movie.html',
                           page=page)

if __name__ == "__main__":
    app.run(host = '0.0.0.0', port=4000, debug=True)
    # 웹 서버 구동 requests 처리
