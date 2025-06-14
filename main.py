

from flask import Flask
from routes.login import login_route
from routes.cad_tarefas import cad_route
from routes.cad_tarefas import del_route
app = Flask(__name__)

app.register_blueprint(login_route)
app.register_blueprint(cad_route)
app.register_blueprint(del_route)

app.run(debug=True)