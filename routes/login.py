from flask import Blueprint,render_template,request

login_route = Blueprint('login', __name__)

cad_email = []

@login_route.route('/')
def login():
    return render_template('index.html')

"""@login_route.route('/home', methods=['POST'])
def receber_dados():

    email = request.form['email']
    nome = request.form['nome']


    cad_email.append(email)
    return render_template('home.html', email=email, list=list , nome=nome, cad_email=cad_email)"""


