import mastermind
from flask import render_template

def index():
    myData = {
        'name': 'Jacky',
        'pets': ['doggo', 'cat', 'fish']
    }

    return render_template('leaderboard.html', data=myData)

