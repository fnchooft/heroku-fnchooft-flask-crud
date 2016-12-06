Flask Heroku Sample
====================

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

## Development Setup

* `virtualenv venv`
* `source venv/bin/activate`
* `pip install -r requirements.txt`

## Deploy
### Heroku cli / Command line
* `heroku create`
* `heroku addons:create heroku-postgresql:hobby-dev`
* `git push heroku master`


### Heroku Github-connection
One can connect a github-repository via Heroku.
Enter into your heroku-account, choose `Github` as your `Deployment method`. In order for this to work you must pass your credentials in order to allow heroku to connect to your github-repository.

After the connection has been established go to the
`Manual deploy`-option and choose your branch.


## Author
 * [Fabian N.C. van 't Hooft](https://twitter.com/FabianHooft)


## Inspired by
 * [Yefim's Example](https://github.com/yefim/flask-heroku-sample)


## Links
 * [Heroku Dashboard](https://dashboard.heroku.com)
 * [Python PIP](http://docs.python-guide.org/en/latest/starting/install/linux)
 * [Python Virtual Environments](http://docs.python-guide.org/en/latest/dev/virtualenvs)
 * [Flask and SQLite3](http://flask.pocoo.org/docs/0.11/patterns/sqlite3)
