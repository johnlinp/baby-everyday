import flask

app = flask.Flask('baby-everyday')


@app.route('/')
def babies():
    return flask.render_template('babies.html')
