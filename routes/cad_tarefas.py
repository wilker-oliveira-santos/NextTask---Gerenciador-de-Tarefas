from flask import Blueprint,render_template,request
from plyer import notification

cad_route  = Blueprint('cadastrar', __name__)
del_route  = Blueprint('deletar', __name__)
up_route  = Blueprint('update', __name__)
status_route  = Blueprint('stat', __name__)

tarefas = []
tarefas_andamento = []
tarefas_concluidas = []

@cad_route.route('/', methods=['GET', 'POST'])
@cad_route.route('/cadastro', methods=['GET', 'POST'])
def cad_tarefas():
    if request.method == 'POST':
        task = request.form['task']
        data = request.form['data_task']
        nivel = request.form['nivel'].upper()

        tarefas.append({
            "tarefa": task,
            "data": data,
            "nivel": nivel
        })

    return render_template('home.html',
        pendentes=tarefas,
        andamento=tarefas_andamento,
        concluidas=tarefas_concluidas
    )


@del_route.route('/delete', methods=['POST'])
def del_tarefa():
    id_tarefa = int(request.form['id'])
    origem = request.form['origem']

    if origem == 'pendente':
        tarefas.pop(id_tarefa)
    elif origem == 'andamento':
        tarefas_andamento.pop(id_tarefa)
    elif origem == 'concluida':
        tarefas_concluidas.pop(id_tarefa)

    notification.notify(
        title='Next Task',
        message='Tarefa excluída com Sucesso!',
        app_icon='./static/images/favicon.ico', 
        timeout=1
    )

    return render_template('home.html',
        pendentes=tarefas,
        andamento=tarefas_andamento,
        concluidas=tarefas_concluidas
    )

@up_route.route('/update', methods=['POST'])
def up_tarefa():
    id_tarefa = int(request.form['id'])
    origem = request.form['origem']

    if origem == 'pendente':
        tarefa = tarefas[id_tarefa]
    elif origem == 'andamento':
        tarefa = tarefas_andamento[id_tarefa]
    elif origem == 'concluida':
        tarefa = tarefas_concluidas[id_tarefa]
    else:
        return "Origem inválida", 400

    return render_template('update.html', tarefa=tarefa, id=id_tarefa, origem=origem)


@up_route.route('/salvar', methods=['POST'])
def salvar_tarefa_editada():
    id_tarefa = int(request.form['id'])
    origem = request.form['origem']
    nova_tarefa = {
        "tarefa": request.form['tarefa'],
        "data": request.form['data'],
        "nivel": request.form['nivel'].upper()
    }

    if origem == 'pendente':
        tarefas[id_tarefa] = nova_tarefa
    elif origem == 'andamento':
        tarefas_andamento[id_tarefa] = nova_tarefa
    elif origem == 'concluida':
        tarefas_concluidas[id_tarefa] = nova_tarefa
    else:
        return "Origem inválida", 400

    return render_template('home.html',
        pendentes=tarefas,
        andamento=tarefas_andamento,
        concluidas=tarefas_concluidas
    )

tCon = []
@status_route.route('/atualiza_status', methods=['POST'])
def atualiza_status():
    id_tarefa = int(request.form['id'])
    status = request.form['status']
    origem = request.form['origem']

    if origem == 'pendente':
        tarefa = tarefas.pop(id_tarefa)
    elif origem == 'andamento':
        tarefa = tarefas_andamento.pop(id_tarefa)
    elif origem == 'concluida':
        tarefa = tarefas_concluidas.pop(id_tarefa)
    else:
        return "Origem inválida", 400

    # Move para a nova lista
    if status == 'pendente':
        tarefas.append(tarefa)
    elif status == 'em_andamento':
        tarefas_andamento.append(tarefa)
    elif status == 'concluido':
        tarefas_concluidas.append(tarefa)

    return render_template('home.html',
        pendentes=tarefas,
        andamento=tarefas_andamento,
        concluidas=tarefas_concluidas
    )