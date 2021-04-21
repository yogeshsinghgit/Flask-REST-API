from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    author = db.Column(db.String(100))
    price = db.Column(db.Integer)
    
    def __repr__(self):
        return f"{self.name}-{self.author}-{self.price}"
    


@app.route('/')
def home():
    return "<h1>Home Page</h1>"

@app.route('/books')
def get_books():
    books = Book.query.all()
    output = []
    for book in books:
        book_data = {'id':book.id,'name':book.name,'author':book.author,'price':book.price}
        output.append(book_data)
    return {'books':output}


@app.route('/book/<id>')
def get_book(id):
    book = Book.query.get(id)
    if book:
        return {'id':book.id,'name':book.name,'author':book.author,'price':book.price}
    return {'result':'Null'}

@app.route('/book',methods=['POST'])
def add_book():
    pass

@app.route('/books/<id>',methods=['DELETE'])
def delete_book(id):
    book = Book.query.get(id)
    if book:
        db.session.delete(book)
        db.session.commit()
        return {'Message':"Data is Deleted"}
    
    return {"Message":"No Such Data Found"}
    

if __name__ == "__main__":
    app.run(debug=True)
    