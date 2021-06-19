from mastermind import controllers
from flask import Blueprint, render_template, redirect, request
import mastermind

web = Blueprint('web', __name__, static_folder='static', template_folder='templates')

@web.route('/')
def index():
    if mastermind.mastermind_game.player == None:
        return redirect('/load')

    myData = controllers.HomeController.index()

    return render_template('index.html', data=myData)

@web.route('/leaderboard')
def leaderboard():
    myData = controllers.LeaderboardController.index()
    
    return render_template('leaderboard.html', data=myData)

@web.route('/load')
def load():
    myData = controllers.LoadController.index()
    
    return render_template('load.html', data=myData)

@web.route('/setting')
def setting():
    myData = controllers.LoadController.index()
    
    return render_template('setting.html', data=myData)


@web.route('/load-username')
def load_username():
    username = request.args.get('username')
    mastermind.mastermind_game.setPlayer(username)

    return redirect('/')

@web.route('/', defaults={'path': ''})
@web.route('/<path:path>')
def catch_all(path):
    return redirect('/') 