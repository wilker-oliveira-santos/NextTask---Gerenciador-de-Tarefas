from flask import Blueprint,render_template,request
from plyer import notification

cad_route  = Blueprint('cadastrar', __name__)
del_route  = Blueprint('deletar', __name__)
up_route  = Blueprint('update', __name__)

tarefas = []

@cad_route.route('/cadastro', methods=['POST'])
def cad_tarefas():
    task = request.form['task']
    data = request.form['data_task']
    nivel = request.form['nivel'].upper()

    tarefas.append({
        "tarefa": task,
        "data": data,
        "nivel": nivel
    })

    return render_template('home.html', tarefas=tarefas) 

@del_route.route('/delete', methods=['POST'])
def del_tarefa():
    id_tarefa = int(request.form['id'])
    tarefas.pop(id_tarefa)

    notification.notify(
        title='Next Task',
        message='Tarefa excluída com Sucesso!',
        app_icon='./static/images/favicon.ico', 
        timeout=0.1 
    )

    return render_template('home.html', tarefas=tarefas)

@up_route.route('/update', methods=['POST'])
def up_tarefa():
    id_tarefa = int(request.form['id'])
    tarefas.pop(id_tarefa)

    return render_template('home.html', tarefas=tarefas)
    

