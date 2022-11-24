from flask import Flask, render_template, request

app = Flask( __name__ ) #

@app.route('/') #데코레이터
def root():
    return '<h1>hello flask</h1>'  #response

@app.route('/hw') 
def hw():
    return render_template('hw.html')

@app.route('/hwproc') 
def hwproc():
    print(request.args) #get요청의 query string 데이터추출
    height= int(request.args['height'])
    weight= int(request.args['weight'])
    avgw = (height - 100)*0.85
    obesity = weight/avgw*100
    if obesity < 90:
        obp = '저체중'
        im = "/static/image/low.jpg"
    elif obesity < 110:
        obp = '정상'
        im = "/static/image/avg.jpg"
    elif obesity < 120:
        obp = '과체중'
        im = "/static/image/fat.jpg"
    else:
        obp = '비만'
        im = "/static/image/obese.jpg"
    return render_template('hwproc.html', height=height, 
            weight=weight, obp=obp, im=im)

# @app.route('/hw2') 
# def hw2():
#     return render_template('hw2.html')

# @app.route('/hw2proc') 
# def hw2proc():
#     print(request.args) #get요청의 query string 데이터추출
#     myname= request.args['myname']
#     myage= request.args['myage']
#     return render_template('hw2proc.html', myname=myname, 
#             myage=myage, test='hello')
#     # return f"<h1>이름: {myname} 나이 {myage}</h1>"

if __name__ =='__main__':
    app.run( host='0.0.0.0', port=4000, debug=True) #0.0.0.0-클라이언트에 있는 ip address가 뭐든 상관없이 웹서버가 응답해주겠다 #port번호- 프로세서 식별자, 4000- 내가 4000번 포트로 대기하겠다
    #웹서버 구동...requests 처리
