from flask import Module, render_template
from ..model import *
from model import *

module = Module(__name__)

def get_board(name):
    board = Board.query.filter_by(name=name).first()
    return board

def get_article(name, id):
    board = get_board(name)
    article = BoardArticle.query.filter_by(group=board, id=id).first()
    return board, article

@module.route('/<path:name>/*')
def list(name):
    board = get_board(name)
    if board is None:
        return 'board not exists', 404
    context = {'board': board}
    return render_template('board/list.html', **context)

@module.route('/<path:name>/', methods=['POST'])
def post(name):
    return ''

@module.route('/<path:name>/+')
def form(name):
    return ''

@module.route('/<path:name>/@<int:id>')
def view(name, id):
    board, article = get_article(name, id)
    if not board or not article:
        return 'article not found', 404
    context = {'board': board, 'article': article}
    return render_template('board/view.html', **context)

@module.route('/<path:name>/@<int:id>', methods=['POST', 'PUT'])
def modify(name, id):
    return ''

@module.route('/<path:name>/@<int:id>', methods=['DELETE'])
def delete(name, id):
    return ''
