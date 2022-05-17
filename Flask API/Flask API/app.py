from flask import Flask,request, jsonify
import sqlite3

app = Flask(__name__)


def db_connection():
    conn = None
    try:
        conn = sqlite3.connect("books.sqlite")
    except sqlite3.error as e:
        print(e)
    return conn



#create route

@app.route('/')
def index():
    return "Test 1 "

books_list = [

  {
     "id": 1,
     "language": "lan1",
     "edition": "1111",
     "author": "11111 Schildt"
  },
  {
     "id": 2,
     "language": "222",
     "edition": "thir222d",
     "author": "Her222bert Schildt"
  },
    {
     "id": 3,
     "language": "J33ava",
     "edition": "thi33rd",
     "author": "Herb3344ert Schildt"
  },  {
     "id": 4,
     "language": "4444",
     "edition": "thi444rd",
     "author": "Her444bert Schildt"
  },  {
     "id": 5,
     "language": "Ja5555va",
     "edition": "th5555ird",
     "author": "Herb5555ert Schildt"
  },  {
     "id": 6,
     "language": "Ja666va",
     "edition": "thir66d",
     "author": "Herbe666rt Schildt"
  },
  {
     "id": 7,
     "language": "C+77+",
     "edition": "seco77nd",
     "author": "E.Bala777gurusamy"
  }

  ]



@app.route('/books',methods = ['GET',"POST"])
def books():
    conn = db_connection()
    # cursor = conn.cursor()
    
    
    if request.method == "GET":
        cursor = conn.execute("select * from book")
        
        books = [
            dict(id=book[0], author=book[1], language=book[2], title=book[3])
            for book in cursor.fetchall()
        ]
        
        if len(books) >0:
            return jsonify(books)
        else:
            'Nothing Found', 404

    if request.method == "POST":
        new_author = request.form["author"]
        new_lang = request.form["language"]
        new_title = request.form["title"]
        sql = """INSERT INTO book (author, language, title)
                 VALUES (?, ?, ?)"""
        cursor = cursor.execute(sql, (new_author, new_lang, new_title))
        conn.commit()
        last_row_sql = 'select *from book ORDER BY id DESC LIMIT 1;'
        
        return f"Book {conn.execute(last_row_sql).fetchall()[0]} created successfully"



@app.route('/book/<int:id>',methods = ['GET','PUT',"DELETE"])
def single_book(id):
    conn = db_connection()
    cursor = conn.cursor()

    if request.method == "GET":
        cursor.execute("SELECT * FROM book WHERE id=?", (id,))
        try:
            thebook = cursor.fetchall()[0]
            return f" your book was {thebook}"
        except:
            return "No Book Found" ,404


    if request.method == "PUT":
        sql = """UPDATE book
                SET title=?,
                    author=?,
                    language=?
                WHERE id=? """
        author = request.form["author"]
        language = request.form["language"]
        title = request.form["title"]
        updated_book = {
            "id": id,
            "author": author,
            "language": language,
            "title": title,
        }
        conn.execute(sql, (author, language, title, id))
        conn.commit()
        return jsonify(updated_book)


    if request.method == "DELETE":
        sql = """ DELETE FROM book WHERE id=? """
        conn.execute(sql, (id,))
        conn.commit()
        return f"The book with id: {id} has been deleted.", 200



# # dynamic routing
# @app.route('/<name>')
# def print_name(name):
#     return f'hi, {name}'


if __name__ == "__main__":
    app.run(debug = True)

# ## commend line option 

