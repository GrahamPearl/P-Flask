from db import get_db

def insert_book(name, price, email):
    db = get_db()
    cursor = db.cursor()
    statement = "INSERT INTO books(name, price, email) VALUES (?, ?, ?)"
    cursor.execute(statement, [name, price, email])
    db.commit()
    return True

def update_book(id, name, price, email):
    db = get_db()
    cursor = db.cursor()
    statement = "UPDATE books SET name = ?, price = ?, email = ? WHERE id = ?"
    cursor.execute(statement, [name, price, email, id])
    db.commit()
    return True

def delete_book(id):
    db = get_db()
    cursor = db.cursor()
    statement = "DELETE FROM books WHERE id = ?"
    cursor.execute(statement, [id])
    db.commit()
    return True

def get_by_id(id):
    db = get_db()
    cursor = db.cursor()
    statement = "SELECT * FROM books WHERE id = ?"
    cursor.execute(statement, [id])
    return cursor.fetchone()


def get_books():
    db = get_db()
    cursor = db.cursor()
    query = "SELECT * FROM books"
    cursor.execute(query)
    #return cursor
    return cursor.fetchall()