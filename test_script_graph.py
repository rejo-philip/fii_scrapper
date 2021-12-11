# %matplotlib qt
import pandas as pd
import plotly.offline as pyo
import plotly.graph_objects as go

# fig = go.Figure(data=[
#             go.Scatter(x=df_report_excel.index, y=df_report_excel['point']),
#             go.Scatter(x=df_report_excel.index, y=df_report_excel['cumsum'])])

fii_data = pd.read_csv('fo_participant_data_01_02_2021-15_02_2o21.csv.csv')
fii_string = 'FII'
fii_data = fii_data.query('@fii_string ==`Client Type`')
print(fii_data.head())
nifty_data = pd.read_csv('nifty_50_data.csv')


pyo.init_notebook_mode()

data=[go.Scatter(x=fii_data['Date'], y=fii_data['Future Index Long'],mode='lines',line=dict(color='red')),
      go.Scatter(x=fii_data['Date'], y=fii_data['Future Index Short'],mode='markers',marker=dict(color='red')),
      go.Scatter(x=fii_data['Date'], y=fii_data['Option Index Call Long'],mode='lines',line=dict(color='green')),
      go.Scatter(x=fii_data['Date'], y=fii_data['Option Index Put Long'],mode='markers',marker=dict(color='green')),

      ]
# data=[go.Scatter(x=fii_data['Date'], y=fii_data['Future Index Long'],mode='lines',lines=dict(color='red')),
#       go.Scatter(x=fii_data['Date'], y=fii_data['Option Index Call Long'],mode='lines',lines=dict(color='green')),
#       go.Scatter(x=fii_data['Date'], y=fii_data['Option Index Put Long'],mode='markers',marker=dict(color='green')),
#         go.Scatter(x=fii_data['Date'], y=fii_data['Option Index Put Long'],mode='markers',marker=dict(color='green'))

#       ]
# data=[go.Scatter(fii_data,x = 'Date', y = 'Future Index Long'),
#       go.Scatter(fii_data,x = 'Date' , y = 'Option Index Call Long'),]

pyo.iplot(data, filename = 'basic-line')




data=[go.Bar(x=fii_data['Date'], y=fii_data['Future Index Long'],mode='lines',line=dict(color='red')),
      go.Bar(x=fii_data['Date'], y=fii_data['Future Index Short'],mode='markers',marker=dict(color='red')),
      go.Bar(x=fii_data['Date'], y=fii_data['Option Index Call Long'],mode='lines',line=dict(color='green')),
      go.Bar(x=fii_data['Date'], y=fii_data['Option Index Put Long'],mode='markers',marker=dict(color='green')),

      ]
# data=[go.Scatter(x=fii_data['Date'], y=fii_data['Future Index Long'],mode='lines',lines=dict(color='red')),
#       go.Scatter(x=fii_data['Date'], y=fii_data['Option Index Call Long'],mode='lines',lines=dict(color='green')),
#       go.Scatter(x=fii_data['Date'], y=fii_data['Option Index Put Long'],mode='markers',marker=dict(color='green')),
#         go.Scatter(x=fii_data['Date'], y=fii_data['Option Index Put Long'],mode='markers',marker=dict(color='green'))

#       ]
# data=[go.Scatter(fii_data,x = 'Date', y = 'Future Index Long'),
#       go.Scatter(fii_data,x = 'Date' , y = 'Option Index Call Long'),]

pyo.iplot(data, filename = 'basic-line')