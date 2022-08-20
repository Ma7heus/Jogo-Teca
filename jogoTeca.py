from flask import Flask, render_template

class Game:
    def __init__(self,name,category,console):
        self.name = name
        self.category = category
        self.console = console

app = Flask(__name__) #RESPONSAVEL POR CRIAR O SERVIDOR ONDE RODA A APLICACAO NA WEB

@app.route('/inicio') #responsavel pela criacao do "caminho" na URL
def carregaGames():
    game1 = Game("Tetris","Puzzle","Atari")
    game2 = Game("God of War","Hack n Alash","PS2")
    game3 = Game("Mortal Kombat","Luta","PS2")
    listGames = [game1,game2,game3]
    titulo = "GAMES"

    return render_template('games.html',titulo = titulo,listGames = listGames)

@app.route('/newGame')
def newGame():
    titulo = "Cadastro de Novos GAMES"
    return render_template('newGame.html',titulo = titulo)

app.run() #RODA A APLICACAO