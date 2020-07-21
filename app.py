import os
import datetime
import flask
import photoage


WEBPAGE_TITLE = os.getenv('WEBPAGE_TITLE', 'Baby Everyday')
SECRET_PATH = os.getenv('SECRET_PATH', '')
STARTUP_DAY = int(os.getenv('STARTUP_DAY', '0'))
LEFT_BIRTHDAY = os.getenv('LEFT_BIRTHDAY')
RIGHT_BIRTHDAY = os.getenv('RIGHT_BIRTHDAY')
PHOTOAGE_OFFSET = os.getenv('PHOTOAGE_OFFSET')

app = flask.Flask('baby-everyday', static_url_path=f'/static/{SECRET_PATH}')


def detect_birthday(dir_path, file_names):
    get_date_time_options = {}
    first_date_time = None
    for file_name in file_names:
        file_path = os.path.join(dir_path, file_name)
        date_time = photoage.get_date_time(file_path, **get_date_time_options)
        if date_time is None:
            continue
        if first_date_time is None or date_time < first_date_time:
            first_date_time = date_time
    if first_date_time is not None:
        return first_date_time.strftime('%Y/%m/%d')


def generate_mapping(side, birthday, photoage_offset):
    dir_path = os.path.join('static', 'photos', side)
    file_names = os.listdir(dir_path)

    calculate_days_options = {}
    if birthday is None:
        birthday = detect_birthday(dir_path, file_names)
    if birthday:
        calculate_days_options['birthday'] = datetime.datetime.strptime(birthday, '%Y/%m/%d')
    if photoage_offset:
        offset_time = datetime.datetime.strptime(photoage_offset, '%H:%M:%S')
        calculate_days_options['offset'] = datetime.timedelta(hours=offset_time.hour, minutes=offset_time.minute, seconds=offset_time.second)

    mapping = {}
    for file_name in file_names:
        file_path = os.path.join(dir_path, file_name)
        days = photoage.calculate_days(file_path, **calculate_days_options)
        mapping[days] = f'/static/{SECRET_PATH}/photos/{side}/{file_name}'

    return mapping

def get_sorry_url():
    dir_path = os.path.join('static', 'photos', 'sorry')
    first_file_name, *_ = os.listdir(dir_path)
    return f'/static/{SECRET_PATH}/photos/sorry/{first_file_name}'

left_mapping = generate_mapping('left', LEFT_BIRTHDAY, PHOTOAGE_OFFSET)
right_mapping = generate_mapping('right', RIGHT_BIRTHDAY, PHOTOAGE_OFFSET)
sorry_url = get_sorry_url()


@app.route('/')
def index():
    return flask.render_template('index.html', title=WEBPAGE_TITLE)


@app.route(f'/babies/{SECRET_PATH}')
def babies():
    return flask.render_template('babies.html', title=WEBPAGE_TITLE, secret_path=SECRET_PATH, startup_day=STARTUP_DAY)


@app.route(f'/babies/{SECRET_PATH}/data.js')
def mapping():
    return flask.render_template('data.js', left_mapping=left_mapping, right_mapping=right_mapping, sorry_url=sorry_url)
