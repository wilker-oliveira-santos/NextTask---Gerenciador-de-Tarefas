from flask import Blueprint,render_template,request

index_route = Blueprint('index', __name__)

@index_route.route('/')
def index():
    return render_template('index.html')

@index_route.route('/home')
def home():
    return render_template('home.html')
