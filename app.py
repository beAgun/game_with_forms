from flask import Flask, render_template, request, redirect, url_for
from project.forms import MyForm
from config import Config
from project.map1 import map_
from logic1 import Game
from operator import add, sub

app = Flask(__name__)
app.config.from_object(Config)

menu = [
    {'name': 'home', 'url': '/'},
    {'name': 'info', 'url': '/info'},
    {'name': 'profile', 'url': '/'}
]

way_op = {0: add, 1: add, 2: sub, 3: sub}

@app.route('/', methods=['get', 'post'])
def home():
    a = Game(map_)
    a.choose_init()
    print('**********', a.cache)
    return render_template('home.html',
                           menu=menu)

@app.route('/game', methods=['get', 'post'])
def game():
    a = Game()
    cache = a.cache

    form = MyForm()
    if form.validate_on_submit():
        way = form.way.data
        steps = form.number_steps.data
        a.change_location(way, steps)

    if cache[len(cache) - 1]['name'] == 'Garden':
        return redirect('/game_over')


    return render_template('game.html',
                           menu=menu,
                           form=form,
                           cache=cache,
                           no_way=a.no_way)

@app.route('/game_over')
def game_over():
    a = Game()
    cache = a.cache
    return render_template('game_over.html',
                           menu=menu,
                           cache=cache)

@app.route('/info')
def info():
    return render_template('info.html', menu=menu)

if __name__ == '__main__':
    app.run()