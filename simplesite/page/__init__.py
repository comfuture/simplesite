from flask import Module, render_template
from model import *
from simplesite import board

module = Module(__name__)

def find_one(path):
    page = Page.query.filter_by(path=path).first()
    return page

def render(page):
    context = {'page': page}
    return render_template('page/view.html', **context)

@module.route('/<path:path>')
def view(path):
    page = find_one(path)
    if page is None:
        return '404 Not Found', 404
    return render(page)

@module.route('/admin/')
def admin_index():
    return 'this is page admin main'

