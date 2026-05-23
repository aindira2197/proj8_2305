from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'

db = SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))


@app.route('/')
def home():

    books = Book.query.all()

    text = ""

    for book in books:
        text += f"{book.title}<br>"

    return text


@app.route('/add/<title>')
def add(title):

    book = Book(title=title)

    db.session.add(book)
    db.session.commit()

    return "Book Added"


if __name__ == '__main__':

    with app.app_context():
        db.create_all()

    app.run(debug=True)
