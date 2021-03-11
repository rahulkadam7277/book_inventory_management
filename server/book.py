from flask import Flask, render_template, request, jsonify
from flask import Flask
import sqlite3 as sql
import requests
import random

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index1.html')



@app.route('/book', methods=['GET'])
def addrec():
    for i in ('history', 'Drama', 'love', 'Mystery', 'Romance', 'Thriller', 'Contemporary'):
        googleapikey = 'AIzaSyAUi6gnlRcWFCUKpqV33Mjuq_DTvMGLAOU'
        parms = {"q": i, 'key': googleapikey}
        r = requests.get(url="https://www.googleapis.com/books/v1/volumes", params=parms)
        my_json = r.json()

        for item in my_json["items"]:
            book = {}
            book['id']=item['id']


            if "title" in item['volumeInfo']:
                book['title'] = item['volumeInfo']['title']
            else:
                book['title'] = ""
            if "authors" in item['volumeInfo']:
                book['authors'] = item['volumeInfo']['authors'][0]
            else:
                book['authors'] = ""
            if "publisher" in item['volumeInfo']:
                book['publisher'] = item['volumeInfo']['publisher']
            else:
                book['publisher'] = ""
            if "description" in item['volumeInfo']:
                book['description'] = item['volumeInfo']['description']
            else:
                book['description'] = ""
            if "pageCount" in item['volumeInfo']:
                book['pageCount'] = item['volumeInfo']['pageCount']
            else:
                book['pageCount'] = ""
            if "averageRating" in item['volumeInfo']:
                book['averageRating'] = item['volumeInfo']['averageRating']
            else:
                book['averageRating'] = ""
            if "imageLinks" in item['volumeInfo']:
                book['imageLink'] = item['volumeInfo']['imageLinks']['thumbnail']
            else:
                book['imageLink'] = ""
            if "previewLink" in item['volumeInfo']:
                book['previewLink'] = item["volumeInfo"]["previewLink"]
            else:
                book['previewLink'] = ""

            book['bookCount'] = random.randint(0, 20)
            if book['bookCount']==0:
                book['isAvailable'] = 'Book not available in inventory'
            else:
                book['isAvailable'] = 'Book available in inventory'





            with sql.connect("database.db") as con:
                cur = con.cursor()

            cur.execute("INSERT INTO booksinfo VALUES (?,?,?,?,?,?,?,?,?,?,?)",
                        (book['id'] ,book['title'],book['authors'],book['publisher'],book['description'],book['pageCount'],
                         book['averageRating'],book['imageLink'],book['previewLink'],book['bookCount'],book['isAvailable']))
            con.commit()

    return "Record successfully added"


@app.route('/selectgener', methods=['GET'])
def selectgener():
    with sql.connect("database.db") as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM booksinfo")
        data = cur.fetchall()

        if len(data) == 0:
            return('This inventory is empty')
        else:
            books = []
            for row in data:
                book = {}
                book["bookID"]=row[0]
                book["title"] = row[1]
                book["authors"] = row[2]
                book["publisher"] = row[3]
                book["description"] = row[4]
                book["pageCount"] = row[5]
                book["averageRating"] = row[6]
                book["imageLink"] = row[7]
                book["previewLink"] = row[8]
                book["bookCount"] = row[9]
                book["isAvailable"] = row[10]


                books.append(book)

    return jsonify(books)


@app.route('/searchbook', methods=['POST'])
def searchbook():
    _json = request.json
    book_search = _json['book_name']

    googleapikey = 'AIzaSyAUi6gnlRcWFCUKpqV33Mjuq_DTvMGLAOU'
    parms = {"q": book_search, 'key': googleapikey}

    print("in try")
    r = requests.get(url="https://www.googleapis.com/books/v1/volumes", params=parms)
    my_json = r.json()
    books = []
    for item in my_json["items"]:
        book = {}
        book['id']=item['id']
        book['title'] = item['volumeInfo']['title']
        book['previewLink'] = item['volumeInfo']['previewLink']
        if "imageLinks" in item['volumeInfo']:
            book['imageLink'] = item['volumeInfo']['imageLinks']['thumbnail']
        else:
            book['imageLink'] = ""
        with sql.connect("database.db") as con:
            cur = con.cursor()
        cur.execute("SELECT * FROM booksinfo WHERE bookID = ?", (book['id'],))
        data = cur.fetchall()
        if len(data) == 0:
            book['isAvailable'] = 'This item is not available in the inventory'
        else:
            book['isAvailable'] = 'This item is available in the inventory'
        books.append(book)
    return jsonify(books)





