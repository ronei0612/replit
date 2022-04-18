from flask import Flask, Response, request
from flask_sqlalchemy import SQLAlchemy
import json


app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database2.db'
db = SQLAlchemy(app)


# Create database
class Usuario(db.Model):
  id = db.Column(db.Integer, primary_key= True)
  nome = db.Column(db.String(50))
  email = db.Column(db.String(100))

  def to_json(self):
      return {"id": self.id, "nome": self.nome, "email": self.email}


# Get all
@app.route("/usuarios", methods=["GET"])
def select_users():
  user_objects = Usuario.query.all()
  users_json = [user.to_json() for user in user_objects]

  return gerate_response(200, "usuarios", users_json)


# Get only onne
@app.route("/usuario/<id>", methods=["GET"])
def select_user(id):
  user_object = Usuario.query.filter_by(id=id).first()
  user_json = user_object.to_json()

  return gerate_response(200, "usuario", user_json)


# To register
@app.route("/usuario", methods=["POST"])
def create_user():
  body = request.get_json()

  try:
      user = Usuario(nome=body["nome"], email= body["email"])
      db.session.add(user)
      db.session.commit()
      return gerate_response(201, "usuario", user.to_json(), "Criado com sucesso")
  except Exception as e:
      print('Erro', e)
      return gerate_response(400, "usuario", {}, "Erro ao cadastrar")


# Update
@app.route("/usuario/<id>", methods=["PUT"])
def update_user(id):
  user_object = Usuario.query.filter_by(id=id).first()
  body = request.get_json()

  try:
      if('nome' in body):
          user_object.nome = body['nome']
      if('email' in body):
          user_object.email = body['email']
      
      db.session.add(user_object)
      db.session.commit()
      return gerate_response(200, "usuario", user_object.to_json(), "Atualizado com sucesso")
  except Exception as e:
      print('Erro', e)
      return gerate_response(400, "usuario", {}, "Erro ao atualizar")


# Delete
@app.route("/usuario/<id>", methods=["DELETE"])
def delete_user(id):
  user_object = Usuario.query.filter_by(id=id).first()

  try:
      db.session.delete(user_object)
      db.session.commit()
      return gerate_response(200, "usuario", user_object.to_json(), "Deletado com sucesso")
  except Exception as e:
      print('Erro', e)
      return gerate_response(400, "usuario", {}, "Erro ao deletar")


# Home Page
@app.route('/')
def homepage():
  return 'Funcionando'


def gerate_response(status, nome_do_conteudo, conteudo, mensagem=False):
  body = {}
  body[nome_do_conteudo] = conteudo

  if(mensagem):
      body["mensagem"] = mensagem

  return Response(json.dumps(body), status=status, mimetype="application/json")


app.run(host='0.0.0.0')