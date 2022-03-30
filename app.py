import datetime
import book_controller
import json
import db
from flask import abort, render_template, jsonify, request, Flask
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

@app.route('/setup', methods=["GET"])
def db_setup():
    result = db.create_tables()
    return render_template('success.html', utc_dt=datetime.datetime.utcnow())

@app.route('/contacts', methods=["GET"])
def get_contacts():
    books = book_controller.get_books()    
    return render_template('contacts.html', books=books)

@app.route('/contact/<int:id>', methods=["GET"])
def get_contact(id):
    book_details = book_controller.get_by_id(id)
    return render_template('contacts.html', book=book_details)
    #return jsonify(book_details)

@app.route("/contact", methods=["POST"])
def insert_contact():
    book_details = request.get_json()    
    result = book_controller.insert_book(book_details["name"], book_details["price"], book_details["email"])
    return jsonify(result)

@app.route('/contact/<int:id>', methods=["PUT"])
def update_contact(id):
    book_details = request.get_json()    
    result = book_controller.update_list(book_details["id"], book_details["name"], book_details["price"], book_details["email"])
    return jsonify(result)

#==========================================================================================================================

@app.route('/books', methods=["GET"])
def get_books():
    books = book_controller.get_books()    
    return render_template('books.html', books=books)
    #return jsonify(books)
    #
    #

@app.route('/book/<int:id>', methods=["GET"])
def get_book(id):
    book_details = book_controller.get_by_id(id)
    return render_template('books.html', book=book_details)
    #return jsonify(book_details)

@app.route("/book", methods=["POST"])
def insert_book():
    book_details = request.get_json()    
    result = book_controller.insert_book(book_details["name"], book_details["price"], book_details["email"])
    return jsonify(result)

@app.route('/book/<int:id>', methods=["PUT"])
def update_book(id):
    book_details = request.get_json()    
    result = book_controller.update_list(book_details["id"], book_details["name"], book_details["price"], book_details["email"])
    return jsonify(result)

@app.route('/about/')
def about():
    return render_template('about.html', utc_dt=datetime.datetime.utcnow())

if __name__ == '__main__':
    app.run(debug=True)