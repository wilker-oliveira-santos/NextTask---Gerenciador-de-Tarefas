

from flask import Flask
from routes.index import index_route
from routes.cad_tarefas import cad_route, del_route, up_route

app = Flask(__name__)

app.register_blueprint(index_route)
app.register_blueprint(cad_route)
app.register_blueprint(del_route)
app.register_blueprint(up_route) 

app.run(debug=True)
