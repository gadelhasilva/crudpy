from flask import Flask, render_template, request, redirect, url_for

app = Flask (__name__)

#Armazenamento temporario dos dados
tarefas = [
    {"id": 1, "titulo": "exemplo", " descricao": "exemplo"},
    
]

@app.route('/')
def index():
    return render_template('index.html', tarefas=tarefas)

@app.route('/nova', methods=['GET','POST'])  #adicionar 
def nova():
    if request.method == 'POST':
        nova_tarefa = {
         "id": len(tarefas) + 1,
        "titulo": request.form['titulo'],
        "descricao": request.form[' descricao']
        }
        tarefas.append(nova_tarefa)
        return redirect(url_for('index'))
    return render_template('nova.html')

@app.route('/editar/<int:id>', methods=['GET','POST']) #editar
def editar(id):
    tarefa = next((t for t in tarefas if t["id"] == id), None)
    if not tarefa:
        return "Tarefa não encontrada", 404

    if request.method == 'POST':
        tarefa['titulo'] = request.form['titulo']
        tarefa['descricao'] = request.form[' descricao']
        return redirect(url_for('index'))

    return render_template('editar.html', tarefa=tarefa)

@app.route('/excluir/<int:id>', methods=['POST']) #excluir
def excluir(id):
    global tarefas
    tarefas = [t for t in tarefas if t["id"] != id]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
