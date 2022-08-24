from flask import Flask, render_template, request, redirect, session, flash, url_for

class Game:
    def __init__(self,name,category,console):
        self.name = name
        self.category = category
        self.console = console

game1 = Game("Tetris","Puzzle","Atari")
game2 = Game("God of War","Hack n Alash","PS2")
game3 = Game("Mortal Kombat","Luta","PS2")
listGames = [game1,game2,game3]
class Usuario:
    def __init__(self,nome,nickname,senha):
        self.nome = nome
        self.nickname = nickname
        self.senha = senha

usuario1 = Usuario("Matheus Biasi", "mhb","tesudo")
usuario1 = Usuario("Laura Weber", "gata","minhadeusa")
usuario3 = Usuario("Diego Bandeira", "Didi","corno")

usuarios = { usuario1.nickname : usuario1,
             usuario2.nickname : usuario2,
             usuario3.nickname : usuario3 }


app = Flask(__name__) #RESPONSAVEL POR CRIAR O SERVIDOR ONDE RODA A APLICACAO NA WEB
app.secret_key = 'alura'

@app.route('/') #responsavel pela criacao do "caminho" na URL
def index():
    titulo = "GAMES"
    return render_template('games.html',titulo = titulo,listGames = listGames)

@app.route('/newGame')
def newGame():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for(('newGame'))))
    titulo = "Cadastro de Novos GAMES"
    return render_template('newGame.html',titulo = titulo)

@app.route('/create',methods=['POST',])
def create():
    name = request.form['name']
    category = request.form['category']
    console = request.form['console']

    game = Game(name,category,console)
    listGames.append(game)

    return redirect(url_for('index'))

@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html')

@app.route('/autenticar',methods=['POST', ])
def autenticar():
    if request.form['usuario'] in usuarios:
        usuario = usuarios[request.form['usuario']]
        if request.form['senha'] == usuario.senha:
            session['usuario_logado'] = usuario.nickname
            flash(usuario.nickname['usuario'] + " logado com sucesso!")
            proxima_pagina = request.form['proxima']
            return redirect(proxima_pagina)
    else:
        flash('Usuario nao logado!')
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash("Logout efetuado com sucesso!")
    return redirect(url_for('index'))


app.run(debug=True)
