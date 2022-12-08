from flask import Flask,render_template,request
from flask_paginate import Pagination, get_page_args

from dbhandle import insertStudentsql, selectStudent, deleteStudentsql
import dbhandlePool as p
import pandas as pd

app = Flask(__name__)

@app.route('/')
def root():
    return "<h1>hello</h1>"

@app.route('/insertStudent')
def insertStudent():
    return render_template('insertStudent.html')

@app.route('/insertProc')
def insertProc():
    myname = request.args['myname']
    myage = int(request.args['myage'])
    mybirth = request.args['mybirth']
    # result = insertStudentsql(myname,myage,mybirth)
    result = p.insertStudentPool(myname,myage,mybirth)
    return render_template('insertProc.html',result=result)

@app.route('/select')
def select():
    data = selectStudent()
    return render_template('selectView.html',data=data)

@app.route('/deleteStudent')
def deleteStudent():
    return render_template('deleteStudent.html')

@app.route('/deleteProc')
def deleteProc():
    myname = request.args['myname']
    result = deleteStudentsql(myname)
    return render_template('deleteProc.html',result=result)

@app.route('/births')
def births():
    birth = pd.read_csv('./births.csv',header=None)
    # print(birth.values.tolist())
    return render_template('birthView.html',birth = birth.values.tolist())

birth = pd.read_csv('./births.csv',header=None)
birthList=birth.values.tolist()

def get_birth(offset=0,per_page=10):
    return birthList[offset:offset+per_page]

@app.route('/birthsPage')
def birthsPage():
    page, per_page, offset = get_page_args(page_parameter='page',
                                           per_page_parameter='per_page')
    
    print('page :',page,'per_page:',per_page,'offset: ',offset)
    
    total = len(birthList)
    
    pagination_births = get_birth(offset=offset,per_page=per_page)
    
    pagination = Pagination(page=page,per_page=per_page,offset=offset,
                            total=total,
                            css_framwork='bootstrap5')
    
    return render_template('birthViewPage.html',
                           pagination=pagination,
                           births=pagination_births)
    
    # return render_template('birthView.html',birth= )

"""
python_module
"""

if __name__=='__main__':
    app.run(host='0.0.0.0',
            port=4000,
            debug=True)
    