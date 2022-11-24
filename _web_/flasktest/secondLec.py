from flask import Flask, render_template ,request

app = Flask( __name__ )

@app.route("/")
def root():
    return "<h1>hello flask</h1>"  #response

@app.route("/jinjaIf")
def jinjaIf():
    return render_template('jinjaIf.html', num=10)

@app.route("/jinjaFor")
def jinjaFor():
    return render_template('jinjaFor.html', myList=['사과','딸기','포도','수박'])

@app.route("/formTest")
def formTest():
    return render_template('formTest.html')

@app.route("/formProc")
def formProc():
    myname = request.args['myname']
    myage = request.args['myage']
    mybirth = request.args['mybirth']
    color = request.args['color']
    # hobby = request.args['hobby']
    hobby = request.args.getlist('hobby')
    print(hobby)
    hobby = '-'.join(hobby)
    return render_template('formProc.html', myname=myname,myage=myage,
         mybirth=mybirth, color=color, hobby=hobby)


@app.route("/bootTest")
def bootTest():
    return render_template('bootTest.html')

@app.route("/travel")
def travel():
    return render_template('travel.html')

@app.route("/phi")
def phi():
    return render_template('phi.html')

@app.route("/thai")
def thai():
    return render_template('thai.html')

if __name__ == "__main__":
    app.run( host='0.0.0.0', port=4000, debug=True)