from flask import Flask, render_template, request

app = Flask(__name__)
"""
Flask(
    import_name: str,
    static_url_path: str | None = None, 
    static_folder: str | PathLike | None = "static",
    template_folder: str | None = "templates",
    static_host: str | None = None, 
    host_matching: bool = False,
    subdomain_matching: bool = False,
    instance_path: str | None = None,
    instance_relative_config: bool = False,
    root_path: str | None = None)
"""

@app.route('/')
def root():
    return "<h1>hello flask</h1>" # response


@app.route('/test')
def test():
    return  "<h1>test flask</h1>" # response

@app.route('/aa')
def aa():
    return render_template('a.html')

@app.route('/div')
def div():
    return render_template('div.html')

@app.route('/img')
def img():
    return render_template('img.html')

@app.route('/anchor')
def anchor():
    return render_template('anchor.html')

@app.route('/ul')
def ul():
    return render_template('ul.html')

@app.route('/table')
def table():
    return render_template('table.html')

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/formproc')
def formproc():
    # get 요청의 query string 데이터 추출
    myname = request.args['myname']
    myage = request.args['myage']
    return render_template('formproc.html',myname=myname, myage=myage,test='Hello')
    # return f"<h1>이름 :{myname} 나이 : {myage}</h1>"

@app.route('/quiz')
def quiz():
    return render_template('quiz.html')


@app.route('/quiz_formproc')
def quiz_formproc():
    # get 요청의 query string 데이터 추출
    num1 = request.args['num1']
    num2 = request.args['num2']
    return f"<h1>합은 :{int(num1)+int(num2)}</h1>"



if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 4000, debug = True)
    # 웹서버 구동 requests처리
