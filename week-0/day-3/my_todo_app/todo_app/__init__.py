import os

from flask import Flask
from flask import request


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that list my todos
    def todo_view(todos):
        view='List of My Todos'+'<br/>'
        for todo in todos:
            view+=(todo+'<br/>')
        
        view += '----LIST ENDS HERE---'
        return view

    def get_todo_list(name):
        if name=='shankar':
            return ['Go Home','Last Day Tomorrow']
        elif name == 'shivang':
            return ['Study Hard','Get Highest Package']
        elif name == 'sonu':
            return ['Be the best','Be mature']
        elif name == 'abhishek':
            return ['Play','Enjoy and be the best']
        else:
            return []

    @app.route('/todos')
    def todos():
        name = request.args.get('name')
        print('-------')
        print(name)
        print('-------')
        person_todo_list = get_todo_list(name)
        return todo_view(person_todo_list)

    return app

