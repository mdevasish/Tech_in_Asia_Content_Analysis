# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 12:13:59 2020

@author: mdevasish
"""

import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
from dash.exceptions import PreventUpdate
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
from ast import literal_eval
from nltk.tokenize import sent_tokenize,word_tokenize
import time

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

def read_files():
    '''
    Read necessary files and return the dataframe and list of the index
    '''
    df = pd.read_csv('./Results/final.csv',index_col = 'id')
    return df,list(set(df.index))

df,index = read_files()
    
text_content = '''
Topic 0: 0.003*"bank" + 0.003*"aim" + 0.002*"brand" + 0.002*"sell" + 0.002*"develop" + 0.002*"deal" + 0.002*"expand" + 0.002*"strategy" + 0.002*"claim" + 0.002*"gojek" + 0.002*"transaction" + 0.002*"funding" + 0.002*"bring" + 0.002*"pandemic" + 0.002*"explain" + 0.002*"group" + 0.002*"announce" + 0.002*"scale" + 0.002*"money" + 0.002*"round"

Topic 1: 0.003*"pandemic" + 0.003*"cost" + 0.002*"expand" + 0.002*"network" + 0.002*"food_delivery" + 0.002*"brand" + 0.002*"delivery" + 0.002*"economy" + 0.002*"grab" + 0.002*"feature" + 0.002*"space" + 0.002*"gojek" + 0.002*"government" + 0.002*"home" + 0.002*"merchant" + 0.002*"aim" + 0.002*"shopee" + 0.002*"group" + 0.002*"operation" + 0.002*"enterprise"

Topic 2: 0.004*"grab" + 0.003*"chinese" + 0.003*"deal" + 0.003*"tiktok" + 0.002*"delivery" + 0.002*"gojek" + 0.002*"develop" + 0.002*"oyo" + 0.002*"round" + 0.002*"space" + 0.002*"serve" + 0.002*"group" + 0.002*"apps" + 0.002*"brand" + 0.002*"pandemic" + 0.002*"expand" + 0.002*"announce" + 0.002*"operation" + 0.002*"management" + 0.002*"program"

Topic 3: 0.004*"grab" + 0.002*"space" + 0.002*"deal" + 0.002*"fintech" + 0.002*"money" + 0.002*"develop" + 0.002*"claim" + 0.002*"logistics" + 0.002*"recently" + 0.002*"operation" + 0.002*"place" + 0.002*"expand" + 0.002*"scale" + 0.002*"merchant" + 0.002*"home" + 0.002*"account" + 0.002*"aim" + 0.002*"feature" + 0.002*"future" + 0.002*"exist"
'''

app = dash.Dash(__name__,external_stylesheets=external_stylesheets)
app.title = 'Tech in Asia - Articles'
server = app.server

layout = dict(
    autosize=True,
    automargin=True,
    margin=dict(
        l=30,
        r=30,
        b=20,
        t=40
    ),
    
    hovermode="closest",
    plot_bgcolor="#F9F9F9",
    paper_bgcolor="#F9F9F9",
    legend=dict(font=dict(size=10), orientation='h'),
)

def generate_plot(df):
    '''
    Function to generate a plot using the plotly express

    Parameters :
        df : Dataframe containing data on which the plot has to be built

    Returns the plot as html
    '''
    df['Topic'] = df['Topic'].astype('category')
    fig = px.bar(df,x = 'Topic', y = 'Percentage',title = 'Topic Distribution of the article',color = 'Topic',range_y=[0,100])
    fig.update_layout(clickmode='event+select',title_x = 0.5)
    return fig

@app.callback(
    [Output('auth_name','value'),
     Output('word_count','value'),
     Output('read_time','value'),
     Output('content_space','value'),
     Output('ner_org','value'),
     Output('ner_cntry','value'),
     Output('words','value')],
    [Input('id_dropdown','value')])
def populate_fields(value):
    '''
    Functions based on call back functionality. Call back functionality enables to render dynamic content based on the user inputs on the application.

    Parameters :
        value : Input value of the dropdown of the artilce ID.
    
    Returns dynamic content based on the input, output list consists of author name, word count, reading time, article, organisations and regions
    '''
    if value is None:
        raise PreventUpdate
    print('Working')
    text = df.loc[value,'content']
    sent = sent_tokenize(text)
    words = [word_tokenize(each) for each in sent]
    summer = sum([len(each) for each in words])
    return df.loc[value,'author.display_name'],summer,df.loc[value,'read_time'],df.loc[value,'content'],df.loc[value,'Organisations'],df.loc[value,'Locations'],text_content

@app.callback(
     Output('plot','figure'),
    [Input('id_dropdown','value'),
     Input('gload','value')])
def plot(value,load):
    '''
    Functions based on call back functionality. Call back functionality enables to render dynamic content based on the user inputs on the application.

    Parameters :
        value : Input value of the dropdown of the artilce ID.
    
    Returns plot of the topic distribution of the articles
    '''
    if value is None:
        raise PreventUpdate
    x = df.loc[value,'Topic_Mixture']
    print(x,type(x))
    x = literal_eval(x)
    new = []
    for each in x:
        new.append((each[0],each[1]*100))
    print(new)
    z = pd.DataFrame(new,columns = ['Topic','Percentage'])
    result = []
    if z.shape[0] == 4:
        return generate_plot(z)
    else:
        a = {0,1,2,3}
        s = {each[0] for each in x}
        diff = a-s
        for each in diff:
            result.append((each,0))
        final = z.append(pd.DataFrame(result,columns = ['Topic','Percentage']),ignore_index = True)
        return generate_plot(final)

@app.callback(Output('outLoading','children'),
              [Input('inLoading','value')])
def Loading(value):
    '''
    Function to implement a loading icon
    '''
    time.sleep(1)
    return True

@app.callback(Output('plot', 'style'),
             [Input('id_dropdown','value')])
def hide_graph(input):
    if input:
        return {'display':'block'}
    else:
        return {'display':'none'}

app.layout = html.Div([                          # complete_container
    
html.Div([
    html.Div([
        html.H2('Articles Profiler at Tech in Asia'),
        html.H4('Analysis Overview')
        ],
        className='ten columns'
        ),
    html.Img(src="https://cdn.techinasia.com/wp-content/uploads/2018/01/three-colored-logo.gif",
             className='two columns'
             )
            ],
            id="header",style = {'height':'18vh'},className='row',
        ),
    html.Hr(id = 'break'),
    html.Div([                         # Main Container start
        html.Div([                     # container_1 start
        html.Div([                     # container_Article start
            html.Label('ID of the Article'),
            dcc.Dropdown(id = 'id_dropdown',
                      options = [{'label' : x, 'value' : x} for x in index 
                                ],
                      placeholder = 'Enter the ID of the Article',
                      ),
            ],id = 'container_article',className='three columns'),
        html.Div([                     # container_Auth start
             html.Label('Author',style = {}),
             dcc.Textarea(id = 'auth_name',
                          style = {'text-align' : 'center',
                                   #'align-items' : 'center',
                                   #'vertical-align' : 'bottom',
                                   #'height' : '50%'
                                   },
                     #style={'width': '50%', 'height': 50},
                     className = 'mini_container'
                     )
                  ],id = 'container_Auth',className = 'three columns'),
        html.Div([
            html.Label('Word Count'),
            dcc.Textarea(id = 'word_count',
                        style = {'text-align' : 'center'},
                        className = 'mini_container'
                         )
            ],id = 'container_count',className = 'three columns'),
        html.Div([                     # container_time start
            html.Label('Read Time in Minutes'),
            dcc.Textarea(id = 'read_time',
                         style = {'text-align' : 'center'},
                         className = 'mini_container'
                         )
            ],id = 'container_time',className = 'three columns')
         ],id = 'container_1',style = {'height' : '10vh'},className = 'pretty_container'),
        html.Br(),
        html.Br(),
        html.Div([                      # container_2 start
            html.Div([                  # content_container start
                html.Label('Content'),
                dcc.Textarea(id = 'content_space',
                             #value = 'Null',
                             style = {'width' : '100%','height' : 350}
                             ),
                ],id = 'container_content',className = 'five columns'),
            html.Div([                  # plot_container start
                #html.Label('Topic Distribution'),
                dcc.Loading(id = 'gload',type = 'graph',children = dcc.Graph(id = 'plot',
                          style = {'height' : 350,'displayModeBar': False})),
                dcc.Loading(id = 'inLoading',type = 'circle',children = html.Div(id = 'outLoading'),fullscreen = True),
                dcc.Markdown('''
                             * Topic 0 : Funding and strategy plans of Gojek
                             * Topic 1 : Food and Goods delivery during pandemic by Grab, Gojek and Shopee
                             * Topic 2 : Unclear topic about Grab, Chinese Tiktok and Gojek
                             * Topic 3 : Expansion plans of Grab into Fintech space by acquiring Banking liscence
                             ''',
                             style = {'font-size' : 12})
                ],id = 'container_plot', className = 'seven columns')
            ],id = 'container_2',style = {'height' : '80vh','display' : 'flex'},className = 'pretty_container'),
        html.Br(),
        html.Br(),
        html.Div([                  # container_3 start
            html.Div([              # NER_container start
                html.Label('Named Entity Recognition for Organisations'),
                dcc.Textarea(id = 'ner_org',
                         #value = 'Null',
                         style = {'width' : '100%','height' : 125}),
                html.Br(),
                html.Label('Named Entity Recognition for Locations/Regions'),
                dcc.Textarea(id = 'ner_cntry',
                         #value = 'Null',
                         style = {'width' : '100%','height' : 125}),
                ],id = 'ner',className = 'five columns'),
            html.Div([
                html.Label('Word Distribution'),
                dcc.Textarea(id = 'words',
                             #value = text,
                             style = {'width' : '100%','height' : 300})
                ],id = 'word_dist',className = 'seven columns')
            ],id = 'container_3',style = {'height' : '50vh'},className = 'pretty_container')
        ],
        id = 'main_container',className = 'pretty_container',
        style={
        "display": "flex",
        "flex-direction": "column",
    })
     ]
    )

if __name__ == '__main__':
    app.server.run(debug=True, threaded=True, port=5000)