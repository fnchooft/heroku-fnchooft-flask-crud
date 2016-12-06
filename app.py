import os
# ----------------------------------------------------------------------
# Simple 2 file flask application implementing a simple CRUD-interface
# ----------------------------------------------------------------------

from flask import Flask, render_template, request, redirect, url_for
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)

DATABASE_URL = os.environ.get('DATABASE_URL', 'sqlite:////tmp/flask_app.db')

# This url will be used by Heroku to inject the database.
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
db = SQLAlchemy(app)

# ----------------------------------------------------------------------
# Eventhough a nicer layout can be used with app/model/Thing.py in this 
# example simplicity was choosen.
# ----------------------------------------------------------------------
class Thing(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  type = db.Column(db.String(100))
  name = db.Column(db.String(100))

  def __init__(self, type,name):
    self.type = type
    self.name = name

db.create_all()

# ----------------------------------------------------------------------
# A very simplictic single view was choosen 
# Top part of page for addition of Things
# Lower part of page for editing and or deleting
# ----------------------------------------------------------------------

@app.route('/')
def index():
  return render_template('index.html', things=Thing.query.all())

# ----------------------------------------------------------------------
# This function adds a new Thing
# ----------------------------------------------------------------------
@app.route('/thing', methods=['POST'])
def thing():
  if request.method == 'POST':
    t = Thing(request.form['type'], request.form['name'])
    db.session.add(t)
    db.session.commit()
  return redirect(url_for('index'))

# ----------------------------------------------------------------------
# This function updates an existing Thing
# Error handling  is not implemented yet...
# ----------------------------------------------------------------------
@app.route('/thing/update', methods=['POST'])
def update_thing():
  if request.method == 'POST':
    thing_to_update = Thing.query.get(request.form['id'])
    app.logger.info('Found item - updating fields...')
    thing_to_update.type = request.form['type']
    thing_to_update.name = request.form['name']
    db.session.commit()
  return redirect(url_for('index'))

# ----------------------------------------------------------------------
# This function deletes an existing Thing
# Since the view is called the item should not show up anymore
# ----------------------------------------------------------------------
@app.route('/thing/delete', methods=['POST'])
def delete_thing():
  if request.method == 'POST':
    thing_to_delete = Thing.query.get(request.form['id'])
    db.session.delete(thing_to_delete)
    db.session.commit()
  return redirect(url_for('index'))


if __name__ == '__main__':
  port = int(os.environ.get('PORT', 5000))
  app.run(host='0.0.0.0', port=port)
