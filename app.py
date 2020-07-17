import os
import flask


SECRET_PATH = os.getenv('SECRET_PATH', '')

app = flask.Flask('baby-everyday', static_url_path=f'/static/{SECRET_PATH}')


@app.route('/')
def index():
    return flask.render_template('index.html')


@app.route(f'/babies/{SECRET_PATH}')
def babies():
    return flask.render_template('babies.html', secret_path=SECRET_PATH)