@app.route('/searchbookbyid', methods=['POST'])
def fetchbyid():
    _json = request.json
    book_id = _json['id']
    with sql.connect("database.db") as con:
        cur = con.cursor()
    cur.execute("SELECT * FROM booksinfo WHERE bookID = ?", (book_id,))
    data = cur.fetchall()
    if len(data) == 0:
        return('This item is not available in the inventory')
    else:

        books = []
        for row in data:
            book = {}
            book["bookID"] = row[0]
            book["title"] = row[1]
            book["authors"] = row[2]
            book["publisher"] = row[3]
            book["description"] = row[4]
            book["pageCount"] = row[5]
            book["averageRating"] = row[6]
            book["imageLink"] = row[7]
            book["previewLink"] = row[8]
            book["bookCount"] = row[9]
            book["isAvailable"] = row[10]

            books.append(book)

        return jsonify(books)


@app.route('/edit', methods=['POST'])
def edit():
    _json = request.json
    book_id = _json['id']
    count = _json['new_count']
    with sql.connect("database.db") as con:
        cur = con.cursor()
    # cur.execute('''UPDATE booksinfo SET book_count = ? WHERE id = ?''', (count, test_id))
    cur.execute(
        "UPDATE booksinfo SET bookCount = ?  WHERE bookID= ?",
        (count, book_id))
    con.commit()
    return "Record updated"
@app.route('/delete', methods=['POST'])
def delete():
    _json = request.json
    book_id = _json['id']
    with sql.connect("database.db") as con:
        cur = con.cursor()
    # cur.execute('''UPDATE booksinfo SET book_count = ? WHERE id = ?''', (count, test_id))
    cur.execute(
        "DELETE from booksinfo  WHERE bookID= ?",
        (book_id,))
    con.commit()
    return "Record Deleted"


@app.route('/create', methods=['POST'])
def create():
    _json = request.json
    book_id = _json['id']
    book_count = _json['new_count']

    googleapikey = 'AIzaSyAUi6gnlRcWFCUKpqV33Mjuq_DTvMGLAOU'
    parms = {"q": book_id, 'key': googleapikey}
    r = requests.get(url="https://www.googleapis.com/books/v1/volumes", params=parms)
    my_json = r.json()

    for item in my_json["items"]:
        book = {}
        book['id'] = item['id']

        if "title" in item['volumeInfo']:
            book['title'] = item['volumeInfo']['title']
        else:
            book['title'] = ""
        if "authors" in item['volumeInfo']:
            book['authors'] = item['volumeInfo']['authors'][0]
        else:
            book['authors'] = ""
        if "publisher" in item['volumeInfo']:
            book['publisher'] = item['volumeInfo']['publisher']
        else:
            book['publisher'] = ""
        if "description" in item['volumeInfo']:
            book['description'] = item['volumeInfo']['description']
        else:
            book['description'] = ""
        if "pageCount" in item['volumeInfo']:
            book['pageCount'] = item['volumeInfo']['pageCount']
        else:
            book['pageCount'] = ""
        if "averageRating" in item['volumeInfo']:
            book['averageRating'] = item['volumeInfo']['averageRating']
        else:
            book['averageRating'] = ""
        if "imageLinks" in item['volumeInfo']:
            book['imageLink'] = item['volumeInfo']['imageLinks']['thumbnail']
        else:
            book['imageLink'] = ""
        if "previewLink" in item['volumeInfo']:
            book['previewLink'] = item["volumeInfo"]["previewLink"]
        else:
            book['previewLink'] = ""

        book['bookCount'] = book_count
        if book['bookCount'] == 0:
            book['isAvailable'] = 'Book not available in inventory'
        else:
            book['isAvailable'] = 'Book available in inventory'

        with sql.connect("database.db") as con:
            cur = con.cursor()

        cur.execute("INSERT INTO booksinfo VALUES (?,?,?,?,?,?,?,?,?,?,?)",
                    (book['id'], book['title'], book['authors'], book['publisher'], book['description'],
                     book['pageCount'],
                     book['averageRating'], book['imageLink'], book['previewLink'], book['bookCount'],
                     book['isAvailable']))
        con.commit()


        return "New book Added"




if __name__ == '__main__':
    app.run(debug=True)
