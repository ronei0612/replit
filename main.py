#from src.server.instance import server

#from src.controllers.books import *

#server.run()




from flask import Flask

app = Flask(__name__)
app.run(host='0.0.0.0')

@app.route('/')
def homepage():
  return 'funcionando'