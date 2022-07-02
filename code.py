import pandas as pd 
import plotly.express as px

df = pd.read_csv('data.csv')

Xdate = df['date']
Ycases = df['cases']
Ccolor = df['country']

fig = px.scatter(df, x = 'date', y = 'cases', color = 'country')
#This is just so I know the code works because there is a large buffer prior to the graph loading.
print('loading...')
fig.show()
