from flask import Flask,request, jsonify
import sqlite3
import pymysql

app = Flask(__name__)


def db_connection():
    conn = None
    try:
        # conn = sqlite3.connect("books.sqlite")
        conn = pymysql.connect(host= 'sql11.freesqldatabase.com',
        database = 'sql11493041',
        user= 'sql11493041',
        password= 'R3EH8RhAww',
        charset = 'utf8mb4',
        cursorclass = pymysql.cursors.DictCursor
            
        )
    # except sqlite3.error as e:
    except pymysql.Error as e:
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
    cursor = conn.cursor()
    
    
    if request.method == "GET":
        cursor.execute("select * from book")
        
        books = [
            dict(id=book['id'], author=book['author'], language=book['language'], title=book['title'])
            for book in cursor.fetchall()
        ]
        
        if len(books) >0:
            conn.close()
            return jsonify(books)
        else:
            'Nothing Found', 404

    if request.method == "POST":
        new_author = request.form["author"]
        new_lang = request.form["language"]
        new_title = request.form["title"]
        sql = """INSERT INTO book (author, language, title)
                 VALUES (%s, %s, %s)"""
        cursor.execute(sql, (new_author, new_lang, new_title))
        conn.commit()
        cursor = conn.cursor()
        # new_book = {
        #     "id": id,
        #     "author": author,
        #     "language": language,
        #     "title": title,
        # }
        last_row_sql = 'select *from book ORDER BY id DESC LIMIT 1;'
        cursor.execute(last_row_sql)
        
        return f"Book {cursor.fetchone()} created successfully"



@app.route('/book/<int:id>',methods = ['GET','PUT',"DELETE"])
def single_book(id):
    conn = db_connection()
    cursor = conn.cursor()

    if request.method == "GET":
        cursor.execute("SELECT * FROM book WHERE id=%s", (id,))
        try:
            thebook = cursor.fetchall()[0]
            return f" your book was {thebook}"
        except:
            return "No Book Found" ,404


    if request.method == "PUT":
        sql = """UPDATE book
                SET title=%s,
                    author=%s,
                    language=%s
                WHERE id=%s """
        author = request.form["author"]
        language = request.form["language"]
        title = request.form["title"]
        updated_book = {
            "id": id,
            "author": author,
            "language": language,
            "title": title,
        }
        cursor.execute(sql, (author, language, title, id))
        conn.commit()
        conn.close()
        return jsonify(updated_book)


    if request.method == "DELETE":
        sql = """ DELETE FROM book WHERE id=%s """
        cursor.execute(sql, (id,))
        conn.commit()
        conn.close()
        return f"The book with id: {id} has been deleted.", 200



# # dynamic routing
# @app.route('/<name>')
# def print_name(name):
#     return f'hi, {name}'


if __name__ == "__main__":
    app.run(debug = True)

# ## commend line option 

