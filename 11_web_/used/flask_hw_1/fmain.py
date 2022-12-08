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


@app.route('/hw_1')
def hw_1():
    return render_template('hw_1.html')

@app.route('/hw_1_formproc')
def hw_1_formproc():
    # get 요청의 query string 데이터 추출
    height = int(request.args['height'])
    weight = int(request.args['weight'])
    av_weight = (height - 100) * 0.85
    av_fat = (weight / av_weight)*100
    if av_fat <= 90:
        result = '저체중'
        path = "/static/image/low.png"
    elif (av_fat > 90)&(av_fat < 110):
        result = '정상'
        path = "/static/image/mid.png"
    elif (av_fat >= 110)&(av_fat < 120):
        result = '과체중'
        path = "/static/image/mid_high.png"
    elif (av_fat >= 120):
        result = '비만'
        path = "/static/image/high.png"
        
    return render_template('hw_1_formproc.html',myname=height, myage=weight, result=result, path = path)

@app.route('/hw_2')
def hw_2():
    print(request.args)
    return render_template('hw_2.html')

@app.route('/hw_2_formproc')
def hw_2_formproc():
    # get 요청의 query string 데이터 추출
    print(request.args)
    return render_template('hw_2_formproc.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 4000, debug = True)
    # 웹서버 구동 requests처리
