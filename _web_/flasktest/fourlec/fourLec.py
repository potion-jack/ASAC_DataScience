from flask import Flask, render_template, request
from mysql.connector import pooling
from base64 import b64encode
from datetime import datetime

import pandas as pd
import plotly
import plotly.express as px
import json

pool = pooling.MySQLConnectionPool(
    pool_name='mypool',
    pool_reset_session=True,
    pool_size=3,
    host='localhost',
    port='3306',
    database='flaskdb',
    user='root',
    password='6569'
)

app = Flask(__name__)


@app.route('/')
def hello():
    return 'hello'

@app.route('/fileForm')
def fileForm():
    return render_template('fileForm.html')

@app.route('/fileSend', methods = ['POST'])
def fileSend():
    myfile = request.files['myfile'] # for file -> request.files
    sql = 'insert into imgup(fname,imgfile) values(%s,%s)'
    con = pool.get_conection()
    c=con.cursor()
    c.execute(sql,(myfile.filename, myfile.read()))
    con.commit()
    c.close()
    con.close()
    return f"<h1>your file has been saved to db</h1>"

@app.route('/selectImg')
def selectImg():
    con = pool.get_conection()
    c=con.cursor()
    c.execute("select * from imgup")
    result = c.fetchall()
    # web image --> base64 encoding
    # data = list()
    # for n,img in result:
    #     b = b64encode(img).decode('utf-8') #
    #     data.append((n,'data:;base64,'+b)) # data는 base64 encoding이다 : data:;base64 
        
    c.close()
    con.close()
    return render_template('selectView.html',data=result)

# https://tedboy.github.io/jinja2/templ14.html


@app.route('/myfilter')
def myfilter():
    return render_template('myfilter.html',n=-10, f=3.141592, s='abc', s1 = "     def     ")


@app.template_filter('reverse')
def reverse_filter(s):
    return s[::-1]


@app.template_filter('base64') # base64 is the filter_name not base64_filterimg
def base64_filter(img):
    b = b64encode(img).decode('utf-8') #
    return 'data:;base64,'+b
    

@app.route('/selectStudnet')
def selectStudent():
    con = pool.get_conection()
    c = con.cursor()
    c.execute('select * from student')
    result = c.fetchall()
    con.close()
    return render_template('selectStudent.html',result=result)

@app.template_filter('datefilter')
def datefilter(date_s):
    ans = datetime.strptime(date_s,'%Y-%m-%d')
    # ans = datetime.strftime(date_s,format='%Y-%m-%d')
    return f"{ans.year}년{ans.month}월{ans.day}일"

"""student chart"""

@app.route('/studentChart')
def studentChart():
    sql = 'select * from student'
    df = pd.read_sql(sql, pool.get_connection())
    fig = px.bar(df, x="person_name", y="person_age", title="타이틀", width=600, height=400,
                 labels={'person_name':'이름','person_age':'나이'},
                 color_discrete_map={"나이": "RebeccaPurple"},
                 template="simple_white",text='person_age')
    fig.update_layout(yaxis_range=[0,100])
    graphJSON = json.dumps(fig,cls=plotly.utils.PlotlyJSONEncoder)
    return render_template('nodash.html', graphJSON=graphJSON)

@app.route('/birthchart')
def birthchart():
    df = pd.read_csv('../thirdlec/births.csv',header=None)
    df.columns = ['year','child_m','child_w']
    my_df = df[(df['year']<1950) & (df['year']>1900)]
    temp = pd.melt(my_df,id_vars=['year'], var_name='gender',value_name='value')
    
    # fig = px.bar(temp, x='year', y='value', color='gender',barmode='group',facet_col='gender')
    fig = px.bar(temp, x='year', y='value', color='gender',barmode='group')
    
    """fig = px.bar(my_df, x="year", y="child_m", title="타이틀", width=600, height=400,
                #  labels={'person_name':'이름','person_age':'나이'},
                #  color_discrete_map={"나이": "RebeccaPurple"},
                 template="simple_white",
                #  text='child_m'
                 )"""
    # fig.update_layout(yaxis_range=[0,])
    graphJSON = json.dumps(fig,cls=plotly.utils.PlotlyJSONEncoder)
    return render_template('nodash.html', graphJSON=graphJSON)
    

""" local
# @app.route('/fileSend', methods = ['POST','GET'])  : for body and also head (defualt -> methods = ['GET'])
@app.route('/fileSend', methods = ['POST'])
def fileSend():
    myname = request.form['myname'] # except file -> request.form
    # string 객체
    myfile = request.files['myfile'] # for file -> request.files
    # file 객체
    print(myfile.filename) # check filename
    myfile.save(f"./rfile/{myfile.filename}") # file_name 으로 저장
    return f"<h1> {myname}, your file has been saved</h1>"
"""

""" run server """
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4000, debug=True)
    