import os

from flask import Flask, render_template, request, redirect, url_for
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)

DATABASE_URL = os.environ.get('DATABASE_URL', 'sqlite:////tmp/flask_app.db')

app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
db = SQLAlchemy(app)


class Thing(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  type = db.Column(db.String(100))
  name = db.Column(db.String(100))

  def __init__(self, type,name):
    self.type = type
    self.name = name

db.create_all()


@app.route('/')
def index():
  return render_template('index.html', things=Thing.query.all())


@app.route('/thing', methods=['POST'])
def thing():
  if request.method == 'POST':
    t = Thing(request.form['type'], request.form['name'])
    db.session.add(t)
    db.session.commit()
  return redirect(url_for('index'))

if __name__ == '__main__':
  port = int(os.environ.get('PORT', 5000))
  app.run(host='0.0.0.0', port=port)
