from flask import Module, request, render_template, make_response, url_for, redirect
from model import *
from sqlalchemy.exc import IntegrityError
from simplesite import board

module = Module(__name__)
filters = []

def add_filter(fn):
    filters.append(fn)

def find_one(path):
    page = Page.query.filter_by(path=path).first()
    return page

@module.route('/+', methods=['GET', 'POST'])
def create():
    if request.method == 'GET':
        return render_template('page/create.html')
    elif request.method == 'POST':
        page = Page(path=request.form.get('path'),
            subject=request.form.get('subject'),
            content=request.form.get('content'),
            author=request.form.get('author'))
        try:
            session.commit()
            """
            # TODO: implement 201 Created redirect
            resp = make_response('201 Created', 201)
            resp.headers['Location'] = url_for('view', path=page.path)
            return resp
            """
            return redirect(url_for('view', path=page.path))
        except IntegrityError, e:
            session.rollback()
            return 'Duplicated entry', 409

@module.route('/<path:path>')
def view(path):
    page = find_one(path)
    if page is None:
        return '404 Not Found', 404
    if request.values.has_key('edit'):
        return render_template('page/modify.html', page=page)
    page = PageProxy(page)

    def a(p):
        p.content = p.content.replace('t','f')
    #add_filter(a)
    for filter in filters:
        filter(page)
    return render_template('page/view.html', page=page)

@module.route('/<path:path>', methods=['PUT', 'POST'])
def modify(path):
    page = find_one(path)
    if page:
        page.subject = request.form.get('subject', '')
        page.content = request.form.get('content', '')
        page.author  = request.form.get('author' , '')
        session.commit()
        return redirect(url_for('view', path=path))
    return "403 Method not allowed", 403

@module.route('/<path:path>', methods=['DELETE'])
def delete(path):
    page = find_one(path)
    if page:
        page.delete()
        session.commit()
        return redirect('/', 301)
