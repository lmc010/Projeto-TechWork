from flask import render_template, request, url_for, redirect
from models.database import db, Alunos


aniversario = []

def init_app(app):
  
  @app.route('/')

  def home():
   
    return render_template('index.html')
  
  @app.route('/aniversarios', methods=['GET', 'POST'])

  def aniversarios():

    if request.method == 'POST':
       if request.form.get('aluno'):
         aniversario.append({request.form.get('aluno')})

         
          
    return render_template('aniversarios.html', aniversario=aniversario)
  
  @app.route('/cadalunos',  methods=['GET', 'POST'])
  @app.route('/cadalunos/delete/<int:id>')
  def cadalunos(id=None):
    if id:
        aluno = Alunos.query.get(id)
        db.session.delete(aluno)
        db.session.commit()
        return redirect(url_for('cadalunos'))
    if request.method == 'POST':
        novoaluno = Alunos(request.form['nome'], request.form['cidade'],
        request.form['email'], request.form['semestre'])
        db.session.add(novoaluno)
        db.session.commit()
        return redirect(url_for('cadalunos'))
    else:
        cadastroalunos = Alunos.query.all()
        return render_template('cadalunos.html', cadastroalunos=cadastroalunos)
    
  @app.route('/edit/<int:id>', methods=['GET', 'POST'])
  def edit(id):
    g = Alunos.query.get(id)  
    if request.method == 'POST':
        g.nome = request.form['nome']
        g.cidade = request.form['cidade']
        g.email = request.form['email']
        g.semestre = request.form['semestre']
        db.session.commit()
        return redirect(url_for('cadalunos'))
    return render_template('editalunos.html', g=g)


  @app.route('/sobre')

  def sobre():
   
    return render_template('sobre.html')
   

