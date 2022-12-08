
import plotly.express as px
import pandas as pd

df=pd.read_csv('rfile/race.csv')
# print(df)

# fig = px.bar(df, x='race', y='Male')
# fig.show()

temp = pd.melt(df,id_vars=['race'], var_name='gender',value_name='value')
print(temp)
print(len(temp))

# fig = px.bar(temp, x='race', y='value', color='gender')
# fig.show()

# fig = px.bar(temp, x='race', y='value', color='gender',barmode='group')
# fig.show()

# fig = px.bar(temp, x='race', y='value', color='gender',barmode='group',facet_row='gender')
# fig.show()

fig = px.bar(temp, x='race', y='value', color='gender',barmode='group',facet_col='gender')
fig.show()
