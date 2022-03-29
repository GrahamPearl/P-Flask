import datetime
import book_controller
#from markupsafe import escape
from flask import Flask, abort, render_template, jsonify, request
app = Flask(__name__)


@app.route('/')
@app.route('/index/')
def hello_world():
    return render_template('index.html', utc_dt=datetime.datetime.utcnow())

@app.route('/login/')
def greet_user():    
    try:
        return render_template('login.html', utc_dt=datetime.datetime.utcnow())
    except IndexError:
        abort(404)

@app.route('/books', methods=["GET"])
def get_books():
    books = book_controller.get_books()
    return jsonify(books)

@app.route("/book", methods=["POST"])
def insert_game():
    book_details = request.get_json()    
    result = book_controller.insert_game(book_details["name"], book_details["price"], book_details["email"])
    return jsonify(result)

@app.route('/book/', methods=["PUT"])
def update_book():
    book_details = request.get_json()    
    result = book_controller.update_list(book_details["id"], book_details["name"], book_details["price"], book_details["email"])
    return jsonify(result)

@app.route('/about/')
def about():
    return render_template('about.html', utc_dt=datetime.datetime.utcnow())

if __name__ == '__main__':
    app.run(debug=True)