from bottle import run, template, get, post, redirect, request
from bokeh.plotting import figure
from bokeh.embed import components

@get('/')
def index():
    return template('index')

@post('/post')
def post():
    age = request.forms.get('age')
    redirect('/result/{}'.format(age))

@get('/result/<age>')
def result(age='XX'):
    plot = figure()
    plot.circle([1,2], [3,4])

    script, div = components(plot)
    return template('bobo', script=script, div=div, age=age)

run(host='localhost', port=8080, debug=True)
