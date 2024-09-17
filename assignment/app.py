from flask import Flask, request
app = Flask(__name__)
from flask_sqlalchemy import SQLAlchemy


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(80), nullable=False)
    author = db.Column(db.String(40), nullable=False)
    publisher = db.Column(db.String(40), nullable=False)


    def __repr__(self):
        return f"{self.book_name} \nWritten by {self.author}\nPublished by {self.publisher}"




@app.route('/')
def index():
    return "Hello!"

@app.route("/books")
def get_books():
    books = Book.query.all()

    output = []
    for book in books:
        book_data = {"book_name": book.book_name, "author": book.author, "publisher": book.publisher}

        output.append(book_data)
        
    return {"books": output}

@app.route("/books/<id>")
def get_book(id):
    book = Book.query.get_or_404(id)
    return {"book_name": book.book_name, "author": book.author, "publisher": book.publisher}

@app.route("/books", methods=["POST"])
def add_book():
    book = Book(name=request.json["book_name"], description=request.json["author"], publisher=request.json["publisher"])
    db.session.add(book)
    db.session.commit()
    return {"id": book.id}

@app.route("/books/<id>", methods=["DELETE"])
def delete_book():
    book = Book.query.get(id)

    if Book is None:
        return "404"
    db.session.delete(book)
    db.session.commit()
    return {"message": "Book Deleted"}
