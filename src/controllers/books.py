from flask_restx import Resource

from src.server.instance import server

app, api = server.app, server.api

books_db = [
  {'id': 0, 'title': 'asdf'},
  {'id': 1, 'title': 'asdf'}
]


@api.route('/books')
class BookList(Resource):
  def get(self, ):
    return books_db


@app.route('/')
def homepage():
  return 'funcionando'
