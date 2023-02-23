import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()

def create_app():
  from .models import Book
  app = Flask(__name__,instance_path=os.getcwd(),instance_relative_config=True)
  app.config.from_pyfile('config.py')
  db.init_app(app)
  migrate = Migrate(app,db)
  
  @app.route('/')
  def index():
      books = db.session.query(Book).all()
      return render_template("index.html", books = books)
  @app.route('/addbook',methods=['GET','POST'])
  def addbook():
      if request.method == 'POST':
          title = request.form['booktitle']
          author = request.form['bookauthor']
          book = Book(booktitle=title,bookauthor=author)
          db.session.add(book)
          db.session.commit()
            
          return redirect(url_for('index'))
       return redirect(url_for('index'))

  
  return app
  
