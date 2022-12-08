# https://plotly.com/python/plotly-express/

import plotly
import plotly.express as px
from mysql.connector import connect
import pandas as pd

def bar():
    df = px.data.tips()
    print( df )
    fig = px.bar(df, x="sex", y="total_bill", color="smoker", barmode="group")
    fig.show()

def student():
    sql = 'select * from student'
    conn = connect(host='localhost',user='root',password='6569',
            db='flaskdb',charset='utf8')
    
    # c = conn.cursor()
    # c.execute('select * from student')
    # result = c.fetchall()
    
    df = pd.read_sql(sql, conn)
    fig = px.bar(df, x="person_name", y="person_age", title="타이틀", width=600, height=400,
                 labels={'person_name':'이름','person_age':'나이'},
                 color_discrete_map={"나이": "RebeccaPurple"},
                 template="simple_white",text='person_age')
    fig.update_layout(yaxis_range=[0,100])
    fig.show()
    
    conn.close()



def hist():
    df = px.data.tips()
    fig = px.histogram(df, x="total_bill", y="tip", color="sex", marginal="rug", hover_data=df.columns)
    fig.show()

def box():
    df = px.data.tips()
    fig = px.box(df, x="day", y="total_bill", color="smoker", notched=True)
    fig.show()

def scatter3d():
    df = px.data.iris()
    df.head()
    fig = px.scatter_3d(df,
                        x='sepal_length',
                        y='sepal_width',
                        z='petal_width',
                        color='petal_length',
                        symbol='species',
                        opacity=0.7)
    fig.show()

def scatter():
    df = px.data.gapminder()
    df.head()
    fig = px.scatter(df.query("year==2007"), x="gdpPercap",
                     y="lifeExp", size="pop",
                     color="continent",
               hover_person_name="country", log_x=True, size_max=60)
    fig.show()

def line():
    df = px.data.gapminder()
    print( df.head() )
    df = px.data.gapminder().query("country=='Korea, Rep.'")
    fig = px.line(df, x="year", y="lifeExp", title='Life expectancy in Korea, Rep.')
    fig.show()


def pie():
    df = px.data.gapminder().query("year == 2007").query("continent == 'Europe'")
    df.loc[df['pop'] < 2.e6, 'country'] = 'Other countries' # Represent only large countries
    fig = px.pie(df, values='pop', person_names='country', title='Population of European continent')
    fig.show()

# bar()
student()
# hist()
# box()
# scatter3d()
# scatter()
# line()
# pie()

# c = con.cursor()
# c.execute('select * from student')
# result = c.fetchall()