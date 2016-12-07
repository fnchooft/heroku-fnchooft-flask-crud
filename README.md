Flask Heroku Sample
====================

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

## Development Setup

* `virtualenv venv`
* `source venv/bin/activate`
* `pip install -r requirements.txt`

If you want to test from the command-line execute:

```bash
python app.py
```

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

The link to the deployed app is: [https://fnchooft-crud-test.herokuapp.com](https://fnchooft-crud-test.herokuapp.com)


## Curl-usage



### Add a Thing
```bash
curl --data 'type=House&name=Chalet03' http://localhost:5000/thing
```
on create no id is passed and a new primary key will be created.

### Update a Thing
```bash
curl --data 'id=1&type=Haus&name=Chalet03' http://localhost:5000/thing/update
```
on update the id must be passed since both the attributes type and name may be changed.

### Delete a Thing
```bash
curl --data 'id=1' http://localhost:5000/thing/delete
```
only the id (primary key) is needed to delete the thing. 

## Author
 * [Fabian N.C. van 't Hooft](https://twitter.com/FabianHooft)


## Inspired by
 * [Yefim's Example](https://github.com/yefim/flask-heroku-sample)


## Links
 * [Heroku Dashboard](https://dashboard.heroku.com)
 * [Python PIP](http://docs.python-guide.org/en/latest/starting/install/linux)
 * [Python Virtual Environments](http://docs.python-guide.org/en/latest/dev/virtualenvs)
 * [Flask and SQLite3](http://flask.pocoo.org/docs/0.11/patterns/sqlite3)
