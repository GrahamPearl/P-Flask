import datetime
from markupsafe import escape
from flask import Flask, abort, render_template
app = Flask(__name__)


@app.route('/')
@app.route('/index/')
def hello_world():
    return render_template('index.html', utc_dt=datetime.datetime.utcnow())

@app.route('/capitalize/<word>/')
def capitalize(word):
    return '<h1>{}</h1>'.format(escape(word.capitalize()))

@app.route('/users/<int:user_id>/')
def greet_user(user_id):
    users = ['Bob', 'Jane', 'Adam']
    try:
        return '<h2>Hi {}</h2>'.format(users[user_id])
    except IndexError:
        abort(404)

@app.route('/about/')
def about():
    return '<h3>This is a Flask web application.</h3>'

if __name__ == '__main__':
    app.run()