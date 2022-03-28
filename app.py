import datetime
from markupsafe import escape
from flask import Flask, abort, render_template
app = Flask(__name__)


@app.route('/')
@app.route('/index/')
def hello_world():
    return render_template('index.html', utc_dt=datetime.datetime.utcnow())

@app.route('/login/<int:user_id>/')
def greet_user():    
    try:
        return render_template('index.html', utc_dt=datetime.datetime.utcnow())
    except IndexError:
        abort(404)

@app.route('/about/')
def about():
    return render_template('about.html', utc_dt=datetime.datetime.utcnow())

if __name__ == '__main__':
    app.run(debug=True)