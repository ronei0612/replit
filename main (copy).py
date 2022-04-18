from flask import Flask, jsonify
import sqlalchemy

# conecta ao banco
engine = sqlalchemy.create_engine('sqlite:///database.db', echo=True)

# declara o mapeamento
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class User(Base):
  __tablename__ = 'users'
  id = Column(Integer, primary_key=True)
  name = Column(String(50))

  def __repr__(self):
    return "<User(name={})>".format(self.name)

Base.metadata.create_all(engine)
################################

user = User(name='ronei')


# cria uma sessão
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
#Session
sessionmaker(class_='Session', bind=Engine(sqlite:///database.db), autoflush=True, autocommit=False, expire_on_commit=True)

session = Session()
session.add(user)
session.commit()
'''
session.add_all([
  User(name='asdf'),
  User(name='fff')
])
session.new
#User.__table__.drop(engine)
'''
#print(user.name)
'''
app = Flask(__name__)

@app.route('/')
def homepage():
  return jsonify('asdf')

@app.route('/contatos')
def contatos():
  return jsonify('asdf')

app.run(host='0.0.0.0')

'''