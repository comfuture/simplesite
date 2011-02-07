import re
from flask import Module, render_template, request, redirect, url_for
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
    exclude_ptn = re.compile(r'/\*$')
    name = re.sub(exclude_ptn, u'', name)
    board = get_board(name)
    if board is None:
        return 'board not exists', 404
    context = {'board': board}
    return render_template('board/list.html', **context)

def init_plugin():
    def embed_board(p):
        p.content = p.content.replace('t', 'f')

    add_filter(embed_board)

@module.route('/<path:name>/+', methods=['GET', 'POST'])
def create(name):
    board = get_board(name)
    if not board:
        return "board not exists", 404
    if request.method == 'GET':
        return render_template('board/create.html', name=name)
    elif request.method == 'POST':
        article = BoardArticle(group=board,
            subject=request.form.get('subject', ''),
            content=request.form.get('content', ''),
            author=request.form.get('author', ''))
        session.commit()
        return redirect(url_for('view', name=name, id=article.id))

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
