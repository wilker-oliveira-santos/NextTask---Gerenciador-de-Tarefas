from flask import Blueprint,render_template,request

cad_route  = Blueprint('cadastrar', __name__)

tarefas_nome = []
tarefas_data = []
tarefa_nivel = []

@cad_route.route('/cadastro', methods=['POST'])
def cad_tarefas():
    task = request.form['task']
    data = request.form['data_task']
    nivel = request.form['nivel']

    if(nivel=="moderado"):
        tarefa_nivel.append("MODERADO")
    else:
        tarefa_nivel.append("URGENTE")
    

    tarefas_nome.append(task)
    tarefas_data.append(data)
    return render_template('home.html', tarefas=tarefas_nome, data=tarefas_data, nivel=tarefa_nivel) 
    

