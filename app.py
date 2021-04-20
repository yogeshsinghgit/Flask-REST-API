from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

books = [
        {'name':'java', 'author':"Author1",'price':240},
        {'name':'Python', 'author':"Author2",'price':300},
        {'name':'java Programming', 'author':"Author1",'price':240},
        {'name':'C programming', 'author':"Author3",'price':500},
        {'name':'C ++', 'author':"Author4",'price':400}
         ]

@app.route('/')
def home():
    return "<h1>Home Page</h1>"

@app.route('/books')
def get_books():
    global books
    return {'books':books}

@app.route('/book/<name>')
def get_book(name):
    global books
    output_book = []
    for book in books:
        if name == book['name'].lower():
            output_book.append(book)
    return {'result':output_book}
            
    

if __name__ == "__main__":
    app.run(debug=True)
    