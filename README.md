# Baby Everyday

Show the photos of the babies growing up.

## Demo

Please go to <https://baby-everyday.herokuapp.com/babies/771AB247-A099-4F64-BD01-6F3461F5D103> and see a chick and a frog growing up.


## Usage


### Running on Local

1. Git clone this repo.
1. Install required packages: `pip3 install flask photoage`
1. Replace the photos in `./static/photos/left` and `./static/photos/right` with your babies photos.
1. (Optional) replace the photo in `./static/photos/sorry` with your customized apology photo.
1. Run `flask run`.
1. Check <http://127.0.0.1:5000/babies>.


### Deploy to Heroku

1. Done the steps above to make sure it can run on local.
1. Create a Heroku app.
1. Git commit the changes and push it to your Heroku app.
1. Check the Heroku URL.


### Environment Variables

There are several environment variables to config:

1. `WEBPAGE_TITLE`: The title of the webpage.
1. `SECRET_PATH`: You can use it to protect your babies photos if you don't want everyone to see them. Setting `SECRET_PATH` will change the URL from `/babies` to `/babies/<SECRET_PATH>`.
1. `STARTUP_DAY`: The days showing up when open the web page. Defaults to `0`.
1. `LEFT_BIRTHDAY`: The birthday of your first baby. Will auto detect if not set.
1. `RIGHT_BIRTHDAY`: The birthday of your second baby. Will auto detect if not set.
1. `PHOTOAGE_OFFSET`: Apply an offset to the cutting point. Defaults to `12:00:00`.
