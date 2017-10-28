from bottle import route, run, template
from bokeh.plotting import figure
from bokeh.embed import components

@route('/')
def hello():
    plot = figure()
    plot.circle([1,2], [3,4])

    script, div = components(plot)
    return template('bobo', script=script, div=div)

run(host='localhost', port=8080, debug=True)
