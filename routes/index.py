from flask import Blueprint,render_template,request

index_route = Blueprint('index', __name__)

@index_route.route('/')
def index():
    return render_template('index.html')

@index_route.route('/home')
def home():
    return render_template('home.html')

"""@login_route.route('/home', methods=['POST'])
def receber_dados():

    email = request.form['email']
    nome = request.form['nome']


    cad_email.append(email)
    return render_template('home.html', email=email, list=list , nome=nome, cad_email=cad_email)"""


