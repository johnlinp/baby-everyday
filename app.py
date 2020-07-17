import os
import flask


SECRET_PATH = os.getenv('SECRET_PATH', '')
STARTUP_DAY = int(os.getenv('STARTUP_DAY', '0'))

app = flask.Flask('baby-everyday', static_url_path=f'/static/{SECRET_PATH}')


@app.route('/')
def index():
    return flask.render_template('index.html')


@app.route(f'/babies/{SECRET_PATH}')
def babies():
    return flask.render_template('babies.html', secret_path=SECRET_PATH, startup_day=STARTUP_DAY)


@app.route(f'/babies/{SECRET_PATH}/data.js')
def mapping():
    left_mapping = {
        0: f'/static/{SECRET_PATH}/photos/left/IMG_20200717_232313.jpg',
        1: f'/static/{SECRET_PATH}/photos/left/IMG_20200717_232332.jpg',
        3: f'/static/{SECRET_PATH}/photos/left/IMG_20200717_232341.jpg',
    }
    right_mapping = {
        0: f'/static/{SECRET_PATH}/photos/right/IMG_20200717_232221.jpg',
        1: f'/static/{SECRET_PATH}/photos/right/IMG_20200717_232236.jpg',
        2: f'/static/{SECRET_PATH}/photos/right/IMG_20200717_232245.jpg',
        3: f'/static/{SECRET_PATH}/photos/right/IMG_20200717_232256.jpg',
    }
    sorry_url = f'/static/{SECRET_PATH}/photos/sorry/IMG_20200717_232425.jpg'
    return flask.render_template('data.js', left_mapping=left_mapping, right_mapping=right_mapping, sorry_url=sorry_url)
