

from flask import Flask
from routes.login import login_route

app = Flask(__name__)

app.register_blueprint(login_route)


app.run(debug=True)